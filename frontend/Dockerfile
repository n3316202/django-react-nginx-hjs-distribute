FROM node:22.14.0-alpine

WORKDIR /app/frontend

# 의존성 설치 및 빌드
COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend .
RUN npm run build

# serve 설치 (정적 파일 서빙용)
#RUN npm install -g serve

# 정적 파일 서빙
#CMD ["serve", "-s", "dist", "-l", "3000"]