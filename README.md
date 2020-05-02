# Blur

A python script that blurs images using a gaussian blur

to encode a message using terminal:

        $ cd Blur
        $ python blur.py path-to-image 

This will add the image blurred.png, which contains the message to the images folder 

# Example

For example to hide the message "Steganography is cool" in pre1.jpg:

        $ cd Blur
        $ python blur.py images/pre1.jpg 

Here are a series of images that have been blurred:

![pre1.jpg](/images/pre1.jpg)
![pre1.jpg](/images/pre1blurred.jpg)
![pre1.jpg](/images/pre1blurredblurred.jpg)
![pre1.jpg](/images/pre1blurredblurredblurred.jpg)
![pre1.jpg](/images/pre1blurredblurredblurredblurred.jpg)
![pre1.jpg](/images/pre1blurredblurredblurredblurredblurred.jpg)
        
# Packages

- Pillow (PIL)
- numpy
- sys

