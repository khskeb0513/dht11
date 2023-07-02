from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from . import readSerial

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    parsed = readSerial.parsed
    parsed.update({'request': request})
    return templates.TemplateResponse('index.html', parsed)


@app.get('/raw')
async def raw():
    return readSerial.latest_line


@app.get('/json')
async def json():
    return readSerial.parsed
