FROM node:14.18.1-alpine

WORKDIR /app/frontend

COPY package.json /app/frontend

RUN npm install -g npm@8.1.1
RUN npm install
ENV REACT_APP_ENVIRONMENT="development"
COPY . /app/frontend/
RUN npm run build

FROM nginx:1.17.10-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=0 /app/frontend/build /var/www/html
