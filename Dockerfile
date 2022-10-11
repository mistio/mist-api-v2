FROM mist/api:master

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["uwsgi"]

CMD ["--plugins", "python3", "--http", "0.0.0.0:8080", "--wsgi-file", "mist_api_v2/__main__.py", "--callable", "application", "--master", "--processes", "8", "--max-requests", "100", "--honour-stdin"]
