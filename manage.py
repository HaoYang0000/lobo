#! /usr/bin/env python
from alembic.config import Config as alembic_config_class
from alembic import command as alembic_command
import click
import sys
import os
import logging
import app.main as main
import libs.config as config
import xconfig
from subprocess import call


# pep8 setup
cwd = os.path.dirname(os.path.realpath(__file__))
_pep8_excluded_patterns = []

# alembic setup
alembic_config = alembic_config_class('db/alembic.ini')


@click.group()
def cli():
    pass


@click.command()
def run():
    """
    Fire it up.
    """
    app = main.create_app()
    logger = logging.getLogger()
    logger.debug("Running on 127.0.0.1:8732")
    app.run(
        host="127.0.0.1",
        port=8732
    )


@click.command()
def shell():
    """
    Create a flask shell
    """
    import code
    app = main.create_app()
    with app.app_context():
        from flask.globals import _app_ctx_stack
        app = _app_ctx_stack.top.app
        ctx = {}
        ctx.update(app.make_shell_context())
        code.interact(local=ctx)


@click.command()
def pep8():
    """
    pep8 check the repo. Will exit with 1 on failure.
    """
    import pycodestyle
    # pycode requires full paths
    exclude = ["{cwd}/{pattern}".format(
        cwd=cwd,
        pattern=pattern
    ) for pattern in _pep8_excluded_patterns]
    style = pycodestyle.StyleGuide(config_file='./tox.ini', exclude=exclude)
    report = style.check_files('.')
    print("Errors: {}".format(report.get_count()))
    # this ensures we can programmatically determine failures
    if report.get_count() > 0:
        sys.exit(1)


@click.command()
def flake8():
    """
    flake8 check the repo.
    """
    call(["flake8"])


# namespace for db commands
@click.group()  # noqa
def db():
    """ Schema related commands.
    """
    pass


@db.command()
@click.option(
    '--revision',
    default='head',
    help="the revision to upgrade to. defaults to head."
)
@click.option('--sql', is_flag=True)
def upgrade(revision, sql):
    """ Upgrade database to a revision
    """
    alembic_command.upgrade(alembic_config, revision, sql=sql)


@db.command()
@click.option(
    '--revision',
    required=True,
    help="the revision to downgrade to."
)
@click.option('--sql', is_flag=True)
def downgrade(revision, sql):
    """ Downgrade database to a revision
    """
    alembic_command.downgrade(alembic_config, revision, sql=sql)


@db.command()
@click.option(
    '--message',
    '-m',
    required=True,
    help="description of this schema change."
)
def revision(message):
    """ Generate a schema change from model changes
    """
    alembic_command.revision(
        alembic_config,
        message=message,
        autogenerate=True
    )


@db.command()
def current():
    """ Downgrade database to a revision
    """
    alembic_command.current(alembic_config, verbose=True)


cli.add_command(run)
cli.add_command(shell)
cli.add_command(pep8)
cli.add_command(flake8)
cli.add_command(db)

if __name__ == '__main__':
    cli()
