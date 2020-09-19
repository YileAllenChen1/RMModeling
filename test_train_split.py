import shutil
import os
import random


source = r"C:/Users/11458/Desktop/RMModeling/images/renamed_images"
destination_train = r"C:/Users/11458/Desktop/RMModeling/images/train"
destination_test = r"C:/Users/11458/Desktop/RMModeling/images/test"

files = os.listdir(source)	#get all the files in directory, stored in list

test_train_ratio = 0.2	#ratio of test samples from total
test_images = random.sample(files, int(len(files)*test_train_ratio))
train_images = list(set(files) - set(test_images))

for count, test_image in enumerate(test_images):
	if test_images not in os.listdir(destination_test):
		new_test_path = shutil.copy(f"{source}/{test_image}", destination_test)
	print(count)

for count, train_image in enumerate(train_images):
	if train_images not in os.listdir(destination_train):
		new_train_path = shutil.copy(f"{source}/{train_image}", destination_train)
	print(count)