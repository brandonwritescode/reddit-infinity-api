const express = require("express");

const app = express();

app.get("/", (request, response) => {
    response.json({"message":"Welcome to the home page"});
});

app.listen(8080, "localhost", () => {
    console.log(`Server running at http://localhost:8080`);
});