#! /usr/bin/env python
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
    try:
        app_config = config.get(xconfig.APP_NAME)
    except IOError as e:
        app_config = {}
        logger.error("Error loading config: {name}".format(name=xconfig.APP_NAME))
        logger.exception(e)
    app.run(
        host=app_config.get("host", "0.0.0.0"),
        port=app_config.get("port", 8088)
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


cli.add_command(run)
cli.add_command(pep8)
cli.add_command(flake8)

if __name__ == '__main__':
    cli()
