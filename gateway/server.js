const app = require('./app');
const dotenv = require('dotenv');

dotenv.config();

const PORT = process.env.PORT || 4001;

app.listen(PORT, () => {
    console.log(`API Gateway corriendo en http://localhost:${PORT}`);
    console.log(`Endpoints disponibles: /movies, /actors, /reviews, /users`);
});