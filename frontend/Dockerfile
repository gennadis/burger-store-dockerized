FROM node:18-alpine3.14

WORKDIR /usr/src/app

COPY package.json package-lock.json ./
COPY bundles-src ./

RUN npm ci --include=dev
RUN ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
