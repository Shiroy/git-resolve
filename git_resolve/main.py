import click
import os
import pygit2


def in_directory(directory, file):
    return os.path.commonpath([directory, file]) == directory


@click.command()
@click.option('-X', 'strategy_option', type=click.Choice(['ours', 'theirs']), help="The strategy to use")
@click.argument('path', type=click.Path(exists=True))
@click.pass_context
def cli(ctx: click.Context, strategy_option, path):
    """Resolve the conflicts in a sub-tree by applying the specified strategy.
    """

    repo_path = os.path.abspath('.git')
    target_dir = os.path.abspath(path)

    if not os.path.exists(repo_path):
        click.echo("Not a git repository", err=True)
        ctx.exit(1)

    repo = pygit2.Repository(repo_path)

    merge_commit = None
    try:
        merge_commit = repo.revparse_single('MERGE_HEAD')
    except KeyError as e:
        click.echo("There is no merge conflict to solve", err=True)
        ctx.exit(1)

    head_commit = repo.revparse_single("HEAD")

    ancestor = repo.merge_base(head_commit.id, merge_commit.id)
    merged_index = repo.merge_trees(ancestor, head_commit.id, merge_commit.id, favor=strategy_option)

    assert not merged_index.conflicts

    repo_index = repo.index
    repo_index.read()

    file_to_update = [file for file in merged_index if in_directory(target_dir, os.path.abspath(file.path))]

    for f in file_to_update:
        full_path = os.path.abspath(f.path)
        with open(full_path, 'wb') as fd:
            fd.write(repo[f.id].data)
