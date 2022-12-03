FROM node:19-slim as build

WORKDIR /app

COPY ./package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM node:alpine3.15

WORKDIR /app
COPY --from=build /app/dist /app 