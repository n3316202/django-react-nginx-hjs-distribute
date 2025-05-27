FROM python:3.12-slim

WORKDIR /app/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn  # ✅ 이 줄이 꼭 필요

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
