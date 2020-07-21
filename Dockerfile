FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/api
WORKDIR /app/api
ADD . /app/api/
RUN pip3 install --upgrade pip -r requirements.txt
ENV API_PORT 8000
