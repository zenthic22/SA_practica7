const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const dotenv = require('dotenv');

dotenv.config();

const app = express();

app.use('/api/actors', createProxyMiddleware({
  target: process.env.ACTORS_SERVICE,
  changeOrigin: true,
  pathRewrite: { '^/api/actors': '/actors' }
}));

app.use('/api/movies', createProxyMiddleware({
  target: process.env.MOVIES_SERVICE,
  changeOrigin: true
}));

app.use('/api/reviews', createProxyMiddleware({
  target: process.env.REVIEWS_SERVICE,
  changeOrigin: true,
  pathRewrite: { '^/api/reviews': '/reviews' }
}));

app.use('/api/users', createProxyMiddleware({
  target: process.env.USERS_SERVICE,
  changeOrigin: true,
  pathRewrite: { '^/api/users': '/users' }
}));

// health
app.get('/healthz', (_req, res) => res.status(200).send('ok'));

module.exports = app;