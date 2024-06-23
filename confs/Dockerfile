# Stage 1: Build the application and install dependencies
# FROM python:3.9 AS builder
# EXPOSE 443/tcp
# RUN apt-get update && apt-get install vim -y &&\
    # python3 -m pip install --upgrade pip
# WORKDIR /project
# COPY /weather_app/weather_app /project
# RUN pip install -r ./requirements.txt
# EXPOSE 8003/tcp

# Stage 2: Deploy the application
# FROM builder AS deploy
# COPY start_gunicorn_server.sh /project/
# WORKDIR /project
# RUN chmod +x start_gunicorn_server.sh
# ENTRYPOINT ["bash", "start_gunicorn_server.sh"]


#   Build: install all requirements for the app
FROM python:3.9 as build

#   Env so python doesnt download them
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -m -r -s /bin/bash weatheruser

WORKDIR /project

COPY /weather_app/weather_app /project

RUN pip install --no-cache-dir -r ./requirements.txt


#   Deploy: Copy all required files to project directory and run gunicorn script
FROM python:3.9-slim as deploy

WORKDIR /project

COPY start_gunicorn_server.sh /project/

USER root

RUN chmod +x start_gunicorn_server.sh
RUN adduser -u 8877 weatheruser

COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=build /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY /weather_app/weather_app /project

RUN chown -R weatheruser:weatheruser /project

USER weatheruser

ENTRYPOINT ["bash", "start_gunicorn_server.sh"]
