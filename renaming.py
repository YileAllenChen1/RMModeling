  
import os
# import re

# def sorted_aphanumeric(data):
#     convert = lambda text: int(text) if text.isdigit() else text.lower()
#     alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
#     return sorted(data, key=alphanum_key)
	
# path = r"C:\Users\11458\Desktop\RMModeling"


# i = 0
# j = 0
# for filename in sorted_aphanumeric(os.listdir(path)):
# 	os.rename(os.path.join(path,filename), os.path.join(path,"Image_" + str(i) + ".xml"))
# 	i+=1
	
def main(): 
	#os.chdir(r"C:\Users\11458\Desktop\RMModeling\image_annotation") 
	os.chdir(r"C:/Users/11458/Desktop/RMModeling/image_annotation")
	print(os.getcwd()) 
	path = r"C:/Users/11458/Desktop/RMModeling/image_annotation/"
	for count, filename in enumerate(os.listdir(path)): 
		dst ="RM_Image_" + str(count) + ".xml"
		src =path+ filename 
		dst =path+ dst 
		  
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
	main()