FROM node:22.14.0 as build

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Step 2: nginx container
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html