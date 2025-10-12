const Actor = require('../models/Actor');

//obtener todos los actores
exports.getAllActors = async (req, res) => {
    try {
        const actors = await Actor.getAll();
        res.json(actors);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

//obtener un actor por id
exports.getActorById = async (req, res) => {
    const { id } = req.params;
    try {
        const actor = await Actor.getById(id);
        if (actor) {
            res.json(actor);
        } else {
            res.status(404).json({ message: "Actor no encontrado" });
        }
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

//crear un nuevo actor
exports.createActor = async (req, res) => {
    const { name, birth_year } = req.body;
    try {
        const newActorId = await Actor.create(name, birth_year);
        res.status(201).json({ message: "Actor creado exitosamente", id: newActorId });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

//actualizar un actor
exports.updateActor = async (req, res) => {
    const { id } = req.params;
    const { name, birth_year } = req.body;
    try {
        await Actor.update(id, name, birth_year);
        res.json({ message: "Actor actualizado exitosamente" });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

//eliminar un actor
exports.deleteActor = async (req, res) => {
    const { id } = req.params;
    try {
        await Actor.delete(id);
        res.json({ message: "Actor eliminado exitosamente" });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
}