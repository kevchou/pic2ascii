pic2ascii
=========

Really simple code that converts a picture to ascii.

Opens a picture, converts to greyscale, and resizes the picture. It then scans each pixel and 
replaces it with a corresponding ascii character depending on the darkness of that pixel.

In the command line, run "python pic2ascii.py (file) (desired height)"

Where file is the picture file, and desired height is the number of pixels you'd like the picture to be resized to.

Eg.

``` python
python pic2ascii.py gasp.png 100
```

Produces "ascimg.txt"
