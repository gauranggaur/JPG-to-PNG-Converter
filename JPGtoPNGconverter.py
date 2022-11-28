import sys
import os
from PIL import Image

# grab directory arguments info
source_folder = sys.argv[1]
destination_folder = sys.argv[2]

# check if destination_folder exists, if not, create one
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    
# loop through source folder, convert to png, and save to new folder
for imgFile in os.listdir(source_folder):
    img = Image.open(f"{source_folder}/{imgFile}")
    clean_name = os.path.splitext(imgFile)[0]
    img.save(f"{destination_folder}/{clean_name}.png", "png")

