FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the app user
# RUN mkdir -p /home/django

# create the app user
# RUN addgroup -S django && adduser -S django -G django

ENV HOME=/home/django
RUN mkdir $HOME
ENV APP_HOME=/home/django/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME
# RUN mkdir /code
# RUN mkdir /code/staticfiles
# RUN mkdir /code/mediafiles
# WORKDIR /code
RUN sudo chown -R $USER:$USER .
RUN apt-get update && apt-get install -y gettext libgettextpo-dev zlib1g libjpeg-dev

RUN /usr/local/bin/python -m pip install --upgrade pip
# COPY /code/chat/staticfiles /code/staticfiles
# COPY /code/media /code/mediafiles
COPY Pipfile Pipfile.lock /$APP_HOME/
RUN pip install pipenv && pipenv install --system

# COPY auto_server_f/requirements.txt /scripts/
# RUN pip install --no-cache-dir -r /scripts/requirements.txt

COPY ./code/ $APP_HOME