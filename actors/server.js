const createApp = require('./app');
const dotenv = require('dotenv');

dotenv.config();

const PORT = process.env.PORT || 4000;

async function startServer() {
    const app = await createApp();

    app.listen(PORT, () => {
        console.log(`Servidor actors corriendo en puerto ${PORT}`);
    });
}

startServer();