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


#python manage.py makemigrations --no-input
python manage.py migrate --no-input

# ✅ Django 마이그레이션 및 static 파일 수집
python manage.py collectstatic --no-input #dev_6_2


#dev_6_4 커맨드 객체 추가
# ✅ 슈퍼유저 생성
echo "👤 Creating superuser..."
python manage.py superuser || echo "⚠️  Superuser creation skipped or failed."
echo "✅ Superuser 처리 완료"


# ✅ 명령어 실행
exec "$@"
