#!/bin/sh

# echo "📌 엔트리포인트 스크립트 시작"

# python manage.py makemigrations --no-input

# python manage.py migrate --no-input

# python manage.py collectstatic --no-input

# exec "$@"

#!/bin/sh

echo "📌 엔트리포인트 스크립트 시작"

# ✅ Django 마이그레이션 및 static 파일 수집
python manage.py makemigrations --no-input
python manage.py migrate --no-input
#python manage.py collectstatic --no-input

# ✅ 명령어 실행
exec "$@"
