import sys
import Image
 
def main(pic_file, desired_height = 100):

    img = Image.open(pic_file).convert('LA')

    w,h = img.size


    #desired_width = 100
    #divisor = w / desired_width

    # Resizes image so that image will be 100 pixels tall
    desired_height = int(desired_height)
    divisor = h / desired_height

    w /= divisor
    h /= divisor

    w, h = int(w), int(h)

    img = img.resize([w,h])


    # Converts picture into a list
    data = [d[0] for d in list(img.getdata())]
 
    # List of characters to use
    chars = list("@%#*+=-:,. " )
 
    div = 256.0/ (len(chars)-1)
 
    # Create file
    f = open('ascimg.txt', 'w')
 
    for y in range(h):
        for x in range(w):
		  pixel = data[(y)*w+(x)]
		  value = int((pixel/div))
		  f.write(chars[value])
        f.write('\n')	
    f.close()
    
if __name__ == "__main__":
    
    picture_file = sys.argv[1]
    desired_height = sys.argv[2]
    main(picture_file, desired_height)