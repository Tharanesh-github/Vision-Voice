(()=>{function e(){chrome.windows.create({url:"index.html",type:"popup",width:400,height:800},(function(e){chrome.tabs.onUpdated.addListener((function n(t,o,r){t===e.tabs[0].id&&"complete"===o.status&&chrome.tabs.onUpdated.removeListener(n)}))}))}self.addEventListener("install",(function(e){console.log("Service worker installed")})),self.addEventListener("activate",(function(e){console.log("Service worker activated")})),self.addEventListener("fetch",(function(e){console.log("Service worker fetching")})),chrome.runtime.onInstalled.addListener((function(){e()})),chrome.runtime.onStartup.addListener((function(){chrome.windows.getAll({populate:!0},(function(n){for(var t=!1,o=0;o<n.length;o++)if(n[o].tabs&&n[o].tabs[0].url.includes("index.html")){t=!0;break}t||e()}))})),chrome.runtime.onMessage.addListener((function(e,n,t){if("openNewTab"===e.action){console.log("Received openNewTab request"),chrome.tabs.create({url:e.url},(function(n){console.log("new tab is created",n.id),chrome.tabs.onUpdated.addListener((function(t,o,r){"complete"===o.status&&t===n.id&&(console.log("tab is updated"),chrome.tabs.sendMessage(n.id,{action:"tabUpdated",url:e.url},(function(e){console.log("Message sent to content script")})))}))}));var o=e.url.toString();return console.log("Sending URL:",o),fetch("http://localhost:3000/url",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url:o})}).then((function(e){return e.json()})).then((function(e){console.log("Response from server:",e)})).catch((function(e){console.error("Error:",e)})),!0}})),chrome.runtime.onMessage.addListener((function(e,n,t){if("userInput"===e.action){var o=e.userInput.toString();return console.log("Received userInput:",o),fetch("http://localhost:3000/user_command",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({userInput:o})}).then((function(e){return e.json()})).then((function(e){console.log("Response from server:",e)})).catch((function(e){console.error("Error:",e)})),!0}}))})();