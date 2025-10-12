FROM node:18-bullseye-slim

ENV NODE_ENV=production
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates dumb-init \
  && rm -rf /var/lib/apt/lists/*

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 4000

ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "server.js"]