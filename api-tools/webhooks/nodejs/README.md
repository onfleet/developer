## Synopsis

Endpoints for each Onfleet webhook trigger. Validate the webhook and print payload to screen. For more information Please see [here](https://docs.onfleet.com/reference/validation)

## Installation
Require node and express
May require bodyParser

1. Install node and npm
2. ```npm install express```
3. Optional: ```npm install body-parser```

### Use 

1. Start node server by use ```node webhookserver.js``` in terminal
2. Expose to the wider internet ( if using ngrok: start ngrok server ) 
3. Create a webhook for your trigger event, using the path from the table below as your webhook URL.