import os
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("output.csv")

# Define the filename to read
filename_to_read = "1_image001.png"   # this is where the image will be called when user asks to explain image

# Define the directory containing the files
image_dir = "F:/University IIT/Coursework 1 (SDGP)/Implementation/Webscraper/Vertex/Images"

# Construct the full path to the image file
full_filename = os.path.join(image_dir, filename_to_read)

# Check if the file exists in the directory
if os.path.exists(full_filename):
    # Check for leading or trailing spaces in the filename
    filename_to_read = filename_to_read.strip()
    
    # Find the row corresponding to the specified filename
    row = df[df['Image'].str.strip() == filename_to_read]

    # Check if the filename exists in the DataFrame
    if not row.empty:
        # Extract the content based on the filename
        content = row['Generated Content'].iloc[0]
        print("Content of", filename_to_read, ":", content)
        output_text_file = "input1.txt"
        with open(output_text_file, 'w') as f:
            f.write(content)
    else:
        print("Filename", filename_to_read, "not found in the CSV file.")
else:
    print("File", filename_to_read, "not found in the directory", image_dir)