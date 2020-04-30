const https = require('https');

exports.test = (req, res) => {
    res.json({"message": "This is a test endpoint. If you are seeing this is means the application is working."})
}