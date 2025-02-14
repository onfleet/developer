const express = require('express');
const app = express();
const port = 3000;
const bodyParser = require('body-parser')

//const fs = require('node:fs');

var jsonParser = bodyParser.json()

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

//GET method query validation
app.get("/webhooks", (req, res) => {
  res.status(200).send(req.query.check);
  //console.log(req.query.check);
})

app.post("/webhooks", jsonParser, (req, res) => {
  res.status(200).send(req.query.check);
  var content = JSON.stringify(req.body.data) + '';
  console.log(content); //the webhook payload

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
})