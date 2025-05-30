FROM node:22.14.0-alpine

WORKDIR /app/frontend

# 의존성 설치 및 빌드
COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend .
RUN npm run build

#Vite 용
# CMD [ "npm", "run", "build" ] 위의 