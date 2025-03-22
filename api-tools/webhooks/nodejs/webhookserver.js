const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser')
const jsonParser = bodyParser.json()
//const fs = require('node:fs');

//GET method query validation
app.get("/webhooks", (req, res) => {
  res.status(200).send(req.query.check);
  //console.log(req.query.check);
})

//POST method for the webhook payload
app.post("/webhooks", jsonParser, (req, res) => {
  res.status(200).send(req.query.check);
  const content = JSON.stringify(req.body);
  console.log(content)
}) 

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

/*  Only if you want to write it to a local File Directory
//  Set the [Path]    
fs.writeFileSync('[path]', content, err => {
  if (err) {
    console.error(err);
    console.log(content);
  } else {
    // file written successfully
  }
});*/
