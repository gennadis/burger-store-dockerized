FROM node:18

WORKDIR /usr/src/app

COPY package.json package-lock.json ./
COPY bundles-src ./bundles-src

RUN npm ci --include=dev
