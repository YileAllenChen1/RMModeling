  
import os
	
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