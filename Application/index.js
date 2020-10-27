const express = require("express");
//Port number is constant and declared in here.
const port = 3000

// the below gives us a variable we can use to run all the methods that are in the express library
const app = express();

app.set('title', 'hacktoberfest');

app.get('/', (req, res) => {
  res.send('hello world')
})

//Start server
app.listen(port, () => {
 //console.log() prints output
    console.log('Listening at port %d (http://localhost:%d)',port,port)
})

//get time
app.get('/time', (req, res) => {
  	res.send(Date.now())
})
