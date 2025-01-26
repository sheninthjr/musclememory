FROM node:18-alpine

WORKDIR /usr/app

COPY package*.json tsconfig.json ./

RUN npm install

COPY . .

RUN npx prisma generate

EXPOSE 3003

CMD ["npm","run","dev"]