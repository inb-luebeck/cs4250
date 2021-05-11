"""
In Colab, you cannot simply embed markdown images that are located in the same 
folder or the repository. They need to be in Google Drive.

First, you need to upload the respective images to your google drive. In Drive, 
get the shareable link of the image. And write them into the dictionary below.
Make sure that link sharing is enabled.

Second, run the script to create embedding links. The links are stored in 
"markdown_links.json" Add these link to the respective notebooks.

For more information, see:
https://medium.com/analytics-vidhya/embedding-your-image-in-google-colab-markdown-3998d5ac2684

"""

import re
import json

DRIVE_LINKS = {
    'thin_lens':"https://drive.google.com/file/d/1-Wu6CkCwgJkMWUdb20UkFsBjXBvLCJ3V/view?usp=sharing",
    'cam_model':"https://drive.google.com/file/d/1TZT2lNjms_CrNBQGC3G3pI3XPZ3iMR3j/view?usp=sharing"
}

RGX = r'https:\/\/drive.google.com\/file\/d\/(.*)\/view\?usp=sharing'

def run():
    output = dict()
    for key, val in DRIVE_LINKS.items():
        match = re.match(RGX, val)
        assert bool(match), key
        im_id = match.group(1)

        new_link = "https://drive.google.com/uc?id=" + im_id
        output[key] = new_link

    with open("markdown_links.json", "w") as file:
        json.dump(output, file)

if __name__ == "__main__":
    run()