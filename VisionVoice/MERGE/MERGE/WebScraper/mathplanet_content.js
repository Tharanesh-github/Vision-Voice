const puppeteer = require('puppeteer')
//acquires the puppeteer module
const fs = require('fs').promises
//acquires the fs module
const path = require('path')
//imports the path module
const ds = require('fs')
const axios = require('axios');

const fileName = "../Text_com/content.txt"
//specifies the text file name
const folderDestination = "../../Webscraper/Vertex/Images"
//specifies the folder destination

// Define the URL
let url_path = "http://localhost:3000/url"

let url = ""

// gets the URL from the API
axios.get(url_path)
  .then(response => {
    url = response.data;
  })
  .catch(error => console.error('Error:', error));
//defines the url to be used


async function emptyFolder(folderLocation) { //an asnyc function (allowing us to use the await function) to empty the images folder of any previous old images
    try {
        let files = await fs.readdir(folderLocation)

		//read the contents of the folder

        for (let file of files) { //iterate over each file in the folder
            let filePath = path.join(folderLocation, file)//get the full path of the file

			await fs.unlink(filePath)//deletes the file

        }

        console.log("Emptied Images folder")
        //logs to let you know that the folder was emptied
    } catch (error) {
        console.error("An error occurred while emptying the folder")
    }
}

async function start() {

    ds.access(fileName, ds.constants.F_OK, (e) => {
        //this function checks and logs if the above file exists or not
        if (e) {
            console.error('File does not exist');
        } else {
            ds.unlink(fileName, (e) => {
                if (e) {
                    console.error('An error occurred');
                } else {
                    console.log('File has been deleted');
                }
            });
        }
    });

    const browser = await puppeteer.launch()
    //the browser is launched
    const page = await browser.newPage()
    console.log(url)
    await page.goto(url)
//a new page is created which goes to the specified URL
    
    const mathplanet_content = await page.evaluate(() => {
        return Array.from(document.querySelectorAll(".body p")).map(x => x.textContent)
        //the textcontent from the specific CSS selector (to the webpage) is selected and returned as an array
    })

    module.exports = mathplanet_content;
    //exports the mathplanet_content array to be used in other files
    await fs.writeFile(fileName, mathplanet_content.join("\r\n"))
    console.log('Wrote text content to file')
    //the array is written to a file with each member written to one line

    // Get the URLs of the images in the specified CSS selector
    const photoUrls = await page.$$eval(".body img", imgs => {
        return imgs.map(x => x.src)
    })

    // Download the specific images from the css selectors
    for (const [index, photoUrl] of photoUrls.entries()) {//iterates with the index and url of the photoUrls array
        const imagePage = await page.goto(photoUrl)//goes to the image page of the URL
        const imageBuffer = await imagePage.buffer() //awaits the image buffer
        const imageName = `${index + 1}_${photoUrl.split("/").pop()}` // Add index to be neat
        const imagePath = `${folderDestination}/${imageName}`//create the file path of the image
        await fs.writeFile(imagePath, imageBuffer)//writes the file to the path
        console.log(`Downloaded:  ${index + 1} of ${photoUrls.length}`)//logs to show the progress
    }

    console.log('Downloaded all the images to the Images folder, if there were any') //Logs to show the process is complete
    await browser.close() // Close the browser 
    //the console logs that the file has been written to and the headless browser is closed
}

try{
    emptyFolder(folderDestination)
    //the folder is emptied first

    start()
    //the async function start() is called when this file is run
} catch (error) {
    error_message = "An error occurred while generating content"
    fs.writeFile(fileName, error_message)
}


