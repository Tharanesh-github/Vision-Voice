//content.js

// import axios from 'axios';
// import axios from 'axios';

// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//     if (request.action === 'tabUpdated') {
//         const updatedUrl = request.url;    //url of the cirrent website
//         console.log('Received tabUpdated message:', updatedUrl);

//         // Identify the website based on the updatedUrl
//         if (updatedUrl.includes('mathplanet.com')) {
//             console.log('mathplanet website was opened');
//             chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/mathplanet_links.txt' });
//         } else if (updatedUrl.includes('tutorial.math.lamar.edu')) {
//             console.log('Pauls online notes website was opened');
//             chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/paul_links.txt' });
//             chrome.runtime.sendMessage({ action: 'goToSectionPaul' });
//             // const script = document.createElement('script');
//             // script.src = 'webscraper/paul_links.js';
//             // document.head.appendChild(script);
//         } else if (updatedUrl.includes('oxnotes.com')) {
//             console.log('Oxnotes website was opened');
//             chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/oxnotes_links.txt' });
//         } else if (updatedUrl.includes('mathsisfun.com')) {
//             console.log('mathsisfun website was opened');
//             chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/mathsisfun_sections.txt' })
//                 .then(function(response) {
//                     console.log('response:', response);
//                 })
//                 .catch(function(error) {
//                     console.error('error occured', error);
//                 });
//             chrome.runtime.sendMessage({ action: 'goToSection' });
//         } else {
//             console.log('Unknown website was opened');
//         }

//         // return true;
//     }
// });

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'url_from_node') {
        const updatedUrl = message.url;  //url of the current website
        console.log('URL from Node:', updatedUrl);
        // Do something with the url

        if (updatedUrl.includes('mathplanet.com')) {
            console.log('mathplanet website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/mathplanet_links.txt' });
        } else if (updatedUrl.includes('tutorial.math.lamar.edu')) {
            console.log('Pauls online notes website was opened');
            chrome.runtime.sendMessage({ action: 'callReadtextFile', filename: 'Text_com/paul_links.txt' });
            chrome.runtime.sendMessage({ action: 'goToSectionPaul' });
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
    }
});
