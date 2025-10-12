const express = require('express');
const actorRouter = require('./routes/actorRoutes');

async function createApp() {
    const app = express();

    app.use(express.json());
    app.use("/actors", actorRouter);
    app.get("/healthz", (_req, res) => res.status(200).send('ok'));
    return app;
}

module.exports = createApp;