FROM node:20-alpine

WORKDIR /app/frontend/

COPY package.json package-lock.json ./
RUN npm ci
COPY . .

CMD ["npm", "start"]
