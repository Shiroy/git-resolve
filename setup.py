from setuptools import setup

setup(
    name='git_resolve',
    version='0.1',
    py_modules=['git_resolve'],
    install_requires=[
        'Click',
        'pygit2'
    ],
    entry_points='''
        [console_scripts]
        git-resolve=git_resolve.main:cli
    ''',
)