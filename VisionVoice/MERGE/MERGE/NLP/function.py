from navigation import WebNavigator
from urllib.parse import urlparse
import pyttsx3

homepage_urls = {
    "oxnotes.com": "https://www.oxnotes.com/igcse-mathematics.html",
    "mathisfun.com": "https://www.mathsisfun.com/algebra/index.html",
    "tutorial.math.lamar.edu": "https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx",
    "mathplanet.com": "https://www.mathplanet.com/education/algebra-2"  # Add more websites as needed
}


def extract_base_url(url):
    # Parse the URL to extract the domain name
    parsed_url = urlparse(url)
    base_url = parsed_url.netloc
    return base_url



def read_hyperlinks_function(navigator):
    print("link")
    current_url = navigator.get_current_url()  # Get the current URL from the navigator
    if current_url:
        print("Current URL:", current_url)
        read_out_text("Going to section")
    else:
        print("Current URL not available.")
        read_out_text("That section doesn't seem to be available")
    return current_url


def write_to_file(URL):
    with open("chosen_URL.txt", "w") as file:
        file.write(URL)


def read_content_function(navigator):
    print("read")
    current_url = navigator.get_current_url()  # Get the current URL from the navigator
    if current_url:
        print("Current URL:", current_url)
    else:
        print("Current URL not available.")
    return current_url


def go_back_function(navigator, current_url):
    print("Go back")
    # Check if the current URL is a homepage URL
    for homepage_url in homepage_urls.values():
        print(navigator.current_url)
        if navigator.current_url.strip() == homepage_url:
            print("You are already on the homepage.")
            read_out_text("You are already on the homepage.")
            return current_url

    # If not on the homepage, navigate back
    navigator.go_back()
    read_out_text("Going back")
    # Update current_url after navigation
    current_url = navigator.current_url
    return current_url


def explain_images_function():
    print("explain images")


def explain_graph_function():
    print("explain graph")

def read_out_text(text):#function to read out text
    engine = pyttsx3.init() #the speech synthesis started
    engine.say(text) #adds text to the speech queue
    engine.runAndWait() #reads out the text

def translate_to_sinhala_function():
    print("tarn sin")


def translate_to_tamil_function():
    print("tarn tamil")


def goto_section_function(test_command, navigator, current_url):
    print("Go to section")
    start_url = current_url if current_url else print(
        "The specified link is not available ")  # Use current URL if available, otherwise ask the user for input
    navigator.navigate(start_url, test_command)
    return start_url  # Return the updated current URL after navigation
