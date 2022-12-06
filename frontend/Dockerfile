FROM node:19-alpine as build

WORKDIR /app

COPY ./package*.json ./

RUN npm install

COPY . .

RUN NODE_ENV=production npm run build

FROM node:19-alpine
WORKDIR /app
COPY --from=build /app/dist /app