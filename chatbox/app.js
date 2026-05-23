const express = require ('express');       //always require when you download something from git bash
const path = require('path');
const ejsMate = require('ejs-mate');         //require ejs-mate to use it as the engine for our app
const expressLayouts = require('express-ejs-layouts');   //require express-ejs-layouts to use it as the engine for our app



const app = express();                           //allowing the app to use express as a function

app.engine("ejs", ejsMate);
app.set("view engine", "ejs");              //telling the app to use ejs as the view engine
app.set("views", path.join(__dirname, "views"));   //telling the app where to find the views folder
app.set("layout", "layouts/boilerplate");                 //telling the app to use the layout.ejs file as the layout for all the views


app.use(expressLayouts);                    //telling the app to use express-ejs-layouts as the layout engine for our app
app.set("layout", "layouts/boilerplate");                 //telling the app to use the layout.ejs file as the layout for all the views

app.get("/", (req, res) => {
    res.render("home")
});


//code to host the server 
app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});

