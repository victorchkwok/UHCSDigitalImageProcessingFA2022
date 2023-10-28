import numpy as np
import math

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        total = 0
        gaussian = np.zeros((5, 5))
        sigma = 5
        for u in range(gaussian.shape[0]):
            for v in range(gaussian.shape[1]):
              x = u - 2
              y = v - 2
              gaussian[u,v] = (1/(2*math.pi*(sigma**2)))*(math.pow(math.e,-1*((math.pow(x,2)+math.pow(y,2))/(2*math.pow(sigma,2)))))             
              total = total + gaussian[u,v]
        print(gaussian) 
        print(total)
        gaussian = gaussian/total
        sum = 0
        for u in range(gaussian.shape[0]):
            for v in range(gaussian.shape[1]):
                sum = sum + gaussian[u,v]
        print(gaussian)  
        print(int(sum))
        return gaussian

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        Laplacian= np.zeros((3,3))
        Laplacian[0,1] =1   
        Laplacian[1,0] =1
        Laplacian[2,1] =1
        Laplacian[1,2] = 1
        Laplacian[1,1] = -4

        print(Laplacian)
        return Laplacian

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        nimage = self.image.copy()
        gf = self.get_gaussian_filter()
        lf = self.get_laplacian_filter() 
        for k in range(-1,2):
            for j in range(-1,2):
                print(lf[k+1,j+1])
                print(3+k," ",3+j)

        for u in range(self.image.shape[0]):
            for v in range(self.image.shape[1]):
                sum = 0  
                if(filter_name ==  "gaussian"):
                    for k in range(-2,3):
                        for j in range(-2,3):
                            if(0<u+k<self.image.shape[0] and 0<v+j<self.image.shape[1]):
                                sum = sum + self.image[u+k,v+j]*gf[k+2,j+2]
                    nimage[u,v] = sum
                if(filter_name ==  "laplacian"):
                    for k in range(-1,2):
                        for j in range(-1,2):
                            if(0<u+k<self.image.shape[0] and 0<v+j<self.image.shape[1]):
                                sum = sum + self.image[u+k,v+j]*lf[k+1,j+1]
                    if(sum<0):
                        sum = 0
                    if(sum>255):
                        sum = 255
                    nimage[u,v] = sum    
            
        
        return nimage



