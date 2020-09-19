import shutil
import os
import random


source = r"C:/Users/11458/Desktop/RMModeling/renamed_images"
destination_train = r"C:/Users/11458/Desktop/RMModeling/train"
destination_test = r"C:/Users/11458/Desktop/RMModeling/test"

files = os.listdir(source)	#get all the files in directory, stored in list

test_train_ratio = 0.2	#ratio of test samples from total
test_images = random.sample(files, int(len(files)*test_train_ratio))
train_images = list(set(files) - set(test_images))

for test_image in test_images:
	new_test_path = shutil.move(f"{source}/{test_image}", destination_test)


for train_image in train_images:
	new_train_path = shutil.move(f"{source}/{train_image}", destination_train)
