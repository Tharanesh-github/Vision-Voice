const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const api = express();
const port = 3000;

// Middleware to parse JSON bodies
api.use(bodyParser.json());

let user_command = "";
let url = "";

function sendURLToExtension(url) {
  chrome.runtime.sendMessage( 'onlnadlphenfaabogkleohajhoidjkjg', { type: 'url_from_node', url: url });
}

// Route to get the url
api.get('/url', (req, res) => {
  res.json(url);
});

// Route to update the url
api.post('/url', (req, res) => {
  console.log(req.body)
  let new_url = req.body.url;
  url = new_url;
  
  // Execute the Python script using child_process.exec
  exec('python visionnlp/commands.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      // res.status(500).json({ error: 'Error executing Python script' });
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);

    const currentURL = stdout.trim();
    console.log(`URL: ${currentURL}`);
    
    if (currentURL) {
      sendURLToExtension(currentURL);
    }
    // res.status(201).json({ message: 'URL updated successfully'}); 
  });
});

// Route to get the user command
api.get('/user_command', (req, res) => {
  res.json(user_command);
});

// Route to update the user command
api.post('/user_command', (req, res) => {
  console.log(req.body)
  let command = req.body.command;
  user_command = command;
  res.status(201).json({ message: 'User command updated successfully'});
});

// Start the server
api.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

module.exports = {
  startServer: function() {
    api.listen(port, () => {
      console.log(`Server is listening on port ${port}`);
    });
  }
};  