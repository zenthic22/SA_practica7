const db = require('../config/db');

class User {
    constructor(id, name, email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    //obtener todos los usuarios
    static async getAll() {
        const [rows] = await db.query("SELECT * FROM users");
        return rows.map(row => new User(row.id, row.name, row.email));
    }

    //obtener usuario por id
    static async getById(id) {
        const [rows] = await db.query("SELECT * FROM users WHERE id = ?", [id]);
        if (!rows.length) return null;
        const row = rows[0];
        return new User(row.id, row.name, row.email);
    }

    //crear usuario
    static async create(name, email) {
        const [result] = await db.query(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            [name, email]
        );
        return await this.getById(result.insertId);
    }

    //actualizar usuario
    static async update(id, name, email) {
        await db.query("UPDATE users SET name = ?, email = ? WHERE id = ?", [name, email, id]);
        return await this.getById(id);
    }

    //eliminar usuario
    static async delete(id) {
        await db.query("DELETE FROM users WHERE id = ?", [id]);
        return true;
    }
}

module.exports = User;