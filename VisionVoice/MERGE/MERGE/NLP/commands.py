import spacy
from spacy.training.example import Example
from function import *
from navigation import WebNavigator
from selenium.common.exceptions import WebDriverException
import requests
import json
import subprocess


def train_text_categorization_model(train_data, use_case_labels, n_iter=20, dropout=0.5, batch_size=8):
    # Load the large English language model
    nlp = spacy.blank("en")

    # Add text categorization pipeline
    textcat = nlp.add_pipe("textcat")
    for label in use_case_labels:
        textcat.add_label(label)

    # Convert training data to Examples
    examples = []
    for text, annotations in train_data:
        examples.append(Example.from_dict(nlp.make_doc(text), annotations))

    # Train only the text categorizer
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "textcat"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for i in range(n_iter):
            losses = {}
            for batch in spacy.util.minibatch(examples, size=batch_size):
                nlp.update(batch, drop=dropout, losses=losses, sgd=optimizer)

    return nlp


def quit_browser(navigator):
    navigator.driver.quit()


def predict_intent(model, command, use_case_labels):
    doc = model(command)
    predicted_labels = [label for label in use_case_labels if label in doc.cats]

    if not predicted_labels:
        print("Command not recognized.")
        return None

    matched_intent = max(predicted_labels, key=lambda label: doc.cats[label])
    return matched_intent


