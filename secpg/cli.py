import click

from .genkey import genkey
from .skes import skes


@click.group()
def secpg():
    pass


def main():
    commands = [
            genkey,
            skes,
            ]
    [secpg.add_command(c) for c in commands]

    secpg()

