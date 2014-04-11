import Image
import numpy as np
 
CHAR_WIDTH = 3
CHAR_HEIGHT = 5


img = Image.open('gasp.jpg').convert('LA')

w,h = img.size

#basic ascii ramp, need to reverse it
chars = [' ','.', ',', ':','-','=','+','*','#','%','@']
charsrev = chars[::-1]  
 
asdf = 256.0/ (len(chars)-1)



data = list(img.getdata())
data2 = np.array([d[0] for d in data]).reshape(w, h)


f = open('ascimg.txt', 'w')

for y in xrange(int(np.floor(h/CHAR_HEIGHT))):
    for x in xrange(int(np.floor(w/CHAR_WIDTH))):
        sub_pixels = data2[y:y + CHAR_HEIGHT, x:x + CHAR_WIDTH]
        avg = sub_pixels.mean()/asdf
        f.write(charsrev[int(avg)])
    f.write('\n')
f.close()
        





desired_width = 300
divisor = w / desired_width



w /= divisor
h /= divisor

w, h = int(w), int(h)

#resize to smaller dimensions
img = img.resize([w,h])
#get a list of pixel data

 

 
#create a file
f = open('ascimg.txt', 'w')
 
for y in range(h):
	for x in range(w):
	    	#get the current pixel from the list, scale its value and write to file
		pixel = data[(y)*w+(x)]
		ave = n.floor(pixel[0]/asdf)
		f.write(chars[int(ave)])
	f.write('\n')	
f.close()