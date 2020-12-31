// Importing the modules.
const express = require("express");
const bodyParser = require("body-parser");

// Creating the objects.
var app = express();
var router = express.Router();

//Enabling the app to use body urls.
app.use(bodyParser.urlencoded({ extended: false }));

// Handling the request.

router.get("/", (req, res) => {
    var my_name = req.query.name;
    res.send("This is a GET Request. My name is " + my_name);
});

router.post("/", (req, res) => {
    var my_name = req.body.name;
    res.send("This is a POST request. My name is " + my_name);
});

// Enablle the use of router.
app.use("/", router);

// Starting the server
app.listen(5000, () => {
    console.log("Server started at PORT: 5000");
});
