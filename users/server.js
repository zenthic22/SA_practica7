const createApp = require('./app');
const dotenv = require('dotenv');

dotenv.config();

const PORT = process.env.PORT || 5003;

async function startServer() {
    const app = await createApp();

    app.listen(PORT, '0.0.0.0', () => {
        console.log(`Servidor users corriendo en puerto ${PORT}`);
        console.log(`GraphQL disponible en http://localhost:${PORT}/users`);
    });
}

startServer()