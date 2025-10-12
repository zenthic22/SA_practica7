const db = require('../config/db');

class Actor {
    constructor(id, name, birth_year) {
        this.id = id;
        this.name = name;
        this.birth_year = birth_year;
    }

    //obtener todos los actores
    static async getAll() {
        const [rows] = await db.query("SELECT * FROM actors");
        return rows.map((row) => new Actor(row.id, row.name, row.birth_year));
    }

    //obtener actor por su id
    static async getById(id) {
        const [rows] = await db.query("SELECT * FROM actors WHERE id = ?", [id]);
        if (rows.length === 0) return null;
        const row = rows[0];
        return new Actor(row.id, row.name, row.birth_year);
    }

    //crear un nuevo actor
    static async create(name, birth_year) {
        const [result] = await db.query(
            "INSERT INTO actors (name, birth_year) VALUES (?, ?)",
            [name, birth_year]
        );
        return result.insertId;
    }

    //actualizar un actor
    static async update(id, name, birth_year) {
        await db.query(
            "UPDATE actors SET name = ?, birth_year = ? WHERE id = ?",
            [name, birth_year, id]
        );
    }

    //eliminar un actor
    static async delete(id) {
        await db.query("DELETE FROM actors WHERE id = ?", [id]);
    }
}

module.exports = Actor;