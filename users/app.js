const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const { typeDefs, resolvers } = require('./schema/userSchema');

async function createApp() {
    const app = express();

    //crear el servidor Apollo
    const server = new ApolloServer({
        typeDefs,
        resolvers,
    });

    await server.start();

    //middleware para GraphQL
    server.applyMiddleware({ app, path: '/users' });

    app.get('/healthz', (_req, res) => res.status(200).send('ok'));

    return app;
}

module.exports = createApp;