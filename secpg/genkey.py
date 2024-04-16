import click
from Crypto.Random import get_random_bytes


@click.group(help="Generate keys for encryption and decryption")
def genkey():
    pass


@genkey.command()
@click.option("--length", type=int, default=32, show_default=True)
@click.option(
        "--output_path",
        type=str,
        default="/tmp/random.txt",
        show_default=True)
def random(length, output_path):
    with open(output_path, "wb") as f:
        f.write(get_random_bytes(length))
    print(f"generate keyfile {output_path}")
