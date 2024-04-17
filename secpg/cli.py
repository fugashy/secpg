import click

from .genkey import genkey
from .skes import skes
from .pkcs import pkcs


@click.group()
def secpg():
    pass


def main():
    commands = [
            genkey,
            skes,
            pkcs,
            ]
    [secpg.add_command(c) for c in commands]

    secpg()

