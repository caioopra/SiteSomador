const express = require("express");
const path = require("path");
const app = express();

app.use(express.static("public"));

app.get("/", (req, res) => {
    console.log("Request to frontend");
    res.sendFile(path.join(__dirname+"/views/index.html"));
});

app.listen(3000, () => {
    console.log("NGINX server starting");
});

