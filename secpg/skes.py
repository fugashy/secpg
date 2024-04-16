import socket
import time

import click
from Crypto.Cipher import AES


@click.group(help="A sample for sending and "
        "receiving data using symmetric key encryption.")
def skes():
    pass


@skes.command()
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
        key = f.read()

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        time.sleep(rate)

        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        padding_size = AES.block_size - len(msg) % AES.block_size
        padding = padding_size * chr(padding_size)
        padded_msg = msg + padding
        encrypted_msg = iv + cipher.encrypt(padded_msg.encode())

        print(f"          msg: {msg}")
        print(f"encrypted msg: {encrypted_msg}")

        client.sendto(encrypted_msg, (ipaddr, port))

    client.close()


@skes.command()
@click.argument("key_path", type=str)
@click.option("--ipaddr", type=str, default="127.0.0.1", show_default=True)
@click.option("--port", type=int, default=48273, show_default=True)
def server(key_path, ipaddr, port):
    with open(key_path, "rb") as f:
        key = f.read()

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ipaddr, port))

    while True:
        encrypted_msg, client_ipaddr = server.recvfrom(1024)
        iv = encrypted_msg[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        print(f"encrypted from {client_ipaddr}:\n{encrypted_msg}")

        msg = cipher.decrypt(encrypted_msg[AES.block_size:]).decode()
        padding_size = ord(msg[-1])
        msg = msg[:-padding_size]

        print(f"msg from {client_ipaddr}:\n{msg}")
