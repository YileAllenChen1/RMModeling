import os

def main(): 
	os.chdir(r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg")
	#print(os.getcwd()) 
	path = r"C:/Users/11458/Desktop/RMModeling/images/raw_images_jpg/"

	rename = ""
	for count, filename in enumerate(os.listdir(path)):
		rename = ""

		#filename=filename[5:]	#because the original file name contains '_' before the names, so we need to get rid of it to detect the '_' after the actual name

		if "追梦" in filename:
			index = filename.find('_')
			rename = "DreamVsDreamTeam" + filename[index:]
		# if "交龙" in filename:
		# 	index = filename.find('_')
		# 	rename = "VW_CH3RoboGrinderVsJiaoDrangon" + filename[index:]
		# if "火线" in filename:
		# 	index = filename.find('_')
		# 	rename = "VW_CH3FireWireVsHorizon" + filename[index:]
		# if "中维动力" in filename: 
		# 	index = filename.find('_')
		# 	rename = "VW_CH3ZwdlVsAlliance" + filename[index:]
		# if "风暴" in filename:
		# 	index = filename.find('_')
		# 	rename = "VW_CH3StormVsHuanan_tiger" + filename[index:]
		# if "领志科技" in filename:
		# 	index = filename.find('_')
		# 	rename = "LingzhiTechAresVsThunder" + filename[index:]

		src =path+ filename 
		rename =path+ rename

		if rename not in path: 
			os.rename(src, rename) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
	main()