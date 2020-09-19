import os

def main(): 
	os.chdir(r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg")
	#print(os.getcwd()) 
	path = r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg/"

	rename = ""
	for count, filename in enumerate(os.listdir(path)):
		rename = ""
		if "狼牙" in filename:
			index = filename.find('_')
			rename = "WMJVsWolfTooth" + filename[index:]
		if "交龙" in filename:
			index = filename.find('_')
			rename = "JiaoDragonVsCUBOT" + filename[index:]
		if "火线" in filename:
			index = filename.find('_')
			rename = "FireWireVsBorn of Fire" + filename[index:]
		if "电创" in filename: 
			index = filename.find('_')
			rename = "DianChuangVsRPS" + filename[index:]
		if "速加网笃行" in filename:
			index = filename.find('_')
			rename = "SJWDXVsHLL" + filename[index:]
		if "领志科技" in filename:
			index = filename.find('_')
			rename = "LingzhiTechAresVsThunder" + filename[index:]

		src =path+ filename 
		rename =path+ rename

		if rename not in path: 
			os.rename(src, rename) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
	main()