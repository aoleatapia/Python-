from PIL import Image as pil_image
import os 

source_path = "./images/"
dest_path = "./new_images/"

if not os.path.isdir(dest_path):
    os.mkdir(dest_path)
    
files = os.listdir(path = source_path) 
counter = 1

crop_box = ()

for img in files:
    print(img) 
    counter +=1
    image = pil_image.open(source_path + img)
    
    #create a cropbox ysing the shortest edge size of picture
    size = image.size
    size = size[0] if size[0] < size[1] else size[1]
    #crop the image
    crop_box = (0,0, size, size)
    
    
    image= image.crop(crop_box)
 
    #rotate the image
    image = image.rotate(270)
    
     #greayscale
    image = image.convert('L')
    #thumbnail
    size = 75,75
    image.thumbnail(size)
    
     #save the image
    save_image = dest_path + f"pic{str(counter).rjust(4,'0')}.png"
    image.save(save_image)
    print(f"Saving {img} as {save_image}")
    #count up
    counter += 1
    
    if counter > 300:
        break
    
    
 
    