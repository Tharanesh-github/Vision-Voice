//content.js

// import axios from 'axios';
// import axios from 'axios';

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'tabUpdated') {
        const updatedUrl = request.url;    //url of the cirrent website
        console.log('Received tabUpdated message:', updatedUrl);

        // Identify the website based on the updatedUrl
        if (updatedUrl.includes('mathplanet.com')) {
            console.log('mathplanet website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/mathplanet_links.txt' });
        } else if (updatedUrl.includes('tutorial.math.lamar.edu')) {
            console.log('Pauls online notes website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/paul_links.txt' });
            chrome.runtime.sendMessage({ action: 'goToSectionPaul' });
            // const script = document.createElement('script');
            // script.src = 'webscraper/paul_links.js';
            // document.head.appendChild(script);
        } else if (updatedUrl.includes('oxnotes.com')) {
            console.log('Oxnotes website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/oxnotes_links.txt' });
        } else if (updatedUrl.includes('mathsisfun.com')) {
            console.log('mathsisfun website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/mathsisfun_sections.txt' })
                .then(function(response) {
                    console.log('response:', response);
                })
                .catch(function(error) {
                    console.error('error occured', error);
                });
            chrome.runtime.sendMessage({ action: 'goToSection' });
        } else {
            console.log('Unknown website was opened');
        }

        // return true;
    }
});

// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//     if (request.action === 'openNewTab') { 

//         // let sendingURL = request.url.toString();

//         // axios.post('http://localhost:3000/url', {
//         //     command: sendingURL
//         // })
//         //     .then(response => {
//         //         console.log(response.data);
//         //     })
//         //     .catch(error => {
//         //         console.error(error);
//         //     });
    
//         chrome.tabs.create({ url: request.url }, function(tab) { 
//             console.log('new tab is created', tab.id);

//             chrome.tabs.onUpdated.addListener(function (updatedTabId, changeInfo, updatedTab) {
//                 if (changeInfo.status === 'complete' && updatedTabId === tab.id) {
//                     console.log('tab is updated');
//                     chrome.tabs.sendMessage(tab.id, { action: 'tabUpdated', url: request.url }, function(response) {
//                         console.log('Message sent to content script');
//                     });
//                     // chrome.tabs.onUpdated.removeListener(onTabUpdated); // Remove the event listener after it's triggered
//                 }
//             });
//         });
//     }
    

//     // postUrl(sendingURL);        
// });

// document.addEventListener('DOMContentLoaded', function () {
//     console.log('DOMContentLoaded event fired.');

//     const fileContentArray = []; // Create a new array to store the file content
//     chrome.runtime.getPackageDirectoryEntry(function (rootDir) {
//         console.log('Got package directory entry.');

//         rootDir.getFile('Text_com/paul_links.txt', {}, function (fileEntry) {
//             console.log('Got file entry.');

//             fileEntry.file(function (file) {
//                 console.log('Got file.');

//                 const reader = new FileReader();

//                 reader.onloadend = function (e) {
//                     console.log('File loaded successfully.');

//                     const content = e.target.result;
//                     const lines = content.split('\n'); // Split the content into an array of lines
//                     fileContentArray.push(...lines); // Add the lines to the fileContentArray

//                     console.log('File content array:', fileContentArray);

//                     // Now you can use the 'fileContentArray' variable containing the lines of the text file
//                     // Perform any additional actions you need with the file content array

//                     console.log(fileContentArray); // Display the array in the console log
//                 };

//                 reader.readAsText(file);
//             });
//         });
//     });
// });

