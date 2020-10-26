const express = require("express");
const port = 3000
const app = express();

app.get('/', (req, res) => {
  res.send('hello world')
})

//Start server
app.listen(port, () => {
    console.log('Listening at port %d (http://localhost:%d)',port,port)
})
