import typer
from io import BytesIO
from datetime import date, datetime
import httpx
from config import api_url
from PIL import Image

# Create typer app
sd = typer.Typer()

COUNT: int = 1
today: str = str(date.today())
image_formats: list = ['jpg', 'png', 'jpeg', 'tiff', 'bmp']


@sd.command()
def hello(name):
    typer.echo(f'Hello {name}', color=True)
    return None


@sd.command()
def squareIt(num):
    typer.echo(f'Sqaure = {int(num) ** 2}')


@sd.command()
def fetchImage(date: datetime = today):
    query = f"{api_url}&count={COUNT}"
    print(f'QUERY : {query}')

    resp = httpx.get(query)
    print(f'status code : {resp.status_code}')
    resp.raise_for_status()
    data = resp.json()[-1]
    print(f'DATA : {type(data)} \n {data}')

    print(data.keys())

    img_url = data.get('hdurl')
    title = data.get('title')

    img_name = img_url.split('//')[-1]
    ext = img_name.split('.')[-1]

    print(f'EXT : {ext}')

    if ext not in image_formats:
        print('Not An Image')
    else:
        img = httpx.get(img_url)
        image = Image.open(BytesIO(img.content))
        image.show()


if __name__ == '__main__':
    sd()
