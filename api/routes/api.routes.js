const express = require('express');
const router = express.Router();

const apiController = require('../controllers/api.controller.js');

router.get('/test', apiController.test);

module.exports = router;