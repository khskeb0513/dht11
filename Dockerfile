FROM python:3.9-alpine

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN /usr/local/bin/python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["/usr/local/bin/python3", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
