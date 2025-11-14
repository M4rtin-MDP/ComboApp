FROM node:20.19-alpine

ENV NODE_ENV=development

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY .env* ./
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
