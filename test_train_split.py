import shutil
import os
import random


source = r"C:/Users/11458/Desktop/RMModeling/train"
destination = r"C:/Users/11458/Desktop/RMModeling/test"

files = os.listdir(source)
#print(int(len(files)*0.2))

test_images = random.sample(files, int(len(files)*0.2))
print(test_images)
for image in test_images:
	new_path = shutil.move(f"{source}/{image}", destination)
	print(new_path)