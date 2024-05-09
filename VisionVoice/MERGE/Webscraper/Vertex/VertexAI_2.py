import os
import csv
from vertexai.preview.generative_models import GenerativeModel, Image
import vertexai.preview.generative_models as generative_models
import vertexai

# Define a function to generate content using the Generative Model
def generate(image_dir, output_csv):
    # Set the environment variable for the API key
    os.environ["API_KEY"] = "AIzaSyARr5FRRNoNCkXTmrrS3L6s0W_pgP6hiJ8"

    # Initialize Vertex AI with project and location
    vertexai.init(project="positive-wonder-414804", location="us-central1")

    # Create a GenerativeModel object with the specified model name
    model = GenerativeModel("gemini-pro-vision")

    # Open CSV file for writing
    with open(output_csv, 'w', newline='') as csvfile:
        # Initialize generated content variable
        generated_content = ""

        writer = csv.writer(csvfile)

        # Write header row to CSV file
        writer.writerow(['Image', 'Generated Content'])

        # Iterate over images in the directory
        for filename in os.listdir(image_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check if the file is an image
                # Load the input image as an Image object
                image_path = os.path.join(image_dir, filename)
                image = Image.load_from_file(image_path)

                # Generate content based on input image and a prompt
                responses = model.generate_content(
                    [image, """explain the above image"""],
                    generation_config={
                        "max_output_tokens": 2048,
                        "temperature": 0.4,
                        "top_p": 1,
                        "top_k": 32
                    },
                    safety_settings={
                        # Specify the safety settings to block harmful content
                        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    },
                    stream=True,
                )         
                       
                i = 0
                # Iterate over the responses and concatenate the generated content
                for response in responses:
                    i = i + 1
                    print("Added explanation for image", i)
                    generated_content += response.text

                # Write image filename and generated content to CSV file
                if not generated_content:
                    generated_content = "There were no images on this webpage"
                    #handles if there was no image

                writer.writerow([filename, generated_content])

    return generated_content


# Directory containing input images
image_dir = "F:/University IIT/Coursework 1 (SDGP)/Implementation/Webscraper/Vertex/Images"

output = "F:/University IIT/Coursework 1 (SDGP)/Implementation/MERGE/Text_com/content.txt"

generated_content = ""

try:
    generated_content = generate(image_dir, output)
except Exception as e:
    if generated_content:
        with open(output, 'w') as file:
            file.write(generated_content)
    else:
        error = "An error occurred when getting the image explanation" 
        with open(output, 'w') as file:
            file.write(error)

print("Generated content saved to", output)