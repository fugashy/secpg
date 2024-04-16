import click
from Crypto.Random import get_random_bytes
from Crypto import Random
from Crypto.PublicKey import RSA


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


@genkey.command()
@click.option("--bit_length", type=int, default=2048, show_default=True)
@click.option(
        "--output_path_pub",
        type=str,
        default="/tmp/rsa_pub.pem",
        show_default=True)
@click.option(
        "--output_path",
        type=str,
        default="/tmp/rsa.pem",
        show_default=True)
def rsa(bit_length, output_path_pub, output_path):
    rand_gen = Random.new().read
    key = RSA.generate(bit_length, rand_gen)
    pub_key = key.publickey()

    with open(output_path_pub, "wb") as f:
        f.write(pub_key.export_key())
    with open(output_path, "wb") as f:
        f.write(key.export_key())

    print(f"generate {output_path_pub} and {output_path}")
