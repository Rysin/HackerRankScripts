import typer

# Create typer app

sd = typer.Typer()


@sd.command()
def hello(name):
    typer.echo(f'Hello {name}', color='red')
    return None


@sd.command()
def squareIt(num):
    typer.echo(f'Sqaure = {int(num) ** 2}')


if __name__ == '__main__':
    sd()
