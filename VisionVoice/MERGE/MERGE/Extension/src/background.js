// import axios from 'axios';
// const axios = require('axios');
// import axios from 'axios';


let shouldReadContent = false;
let currentSection = '';

// background.js
self.addEventListener('install', event => {
    console.log('Service worker installed');
});
  
self.addEventListener('activate', event => {
console.log('Service worker activated');
});

self.addEventListener('fetch', event => {
console.log('Service worker fetching');
});
  

// Function to open the extension window
function openExtensionWindow() {
    chrome.windows.create({
        url: 'index.html',
        type: 'popup',
        width: 400, 
        height: 800
    }, function (window) {
        chrome.tabs.onUpdated.addListener(function onTabUpdated(tabId, changeInfo, updatedTab) {
            if (tabId === window.tabs[0].id && changeInfo.status === 'complete') {
                // Start speech recognition when the extension window is fully loaded
                // startSpeechRecognition();
                chrome.tabs.onUpdated.removeListener(onTabUpdated);
            }
        });
    });
}

// Open the extension window when the extension is first installed or updated
chrome.runtime.onInstalled.addListener(function() {
    openExtensionWindow();
});

//open extension window if it's not open on startup
chrome.runtime.onStartup.addListener(function() {
    chrome.windows.getAll({ populate: true }, function(windows) {
        let isExtensionWindowOpen = false;
        for (let i = 0; i < windows.length; i++) {
            if (windows[i].tabs && windows[i].tabs[0].url.includes('index.html')) {
                isExtensionWindowOpen = true;
                break;
            }
        }
        // If extension window is not open, open it
        if (!isExtensionWindowOpen) {
            openExtensionWindow();
        }
    });
});


chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'openNewTab') { 
        console.log('Received openNewTab request');

        // chrome.tabs.create({ url: request.url }, function(tab) { 
        //     console.log('new tab is created', tab.id);

        //     chrome.tabs.onUpdated.addListener(function (updatedTabId, changeInfo, updatedTab) {
        //         if (changeInfo.status === 'complete' && updatedTabId === tab.id) {
        //             console.log('tab is updated');
        //             chrome.tabs.sendMessage(tab.id, { action: 'tabUpdated', url: request.url }, function(response) {
        //                 console.log('Message sent to content script');
        //             });
        //             // chrome.tabs.onUpdated.removeListener(onTabUpdated); // Remove the event listener after it's triggered
        //         }
        //     });
        // });
        
        let sendingURL = request.url.toString();
        console.log('Sending URL:', sendingURL);

        fetch('http://localhost:3000/url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: sendingURL })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from server:', data);
            // Optionally handle the response data
        })
        .catch(error => {
            console.error('Error:', error);
            // Optionally handle the error
        });

        // Return true to indicate that you want to send a response asynchronously
        return true;
    }        
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'userInput') {
        let userInput = request.userInput.toString();
        console.log('Received userInput:', userInput);
        // Process the userInput here
        fetch('http://localhost:3000/user_command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userInput: userInput })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from server:', data);
            // Optionally handle the response data
        })
        .catch(error => {
            console.error('Error:', error);
            // Optionally handle the error
        });

        // Return true to indicate that you want to send a response asynchronously
        return true;
        // ...
    }
});


//read from server
//write to the server
//bifferreader
//try catch
//printreader
//multi threader chat apllication
//client names - bob is connected
//loggers
//create thread
//start thread


