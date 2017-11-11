import click
import pygit2


@click.command()
@click.option('-X', 'strategy_option', type=click.Choice(['ours', 'theirs']), help="The strategy to use")
@click.argument("path", type=str)
def cli():
    """Resolve the conflicts in a sub-tree by applying the specified strategy.
    """
    pass
