import os
from PIL import Image

def delete_corrupt_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg', '.png')):
                try:
                    with Image.open(os.path.join(root, file)) as img:
                except (IOError, SyntaxError) as e:
                    os.remove(os.path.join(root, file))
                    print(f'Deleted corrupt image: {file}')

delete_corrupt_images('/Users/irahhal/Desktop/projects/nudity-dataset/hugging-scenes')