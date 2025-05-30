# 1단계: Node로 빌드
FROM node:22.14.0-alpine AS build

WORKDIR /app

COPY ./package*.json ./
RUN npm install

COPY ./ .
RUN npm run build


# 2단계: Nginx로 정적 파일 서빙
FROM nginx:stable-alpine

# 기본 설정 제거 (sites-enabled 디렉토리는 Debian 계열, Alpine에선 필요 없음)
# RUN rm -rf /etc/nginx/sites-enabled/default  <- Alpine에는 해당 디렉토리 없음. 제거 OK.

# Nginx 설정 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 정적 파일 복사
COPY --from=build /app/dist /usr/share/nginx/html

# frontend 포트
EXPOSE 3000

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
