FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir google

COPY presents.py .

ENTRYPOINT [ "python", "presents.py" ]
