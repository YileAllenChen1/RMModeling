import os

def main(): 
	os.chdir(r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg")
	#print(os.getcwd()) 
	path = r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg/"

	rename = ""
	for count, filename in enumerate(os.listdir(path)):
		rename = ""

		#filename=filename[5:]	#because the original file name contains '_' before the names, so we need to get rid of it to detect the '_' after the actual name

		if "华南虎" in filename:
			index = filename.find('_')
			rename = "EvolutionVsHuanan_tiger" + filename[index:]
		if "逸仙狮" in filename:
			index = filename.find('_')
			rename = "Hello WorldVsYixianLion" + filename[index:]
		if "新日成_火锅" in filename:
			filename=filename[5:]
			index = filename.find('_')
			rename = "yxsVsXRC_HG" + filename[index:]
		if "中维动力" in filename: 
			index = filename.find('_')
			rename = "zhongweiVsRobotPilots" + filename[index:]
		if "RoboPilots" in filename:
			index = filename.find('_')
			rename = "GjhyVsRobotPilots" + filename[index:]
		if "高巨毅恒" in filename:
			index = filename.find('_')
			rename = "GjhyVsHuanan_tiger" + filename[index:]

		src =path+ filename 
		rename =path+ rename

		if rename not in path: 
			os.rename(src, rename) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
	main()