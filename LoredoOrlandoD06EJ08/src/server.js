const express = require('express');
const app = express ();

app.get('/', (req, res) =>{
res. send("Welcome to my awesome app!");
});

app. listen (3000, function ( ) {
console. log ("app listening on port 3000");
});

{
  "name": "my-app",
  "version": "1.0",
  "dependencies": {
  "express": "4.18.2"
}
}

