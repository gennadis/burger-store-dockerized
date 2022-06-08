FROM node:18

WORKDIR /home/burger/web

COPY package.json package-lock.json ./
COPY bundles-src ./bundles-src

RUN npm ci --include=dev

RUN ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
