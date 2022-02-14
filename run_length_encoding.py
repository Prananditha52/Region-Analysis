import numpy as np
class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        For efficiency, flatten the image by concatinating rows to create one long array, and
        compute run length encoding.
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        rle=[]
        
        for i in range(np.shape(binary_image)[0]):
            iv = binary_image[i, 0]
            rle.append(str(binary_image[i, 0]))
            count = 0
            for j in range(np.shape(binary_image)[1]):
               if binary_image[i,j]==iv:
                   count+=1
               else:
                   rle.append(count)
                   count = 1
                   iv = binary_image[i, j]
            rle.append(count)

#         print(np.shape(binary_image))
#         print(rle)



        return rle 


    def decode_image(self, rle_code, height , width):
        """
        Since the image was flattened during the encoding, use the hight and width to reconstruct the image
        Reconstructs original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        decode = []
        for i in range(len(rle_code)):
            if rle_code[i] == '255':
                a = 255
            elif rle_code[i] == '0':
                a = 0
            else:
                if a == 255:
                    decode.append(255 * np.ones(rle_code[i]))
                    a = 0
                else:
                    decode.append(np.zeros(rle_code[i]))
                    a = 255

        decoded = [j for i in decode for j in i]
        decode_image=np.array(decoded).reshape(height,width)

        return decode_image
