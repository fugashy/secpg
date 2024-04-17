import socket
import time

import click
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


@click.group(help="A sample for sending and receiving data "
        "using Public Key Crypto System.")
def pkcs():
    pass


@pkcs.command()
@click.argument("key_path", type=str)
@click.option("--ipaddr", type=str, default="127.0.0.1", show_default=True)
@click.option("--port", type=int, default=48273, show_default=True)
@click.option("--rate", type=float, default=1.0, show_default=True)
@click.option(
        "--msg",
        type=str,
        default="hello encryption !",
        show_default=True)
def client(key_path, ipaddr, port, rate, msg):
    with open(key_path, "rb") as f:
        key = RSA.import_key(f.read())

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time.sleep(rate)

        cipher = PKCS1_OAEP.new(key)
        encrypted_msg = cipher.encrypt(msg.encode())

        print(f"          msg: {msg}")
        print(f"encrypted msg: {encrypted_msg}")

        client.sendto(encrypted_msg, (ipaddr, port))

    client.close()


@pkcs.command()
@click.argument("key_path", type=str)
@click.option("--ipaddr", type=str, default="127.0.0.1", show_default=True)
@click.option("--port", type=int, default=48273, show_default=True)
def server(key_path, ipaddr, port):
    with open(key_path, "rb") as f:
        key = RSA.import_key(f.read())

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ipaddr, port))

    while True:
        encrypted_msg, client_ipaddr = server.recvfrom(1024)
        cipher = PKCS1_OAEP.new(key)
        print(f"encrypted from {client_ipaddr}:\n{encrypted_msg}")

        msg = cipher.decrypt(encrypted_msg).decode()
        print(f"msg from {client_ipaddr}:\n{msg}")
