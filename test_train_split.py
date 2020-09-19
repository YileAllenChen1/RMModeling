import shutil
import os
import random


xml_source = r"C:/Users/11458/Desktop/RMModeling/images/renamed_images_xml"
jpg_source = r"C:/Users/11458/Desktop/RMModeling/images/renamed_images_jpg"
destination_train = r"C:/Users/11458/Desktop/RMModeling/images/train"
destination_test = r"C:/Users/11458/Desktop/RMModeling/images/test"

xml_files = os.listdir(xml_source)	#get all the files in directory, stored in list
jpg_files = os.listdir(jpg_source)

test_train_ratio = 0.2	#ratio of test samples from total
test_images_xml = random.sample(xml_files, int(len(xml_files)*test_train_ratio))
train_images_xml = list(set(xml_files) - set(test_images_xml))

test_images_jpg = []
train_images_jpg = []

for count, jpg_image in enumerate(jpg_files):
	# print(jpg_image[:-4])
	for xml_image in test_images_xml:
		if jpg_image[:-4] == xml_image[:-4]:
			test_images_jpg.append(jpg_image)
	for xml_image in train_images_xml:
		if jpg_image[:-4] == xml_image[:-4]:
			train_images_jpg.append(jpg_image)
	print(count)



for count, test_image_xml in enumerate(test_images_xml):
	new_test_path = shutil.copy(f"{xml_source}/{test_image_xml}", destination_test)
	print(count)

for count, train_image_xml in enumerate(train_images_xml):
	new_train_path = shutil.copy(f"{xml_source}/{train_image_xml}", destination_train)
	print(count)

for count, test_image_jpg in enumerate(test_images_jpg):
	new_test_path = shutil.copy(f"{jpg_source}/{test_image_jpg}", destination_test)
	print(count)

for count, train_image_jpg in enumerate(train_images_jpg):
	new_train_path = shutil.copy(f"{jpg_source}/{train_image_jpg}", destination_train)
	print(count)