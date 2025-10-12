const User = require('../models/User');

const userResolvers = {
    Query: {
        //obtener todos los usuarios
        allUsers: async () => {
            return await User.getAll();
        },
        //obtener usuario por id
        userById: async (_, { id }) => {
            return await User.getById(id);
        },
    },

    Mutation: {
        //crear usuario
        createUser: async (_, { name, email }) => {
            return await User.create(name, email);
        },
        //actualizar usuario
        updateUser: async (_, { id, name, email }) => {
            return await User.update(id, name, email);
        },
        //eliminar usuario
        deleteUser: async (_, { id }) => {
            const result = await User.delete(id);
            return result ? "Usuario eliminado exitosamente" : null;
        },
    },
};

module.exports = userResolvers;