FROM python:3.12-alpine

LABEL creator="Roman Ivanov"
LABEL email="sitdoff@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN flask --app application.main db upgrade

CMD ["python", "-m", "flask", "--app", "application.main", "run", "--host=0.0.0.0", "--port=8000"]
