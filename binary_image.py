import math as m
import numpy as np
class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram as a list"""

        hist = [0]*256
        height,width=np.shape(image)
        for i in range(height):
            for j in range(width):
                # k= image[i,j]
                hist[image[i,j]]+=1

        return hist

    def find_otsu_threshold(self, hist):
        """analyses a histogram to find the otsu's threshold assuming that the input histogram is bimodal.
        takes as input
        hist: a histogram
        returns: an optimal threshold value (otsu's threshold)"""

 
        threshold = 0
        t_value = [0] * 256
        sum=0
        w1,w2,m1,m2,var_left,var_right,wcv,value=0,0,0,0,0,0,0,0

        # print(np.shape(hist))
        size = np.shape(hist)[0]
        for i in range(size):
            sum += hist[i]
        # print("sum", sum)
        for t in range(1,size):
            temp=0
            temp1=0
            temp2=0
            for i in range(t):
                temp+=hist[i]
                temp1+=i*hist[i]
            w1=temp/sum
            if temp!=0:
                m1=temp1/temp
            else:
                m1=0
            for i in range(t ):
                temp2+=m.pow((i-m1),2)*hist[i]
            if temp!=0:
                var_left=temp2/temp
            else:
                var_left=0
            for i in range(t,size):
                temp+=hist[i]
                temp1 += i * hist[i]
            w2=temp/sum
            if temp != 0:
                m2 = temp1 / temp
            else:
                m2 = 0
            for i in range(t,size):
                temp2+=m.pow((i-m2),2)*hist[i]
            if temp!=0:
                var_right=temp2/temp
            else:
                var_right=0
            wcv=(w1*var_left)+(w2*var_right)

            t_value[t]=wcv
        t_value.pop(0)
        value=min(t_value)
        for k in range(np.shape(t_value)[0]):
            if value==t_value[k]:
                threshold=k

        # print("thre",threshold)

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        Make calls to the compute_histogram and find_otsu_threshold methods as needed.
        takes as input
        image: an grey scale image
        returns: a binary image"""

        hist=BinaryImage.compute_histogram(self,image)
        t=BinaryImage.find_otsu_threshold(self,hist)
        t= 130
        box3 = np.zeros((np.shape(image)[0], np.shape(image)[1]), np.uint8)
        for i in range(np.shape(image)[0]):
            for j in range(np.shape(image)[1]):
                if image[i,j]>t:
                    box3[i,j]=0
                else:
                    box3[i,j]=255

        return box3


