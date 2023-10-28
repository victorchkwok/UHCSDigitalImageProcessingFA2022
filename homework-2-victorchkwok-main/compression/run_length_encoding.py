import numpy as np

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        row = binary_image.shape[0]
        columns = binary_image.shape[1]
        rle_code = []
        for x in range(row):
            colour = binary_image[x, 0]
            rle_code.append(str(binary_image[x, 0]))
            c = 0
            for y in range(columns):
                if binary_image[x, y] == colour:
                    c = c + 1
                else:
                    rle_code.append(c)
                    colour = binary_image[x, y]
                    c = 1
            rle_code.append(c)

        return rle_code  # replace zeros with rle_code

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        image = np.zeros((height, width))
        colour = 0
        r = 0
        c = 0
        for i in range(len(rle_code)):
            if rle_code[i] == '255':
                    colour = 255
            elif rle_code[i] == '0':
                    colour = 0
            else:
                if colour == 255 :
                    for k in range(rle_code[i]):
                        image[r,c] = colour
                        c = c + 1
                        if(c >= width):
                            c = 0
                            r = r + 1
                    colour = 0
                else:    
                    for k in range(rle_code[i]):
                        image[r,c] = colour
                        c = c + 1
                        if(c >= width):
                            c = 0
                            r = r + 1
                    colour = 255
                       

        


        
        
                

        return  image#image  # replace zeros with image reconstructed from rle_code





        




