##### BUILDING STAGE #####
FROM node:18 as build

WORKDIR /usr/src/app

COPY package.json package-lock.json ./
COPY bundles-src ./bundles-src

RUN npm ci --include=dev
RUN ./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"


##### RELEASE STAGE #####
FROM node:18-alpine

COPY --from=build /usr/src/app//node_modules/.bin/ /home/burger/web/node_modules/.bin/
COPY --from=build /usr/src/app/bundles /home/burger/web/bundles
