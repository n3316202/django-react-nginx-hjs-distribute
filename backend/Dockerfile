FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

