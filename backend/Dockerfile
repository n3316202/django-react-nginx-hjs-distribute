# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app/backend

# requirements.txt 복사 후 의존성 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 소스 전체 복사
COPY . .

# gunicorn 실행, wsgi 경로는 config.wsgi로 가정 (backend/config/wsgi.py)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
