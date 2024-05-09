const puppeteer = require('puppeteer')
//provides access to puppeteer
const fs = require('fs/promises')
//this import provides the asynchronous version of the file system functions
const ds = require('fs')
//this import provides the synchronous version of the file system functions
const path = require('path')
//imports the path module
const axios = require('axios');

let fileName = "../Text_com/content.txt"
//specifies the output text file

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

const folderDestination = "../../Webscraper/Vertex/Images"
//specifies the folder destination


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
		//the beginning of the async function start, allowing the await function to be called
		ds.access(fileName, ds.constants.F_OK, (e) => {
			//this function checks and logs if the above file exists or not
			if (e) {
				console.error('File does not exist');
			} else {
				ds.unlink(fileName, (e) => {
					if (e) {
						console.error('An error occurred');
					} else {
						console.error('File has been deleted');
					}
				});
			}
		});

		const browser = await puppeteer.launch()
		//the browser is launched
		const page = await browser.newPage()
		await page.goto(url)
	//a new page is created which goes to the specified URL
		const mathsisfun_content = await page.evaluate(() => {
			return Array.from(document.querySelectorAll("p")).map(x => x.textContent)
			//the textcontent from the specific CSS selector (to the webpage) is selected and returned as an array
		})

		module.exports = mathsisfun_content;
        //exports the mathsisfun_content array to be used in other files

		await fs.writeFile(fileName, mathsisfun_content.join("\r\n"))
		//the array is written to a file with each member written to one line
		console.log('Wrote to text file');

		await browser.close()
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