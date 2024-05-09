from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import spacy
import pyttsx3

def read_out_text(text):#function to read out text
    engine = pyttsx3.init() #the speech synthesis started
    engine.say(text) #adds text to the speech queue
    engine.runAndWait() #reads out the text

class WebNavigator:


    def __init__(self, commands=None):
        self.driver = webdriver.Chrome()
        self.current_url = None
        self.commands = commands
        self.nlp_navigation = spacy.load("fine_tuned_model")

    def open_hyperlink(self, absolute_url):
        try:
            self.driver.get(absolute_url)
            self.current_url = self.driver.current_url
            return self.current_url
        except WebDriverException as e:
            print("An error occurred while opening the hyperlink")
            read_out_text("An error occurred while opening the hyperlink")
            return None

    def go_back(self):
        try:
            self.driver.back()
            self.current_url = self.driver.current_url
            return self.current_url
        except WebDriverException as e:
            print("An error occurred while navigating back:", e)
            read_out_text("An error occurred while navigating back")
            return None

    def navigate(self, start_url, command):
        #self.current_url = start_url
        #self.driver.get(start_url)
        WebDriverWait(self.driver, 3600).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        response = self.driver.page_source
        soup = BeautifulSoup(response, 'html.parser')
        hyperlinks = soup.find_all('a')

        print(command)

        doc_navigation = nlp_navigation(command)

        hyperlink_entities = [ent.text.lower() for ent in doc_navigation.ents if ent.label_ == "HYPERLINK"]
        hyperlink_found = False

        if hyperlink_entities:
            for hyperlink_entity in hyperlink_entities:
                for hyperlink in hyperlinks:
                    if hyperlink_entity.lower() in hyperlink.text.lower():
                        self.current_url = start_url  # Case-insensitive comparison
                        absolute_url = urljoin(self.current_url, hyperlink.get('href'))
                        print(f"Opening the hyperlink: {absolute_url}")
                        read_out_text("Opening webpage")
                        self.current_url = self.open_hyperlink(absolute_url)
                        if self.current_url:
                            hyperlink_found = True
                            break
            if not hyperlink_found:
                print("No matching hyperlinks found for the given command. Staying on the current page.")
                read_out_text("No matching hyperlinks found for the given command. Staying on the current page.")
        else:
            print("No hyperlink entities found in the command. Staying on the current page.")
            read_out_text("No hyperlink entities found in the command. Staying on the current page.")

            

    def get_current_url(self):
        return str(self.current_url)


nlp_navigation = spacy.load("fine_tuned_model")
