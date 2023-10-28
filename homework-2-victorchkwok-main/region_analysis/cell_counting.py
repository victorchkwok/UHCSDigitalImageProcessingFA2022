import cv2
import numpy as np
class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""
        R = np.zeros(image.shape)
        k = 1
        regions = dict()
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                if i == 0:
                    image[i - 1, j] = 0
                if j == 0:
                    image[i, j - 1] = 0
                if i == 0 and j == 0:
                    image[i - 1, j - 1] = 0

                if(image[i,j]==255 and image[i,j-1]==0 and image[i-1,j]==0):
                    R[i][j] = k
                    k =  k+1
                if(image[i,j]==255 and image[i,j-1]==0 and image[i-1,j]==255):
                    R[i][j] = R[i-1][j]
                if(image[i,j]==255 and image[i,j-1]==255 and image[i-1,j]==0):
                    R[i][j] = R[i][j-1]
                if(image[i,j]==255 and image[i,j-1]==255 and image[i-1,j]==255):
                    R[i][j] = R[i-1][j]
                    if(R[i,j-1] != R[i-1,j]):
                        temp = R[i - 1, j]
                        for x in range(R.shape[0]):
                                for y in range(R.shape[1]):
                                    if R[x, y] == temp:
                                        R[x, y] = R[i, j - 1]
        count = 1
        for colour in range(k):
            for i in range(R.shape[0]):
                for j in range(R.shape[1]):
                    if R[i, j] == colour:
                        if count in regions.keys():
                            regions[count].append((i, j))
                        else:
                            regions.update({count: [(i, j)]})

            if count in regions.keys():
                count += 1
        
        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        stats = []
        c = 0
        for key in region.keys():
            if len(region[key]) > 15:
                pixels = region[key]
                x = 0
                y = 0
                A = len(region[key])
                c += 1
                for points in pixels:
                    x += points[0]
                    y += points[1]
                x = int(x/len(region[key]))
                y = int(y/len(region[key]))
                centroid =(x,y)
                stats.append([c,A,centroid])
                print("Region: ", c, "Area: ", A, "Centroid", centroid)

        return stats

    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for Label in stats:
            c = str(Label[0])
            A = str(Label[1])
            label = c + ", "+ A
            centroid = Label[2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            colour = (0,0,255)
            image = cv2.putText(image,"*", (centroid[1],centroid[0]),font,0.25,(0,0,255),1)
            image = cv2.putText(image, label, (centroid[1],centroid[0]+5),font,0.25,colour,1)

        return image