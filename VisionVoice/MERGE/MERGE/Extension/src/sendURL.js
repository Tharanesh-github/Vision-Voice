// import axios from 'axios';

//opening the tab

// function postUrl(url) {
//     axios.post('http://localhost:3000/url', {
//         command: url
//     })
//     .then(response => {
//         console.log(response.data);
//     })
//     .catch(error => {
//         console.error(error);
//     });
// }

// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//     if (request.action === 'openNewTab') {
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
//     let sendingURL = request.url;
//     postUrl(sendingURL);        
// });
