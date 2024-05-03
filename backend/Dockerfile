FROM python:3.8.5-alpine3.12

# Set workdirectory
WORKDIR /usr/src/backend

# Enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gettext

# Install server packages
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev mysql-client mysql-dev \
    && apk add jpeg-dev libwebp-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxml2-dev libxslt-dev libxml2 gettext \
    && pip install --upgrade pip

# Install python packages
COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run the application.
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod 755 /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