# Define your training data
train_data = [
    ("go to matrices", {"cats": {"goto_section": 1}}),
    ("matrices", {"cats": {"goto_section": 1}}),
    ("Going to the Ratios section", {"cats": {"goto_section": 1}}),
    ("Going to the Ratios section", {"cats": {"goto_section": 1}}),
    ("open introduction to algebra", {"cats": {"goto_section": 1}}),
    ("go to factorising guadratics ", {"cats": {"goto_section": 1}}),
    ("Introduction to algebra", {"cats": {"goto_section": 1}}),
    ("Move to introduction to algebra", {"cats": {"goto_section": 1}}),
    ("explore introduction to geometry", {"cats": {"goto_section": 1}}),
    ("balance when adding and subtracting", {"cats": {"goto_section": 1}}),
    ("go to balance when adding and subtracting", {"cats": {"goto_section": 1}}),
    ("open balance when adding and subtracting", {"cats": {"goto_section": 1}}),
    ("open trigonometry", {"cats": {"goto_section": 1}}),
    ("PEMDAS", {"cats": {"goto_section": 1}}),
    ("explore PEMDAS", {"cats": {"goto_section": 1}}),
    ("i want to access PEMDAS", {"cats": {"goto_section": 1}}),
    ("open Substitution", {"cats": {"goto_section": 1}}),
    ("substitution", {"cats": {"goto_section": 1}}),
    ("explore Substitution", {"cats": {"goto_section": 1}}),
    ("i want to access Substitution", {"cats": {"goto_section": 1}}),
    ("open Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("explore Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("click Equations and Formulas", {"cats": {"goto_section": 1}}),
    ("inequalities", {"cats": {"goto_section": 1}}),
    ("pythagoras' Theorem", {"cats": {"goto_section": 1}}),
    ("what is an Exponent?", {"cats": {"goto_section": 1}}),
    ("what Is A Logarithm", {"cats": {"goto_section": 1}}),
    ("what is a Polynomial?", {"cats": {"goto_section": 1}}),
    ("rationalizing The Denominator", {"cats": {"goto_section": 1}}),
    ("explore the Straight Line Graph", {"cats": {"goto_section": 1}}),
    ("solving systems of equations in two variables", {"cats": {"goto_section": 1}}),
    ("solving systems of equations in three variables", {"cats": {"goto_section": 1}}),
    ("matrix operations", {"cats": {"goto_section": 1}}),
    ("simplify expressions", {"cats": {"goto_section": 1}}),
    ("solving radical equations", {"cats": {"goto_section": 1}}),
    ("complex numbers", {"cats": {"goto_section": 1}}),
    ("how to graph quadratic functions", {"cats": {"goto_section": 1}}),
    ("The Quadratic formula", {"cats": {"goto_section": 1}}),
    ("Basic knowledge of polynomial functions", {"cats": {"goto_section": 1}}),
    ("Logarithm property", {"cats": {"goto_section": 1}}),
    ("Counting principle", {"cats": {"goto_section": 1}}),
    ("trigonometric functions", {"cats": {"goto_section": 1}}),
    ("law of sines", {"cats": {"goto_section": 1}}),
    ("law of cosines", {"cats": {"goto_section": 1}}),
    ("trigonometric identities", {"cats": {"goto_section": 1}}),
    ("rational expressions", {"cats": {"goto_section": 1}}),
    ("going to the ratios section", {"cats": {"goto_section": 1}}),
    ("open introduction to algebra", {"cats": {"goto_section": 1}}),
    ("open trigonometry", {"cats": {"goto_section": 1}}),

    ("readout the Hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("list the links", {"cats": {"read_hyperlinks": 1}}),
    ("provide a list of hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("read out the URLs", {"cats": {"read_hyperlinks": 1}}),
    ("enumerate the hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("announce the links", {"cats": {"read_hyperlinks": 1}}),
    ("retrieve the hyperlink addresses", {"cats": {"read_hyperlinks": 1}}),
    ("read aloud the hyperlinks", {"cats": {"read_hyperlinks": 1}}),
    ("present the list of links", {"cats": {"read_hyperlinks": 1}}),
    ("display the URLs", {"cats": {"read_hyperlinks": 1}}),
    ("list all the clickable links", {"cats": {"read_hyperlinks": 1}}),
    ("readout the link", {"cats": {"read_hyperlinks": 1}}),

    ("go to the home page", {"cats": {"goto_homepage": 1}}),
    ("navigate to the main page", {"cats": {"goto_homepage": 1}}),
    ("return to the homepage", {"cats": {"goto_homepage": 1}}),
    ("visit the front page", {"cats": {"goto_homepage": 1}}),
    ("access the initial page", {"cats": {"goto_homepage": 1}}),
    ("move to the starting page", {"cats": {"goto_homepage": 1}}),
    ("return to the landing page", {"cats": {"goto_homepage": 1}}),
    ("browse to the home screen", {"cats": {"goto_homepage": 1}}),
    ("go back to the main menu", {"cats": {"goto_homepage": 1}}),
    ("access the primary page", {"cats": {"goto_homepage": 1}}),
    ("navigate to the front end", {"cats": {"goto_homepage": 1}}),

    ("read the content", {"cats": {"read_content": 1}}),
    ("read out loud this page", {"cats": {"read_content": 1}}),
    ("retrieve this paragraph", {"cats": {"read_content": 1}}),
    ("provide the information in the page", {"cats": {"read_content": 1}}),
    ("narrate the full content", {"cats": {"read_content": 1}}),
    ("speak the content", {"cats": {"read_content": 1}}),
    ("vocalize the content", {"cats": {"read_content": 1}}),
    ("recite the paragraph", {"cats": {"read_content": 1}}),
    ("verbally present the content", {"cats": {"read_content": 1}}),
    ("announce the content", {"cats": {"read_content": 1}}),

    ("go back", {"cats": {"go_back": 1}}),
    ("return to the previous page", {"cats": {"go_back": 1}}),
    ("navigate backward", {"cats": {"go_back": 1}}),
    ("backtrack", {"cats": {"go_back": 1}}),
    ("revert to the previous screen", {"cats": {"go_back": 1}}),
    ("return to the prior page", {"cats": {"go_back": 1}}),
    ("move backward in navigation", {"cats": {"go_back": 1}}),
    ("step back", {"cats": {"go_back": 1}}),
    ("go in reverse", {"cats": {"go_back": 1}}),
    ("retreat to the last page", {"cats": {"go_back": 1}}),
    ("revisit the previous screen", {"cats": {"go_back": 1}}),

    ("provide details about the images", {"cats": {"explain_images": 1}}),
    ("describe the images", {"cats": {"explain_images": 1}}),
    ("give information about the pictures", {"cats": {"explain_images": 1}}),
    ("elaborate on the visuals", {"cats": {"explain_images": 1}}),
    ("offer an explanation of the images", {"cats": {"explain_images": 1}}),
    ("discuss the content of the pictures", {"cats": {"explain_images": 1}}),
    ("clarify what the images depict", {"cats": {"explain_images": 1}}),
    ("offer insights into the visuals", {"cats": {"explain_images": 1}}),
    ("examine the imagery", {"cats": {"explain_images": 1}}),
    ("explain about the images", {"cats": {"explain_images": 1}}),

    ("describe the graph", {"cats": {"explain_graph": 1}}),
    ("explain the data visualization", {"cats": {"explain_graph": 1}}),
    ("provide details about the chart", {"cats": {"explain_graph": 1}}),
    ("analyze the graphical representation", {"cats": {"explain_graph": 1}}),
    ("discuss the plotted data", {"cats": {"explain_graph": 1}}),
    ("interpret the graph", {"cats": {"explain_graph": 1}}),
    ("elaborate on the graph", {"cats": {"explain_graph": 1}}),
    ("give insights into the visual representation", {"cats": {"explain_graph": 1}}),
    ("clarify what the graph depicts", {"cats": {"explain_graph": 1}}),
    ("break down the chart", {"cats": {"explain_graph": 1}}),
    ("explain the graphical data", {"cats": {"explain_graph": 1}}),

    ("please translate to Sinhala", {"cats": {"translate_to_sinhala": 1}}),
    ("translate this into Sinhala please.", {"cats": {"translate_to_sinhala": 1}}),
    ("can you convert this to Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("i need this text in Sinhala please.", {"cats": {"translate_to_sinhala": 1}}),
    ("could you provide a translation in Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("please translate this into Sinhala.", {"cats": {"translate_to_sinhala": 1}}),
    ("i'm looking for a translation into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),
    ("is it possible to get this text translated into Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("kindly translate this into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),
    ("can you render this in Sinhala?", {"cats": {"translate_to_sinhala": 1}}),
    ("i'd like this text converted into Sinhala, please.", {"cats": {"translate_to_sinhala": 1}}),

    ("translate this into Tamil please.", {"cats": {"translate_to_tamil": 1}}),
    ("can you convert this to Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("i need this text in Tamil please.", {"cats": {"translate_to_tamil": 1}}),
    ("could you provide a translation in Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("please translate this into Tamil.", {"cats": {"translate_to_tamil": 1}}),
    ("i'm looking for a translation into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("is it possible to get this text translated into Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("kindly translate this into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("can you render this in Tamil?", {"cats": {"translate_to_tamil": 1}}),
    ("i'd like this text converted into Tamil, please.", {"cats": {"translate_to_tamil": 1}}),
    ("please translate to Tamil", {"cats": {"translate_to_tamil": 1}}),

    ("Shut down the browser.", {"cats": {"close_browser": 1}}),
    ("Exit the browser.", {"cats": {"close_browser": 1}}),
    ("Close the browser window.", {"cats": {"close_browser": 1}}),
    ("Terminate the browser.", {"cats": {"close_browser": 1}}),
    ("End the browser session.", {"cats": {"close_browser": 1}}),  # no need this command
    ("Quit the browser.", {"cats": {"close_browser": 1}}),
    ("Stop the browser.", {"cats": {"close_browser": 1}}),
    ("Close the web browser.", {"cats": {"close_browser": 1}}),
    ("Turn off the browser.", {"cats": {"close_browser": 1}}),
    ("shut the browser down.", {"cats": {"close_browser": 1}}),
    ("close the browser", {"cats": {"close_browser": 1}})
]

# Define your use case labels
use_case_labels = ["goto_section", "read_hyperlinks", "read_content", "goto_homepage", "go_back",
                   "explain_images", "explain_graph", "translate_to_sinhala", "translate_to_tamil",
                   "close_browser"]

# Train the model
model = train_text_categorization_model(train_data, use_case_labels)

path = "http://localhost:3000/url"

response = requests.get(path)
print(response.json())
url = response.json()

if "oxnotes" in url:
    url = "https://www.oxnotes.com/igcse-mathematics.html"
elif "mathsisfun" in url:
    url = "https://www.mathsisfun.com/algebra/index.html"
elif "mathplanet" in url:
    url = "https://www.mathplanet.com/education/algebra-2"
elif "tutorial" in url:
    url = "https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx"


#url = input("Enter the initial URL: ")
navigator = None  # Initialize navigator variable


def predict_intent_loop(model, use_case_labels, intent_functions):
    global navigator, url  # Access the navigator and url variables defined outside the function

    if navigator is None:  # If navigator object is not created yet, create it
        navigator = WebNavigator()
        #navigator.url = url
        '''if url:
            navigator.driver.get(url)  # Open the initial URL in the browser'''
        try:
            navigator.driver.get(url)  # Open the initial URL in the browser
        except WebDriverException as e:
            print("Error: Unable to open the initial URL. Please check your internet connection or the URL provided.")
            return

    while True:
        test_command = input("Enter your command: ").lower()




        predicted_intent = predict_intent(model, test_command, use_case_labels)
        if test_command.lower() == "close browser":
            print("Closing the browser...")
            if navigator is not None:
                quit_browser(navigator)  # Call quit_browser function with the navigator object
            break

        if predicted_intent == "goto_section":  # Check if the predicted intent is 'goto_section'
            url = goto_section_function(test_command, navigator,url)  # Update url after navigation
        elif predicted_intent == "go_back":  # Check if the predicted intent is 'goto_homepage'
            go_back_function(navigator,url)
        elif predicted_intent == "read_hyperlinks":

            url = read_hyperlinks_function(navigator)
            path = "http://localhost:3000/url"
            data = {"url": url}
            response = requests.post(path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(response.json)

            mathplanet_subsections = ["node", "../WebScraper/mathplanet_subsections.js"]

            try:
                subprocess.run(mathplanet_subsections, check=True)
                print("Node.js file executed successfully")
            except subprocess.CalledProcessError as e:
                print("Error occurred while executing Node.js file:", e)
            
        elif predicted_intent == "read_content":
            url = read_content_function(navigator)

            path = "http://localhost:3000/url"
            data = {"url": url}
            response = requests.post(path, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(response.json)

            if "oxnotes" in url:
                content = ["node", "../WebScraper/oxnotes_content.js"]
                print("oxnotes")
                try:
                    subprocess.run(content, check=True)
                    print("Node.js file executed successfully")
                except subprocess.CalledProcessError as e:
                    print("Error occurred while executing Node.js file:", e)
            elif "mathsisfun" in url:
                content = ["node", "../WebScraper/mathsisfun_content.js"]
                print("mathsisfun")
                try:
                    subprocess.run(content, check=True)
                    print("Node.js file executed successfully")
                except subprocess.CalledProcessError as e:
                    print("Error occurred while executing Node.js file:", e)
            elif "mathplanet" in url:
                content = ["node", "../WebScraper/mathplanet_content.js"]
                print("mathplanet")
                try:
                    subprocess.run(content, check=True)
                    print("Node.js file executed successfully")
                except subprocess.CalledProcessError as e:
                    print("Error occurred while executing Node.js file:", e)
            elif "tutorial" in url:
                content = ["node", "../WebScraper/paul_content.js"]
                print("paul content")
                try:
                    subprocess.run(content, check=True)
                    print("Node.js file executed successfully")
                except subprocess.CalledProcessError as e:
                    print("Error occurred while executing Node.js file:", e)

            summarizer = ["node", "../Summarizer/code.js"]

            try:
                subprocess.run(summarizer, check=True)
                print("Node.js file executed successfully")
            except subprocess.CalledProcessError as e:
                print("Error occurred while executing Node.js file:", e)
        
        elif predicted_intent == "explain_images":
            explain_images_function()


        elif predicted_intent in intent_functions:
            intent_functions[predicted_intent]()  # Call the corresponding function
        else:
            print("Command not recognized.")


intent_functions = {
    "goto_section": goto_section_function,
    "read_hyperlinks": read_hyperlinks_function,
    "read_content": read_content_function,
    "go_back": go_back_function,
    "explain_images": explain_images_function,
    "explain_graph": explain_graph_function,
    "translate_to_sinhala": translate_to_sinhala_function,
    "translate_to_tamil": translate_to_tamil_function,
}

# Test the trained model
predict_intent_loop(model, use_case_labels, intent_functions)
