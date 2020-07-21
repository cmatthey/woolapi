FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/api
WORKDIR /app/api
ADD . /app/api/
# COPY wool-api/requirements.txt /app/api/
RUN pip3 install --system --deploy
RUN pipenv
ENV API_PORT 8000
