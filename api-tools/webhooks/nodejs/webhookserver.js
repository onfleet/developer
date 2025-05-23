const express = require('express');
const escape = require('escape-html');
const app = express();
const port = 3000;
//const fs = require('node:fs');
app.use(express.json());
//GET method query validation
app.get("/webhooks", (req, res) => {
  res.status(200).send(escape(req.query.check));
  //console.log(req.query.check);
})

//POST method for the webhook payload
app.post("/webhooks", (req, res) => {
  const content = JSON.stringify(req.body);
  console.log(content)
  res.sendStatus(200);
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
