import os 
import pandas as pd

img_directory = './image'

# df of the images, to remove images that are ungradable
df = pd.read_csv('./Form Responses/long_final_data.csv')
images = df['variable']

deleted = []

for img in os.listdir(img_directory):
    delete = True
    for i in range(len(images)):
        if img in images.iloc[i]:
            delete = False
            break
    if delete:
        deleted.append(img)
        img_path = os.path.join(img_directory, img)
        os.remove(img_path)

print(deleted)