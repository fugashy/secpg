import click

from .aes import aes


@click.group()
def secpg():
    pass


def main():
    commands = [
            aes,
            ]
    [secpg.add_command(c) for c in commands]

    secpg()

