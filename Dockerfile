FROM python:3 AS build

RUN pip install -U requests

RUN pip install -U pytest

COPY . /usr/src/myapp/

WORKDIR /usr/src/myapp/ 

ENTRYPOINT [ "python", "-m", "pytest" ]