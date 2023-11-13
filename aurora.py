import click
from engine import sx
from engine import sp

@click.group(help="⚡ Aurora-Framework @v0.1.2")
def aurora():
    pass

@aurora.command()
@click.option('--host', required=True, type=str, help='Host for the server.')
@click.option('--port', required=True, type=int, help='Port for the server.')
def server(host, port):
    click.clear()
    sx.Main(host, port)

@aurora.command()
@click.option('--name', required=True, type=str, help='Name for the payload.')
@click.option('--host', required=True, type=str, help='Host for the payload.')
@click.option('--port', required=True, type=int, help='Port for the payload.')
@click.option('--time', required=True, type=int, help='Time for the payload.')
def payload(name, host, port, time):
    click.clear()
    sp.Main(name, host, port, time)

if __name__ == '__main__':
    aurora()
