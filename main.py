"""
Main cli or app entry point
"""

from mylib.calculator import add
import click

import polars as pl
import matplotlib.pyplot as plt
#var=1;var=2

@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    click.echo(add(a, b))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
