const express = require('express');
const router = express.Router();
const actorController = require('../controllers/actorController');

router.get("/listar", actorController.getAllActors);
router.get("/listar/:id", actorController.getActorById);
router.post("/crear", actorController.createActor);
router.delete("/eliminar/:id", actorController.deleteActor);
router.put("/actualizar/:id", actorController.updateActor);

module.exports = router;