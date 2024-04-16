import click


@click.group(help="A sample for sending and "
        "receiving data using symmetric key encryption.")
def aes():
    pass


@aes.command()
@click.argument("key_path", type=str)
@click.option("--ipaddr", type=str, default="127.0.0.1", show_default=True)
@click.option("--port", type=float, default=1.0, show_default=True)
def send(key_path, ipaddr, port):
    pass


@aes.command()
@click.argument("key_path", type=str)
@click.option("--port", type=float, default=1.0, show_default=True)
def recv(key_path, port):
    pass
