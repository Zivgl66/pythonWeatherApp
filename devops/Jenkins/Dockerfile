#   Build: install all requirements for the app
FROM python:3.9 as build

#   Env so python doesnt download them
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -m -r -s /bin/bash weatheruser

WORKDIR /project

COPY /weather_app /project

RUN pip install --no-cache-dir -r ./requirements.txt


#   Deploy: Copy all required files to project directory and run gunicorn script
FROM python:3.9-slim as deploy

WORKDIR /project
COPY /weather_app /project

USER root

RUN ls
RUN chmod +x ./gunicorn_server.sh
RUN adduser -u 8877 weatheruser

COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=build /usr/local/bin/gunicorn /usr/local/bin/gunicorn

RUN chown -R weatheruser:weatheruser /project

USER weatheruser

ENTRYPOINT ["bash", "./gunicorn_server.sh"]