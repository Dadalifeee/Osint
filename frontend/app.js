const express = require('express')
const app = express()
var cors = require('cors')
const port = 3000
const path = require('path');
app.use(express.static('public'));
app.use(cors())

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, '/view/index.html'));
});
