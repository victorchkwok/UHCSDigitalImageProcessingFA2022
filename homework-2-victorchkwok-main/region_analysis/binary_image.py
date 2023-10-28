class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        
        for r in range(image.shape[0]):
            for c in range(image.shape[1]):
                hist[image[r,c]]+=1
       
        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram it to find the otsu's threshold assuming that the input hstogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value (otsu's threshold)"""
        total =0
        threshold = 0
        for r in range(256):
            total = total + hist[r]
        
        Max = 0
        for r in range(256):
            bpix = 0
            fpix = 0
            ub = 0
            uf = 0
            for v in range(r):
                bpix = bpix + hist[v]
                ub = ub + hist[v]*v
                
            for t in range(r,256):
                fpix = fpix + hist[t]
                uf = uf + hist[t]*t
            
            if(bpix <= 0):
                continue
            elif(fpix <= 0):
                continue
            else:
                ub = ub/bpix
                uf = uf/fpix
            Wb = bpix/total
            Wf = fpix/total
            
            o = Wb*Wf*((ub-uf)**2)
            
            if(Max < o):
                threshold = r
                Max = o

            
            

      
        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        histogram = self.compute_histogram(image)
        threshold = self.find_otsu_threshold(histogram)

        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                if image[x][y] < threshold:
                    image[x][y] = 255
                else:
                    image[x][y] = 0
        bin_img = image.copy()
       
        

        return bin_img


