FROM python:3.8
RUN mkdir -p /app/api
WORKDIR /app/api
ADD . /app/api/
RUN pip install --upgrade pip -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV API_PORT 8000
ENV PORT 8000
