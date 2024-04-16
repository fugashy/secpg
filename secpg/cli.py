import click

from .skes import skes


@click.group()
def secpg():
    pass


def main():
    commands = [
            skes,
            ]
    [secpg.add_command(c) for c in commands]

    secpg()

