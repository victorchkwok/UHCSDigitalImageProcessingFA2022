# Victor Kwok 1890910
import numpy as np
import cv2
import math

class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        filter = np.ones(shape)
        for x in range(0, shape[0]):
            for y in range(0, shape[1]):
                if(275<x<295 and 205<y<225):
                    filter[x,y] = 0
                if(220<x<240 and 290<y<310):
                    filter[x,y] = 0
                if(255<x<275 and 275<y<295):
                    filter[x,y] = 0
                if(235<x<255 and 225<y<245):
                    filter[x,y] = 0
        return filter

    def post_process_image(self, image):
        newImage = image.copy()
 
        max = np.max(newImage)
        Min = np.min(newImage)
 
        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                newImage[x, y] = int(((255-1)/(max - Min)) * (newImage[x, y] - Min) + 0.5)
 
        return newImage


    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """
        
        tempImage = self.image.copy()
 
        FFT = np.fft.ifftshift(np.fft.fft2(tempImage))
 
        filtered = FFT.copy()
       
        filter = self.get_mask(tempImage.shape)
        #filtered = FFT* filter
        for x in range(0, self.image.shape[0]):
            for y in range(0, self.image.shape[1]):
                filtered[x,y] = FFT[x,y]* filter[x,y]

 
        temp = np.abs(FFT)
        temp = np.log(temp)
        filtered_display = self.post_process_image(temp)
 
        #filtered_display = filtered_display* filter
        for x in range(0, self.image.shape[0]):
            for y in range(0, self.image.shape[1]):
                filtered_display[x,y] = filtered_display[x,y]* filter[x,y]
       
        final_img = np.fft.ifft2(np.fft.ifftshift(filtered))
        result = np.abs(final_img)
        result = self.post_process_image(result)
   
       
        return [self.post_process_image(np.log(np.abs(FFT))), filtered_display, result ]
