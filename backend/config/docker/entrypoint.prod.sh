#!/bin/sh

# echo "📌 엔트리포인트 스크립트 시작"

# python manage.py makemigrations --no-input

# python manage.py migrate --no-input

# python manage.py collectstatic --no-input

# exec "$@"

#!/bin/sh

echo "📌 엔트리포인트 스크립트 시작"

# ✅ .env.prod 파일 생성
echo "🔧 .env.prod 파일 생성 중..."
echo "$DJANGO_ENV_PROD_CONTENTS" > /app/backend/.env.prod

# ✅ Django 마이그레이션 및 static 파일 수집
#python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input #dev_6_2

# ✅ 명령어 실행
exec "$@"
