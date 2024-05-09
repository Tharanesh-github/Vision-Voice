// const axios = require('axios');

const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  //requiring of the Gemini API

  const MODEL_NAME = "gemini-pro";
  const API_KEY = "AIzaSyDdjzJ8VmKnfHhcINX0nwLepnPEPUkA2u8";
  //specifying the model name and the unique api key
  
  async function run() { //the async function run can use the await function
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
    //the model name and api key are used
  
    const generationConfig = { //This is configuration of the Gemini API model being used
      temperature: 0.9,
      topK: 1,
      topP: 1,
      maxOutputTokens: 2048,
    };
  
    const safetySettings = [ //These are the safety settings imposed by Gemini API, they have been set to LOW
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      },
    ];

    const fs = require('fs');
    
    let text_file = '../Text_com/content.txt';//defines the text file 

    let fileContent = ""; //defines the variable fileContent to hold a string
    
    
    fs.readFile(text_file, 'utf-8', async (e, text_content) => { //the implementation of the async funstion readFile
      //to prevent any possible errors, this file contains the call to the Gemini API along with the reading of the input file and the writing to the output file

      if (e) {
        console.error('An Error came whilst reading the file');
        //logs if there is an error and rejects the function
      }
      
      fileContent = text_content;//the String variable takes the read content from the input text file

      let paragraph = fileContent; //passes fileContent again to the paragraph variable for the sake of neatness

      console.log("Read from the input text file")
      //just to inform that the file has been read from

      let text1 = "Explain the following text in a simple and concise manner, '" + paragraph + "'. Write it in a short form without any point forms and '*'.";
      //text1 is the prompt that is sent to the API, it is a concatenation of paragraph

      const parts = [ //the array that contains the prompt
        {text: text1},
      ];
    
      let result = await model.generateContent({ 
        //since that this is an async function await can be called
        contents: [{ role: "user", parts }],
        generationConfig,
        safetySettings,
      });
    
      let response = result.response;//the response from the API is gotten

      let textToWrite = response.text();//the response is converted to text and assigned to a variable

      let filePath2 = "../Text_com/summarized_content.txt";
      //the file name of the output text file

      let summarized_content = textToWrite

      module.exports = summarized_content;
      //exports the texttoWrite string to be used in other files

      //posts the content to the API
      // axios.post('http://localhost:3000/content', {
      //   content: summarized_content
      // })
      // .then((res) => {
      //   console.log(`Status: ${res.status}`);
      //   console.log('Body: ', res.data);
      // })
      // .catch((err) => {
      //   console.error(err);
      // });



      fs.writeFile(filePath2, textToWrite, 'utf-8', (e) => {
        if (e) {
          console.error('An Error happened whilst writing');
          return;//the error is logged and rejects the async function promise
        }
        console.log('File has been written to');
        //lets you know that the file has been written to
      });
      
    });
    
  }
  

try{
    run(); //the defined async function is called when this file is run
} catch (error) {
    error_message = "An error occurred while generating content"
    fs.writeFile(fileName, error_message)
}