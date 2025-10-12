FROM node:18-bullseye-slim

ENV NODE_ENV=production \
    PORT=5003

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates dumb-init \
    && rm -rf /var/lib/apt/lists/*

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 5003

ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "server.js"]