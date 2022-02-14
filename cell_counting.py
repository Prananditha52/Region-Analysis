import numpy as np
import cv2
class CellCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window and assigns region names
        takes a input:
        image: binary image
        return: a list/dict of regions"""
        regions = dict()
        count = 1
        
        # row,coloum = np.shape(img)
        new_img = np.zeros((np.shape(image)[0] + 2, np.shape(image)[1] + 2), np.uint8)
        for i in range(np.shape(image)[0]):
            for j in range(np.shape(image)[1]):
                new_img[i + 1, j + 1] = image[i, j]
        region_img = np.zeros((np.shape(image)[0] + 2, np.shape(image)[1] + 2), np.uint8)
        # print(new_img)
        for i in range(np.shape(new_img)[0]):
            for j in range(np.shape(new_img)[1]):
                if new_img[i, j] == 255 and new_img[i, j - 1] == 0 and new_img[i - 1, j] == 0:
                    region_img[i, j] = count
                    count = count + 1
                    regions[str(region_img[i, j])] = []
                    regions[str(region_img[i, j])].append((i, j))
                elif new_img[i, j] == 255 and new_img[i, j - 1] == 0 and new_img[i - 1, j] == 255:
                    region_img[i, j] = region_img[i - 1, j]
                    regions[str(region_img[i, j])].append((i, j))
                elif new_img[i, j] == 255 and new_img[i, j - 1] == 255 and new_img[i - 1, j] == 0:
                    region_img[i, j] = region_img[i, j - 1]
                    regions[str(region_img[i, j])].append((i, j))
                elif new_img[i, j] == 255 and new_img[i, j - 1] == 255 and new_img[i - 1, j] == 255:
                    region_img[i, j] = region_img[i - 1, j]
                    regions[str(region_img[i, j])].append((i, j))
                    regions[str(region_img[i, j])].extend(regions[str(region_img[i, j - 1])])
                    regions[str(region_img[i, j - 1])].clear()
        for i in range(len(regions)):
            if len(regions[str(i)]) == 0:
                regions.pop(str(i))
        #         print(regions)
        #         print(len(regions))
        print(regions)
        return regions
    def compute_statistics(self, region):
        """Computes cell statistics area and location
        takes as input
        region: list regions and corresponding pixels
        returns: stats"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)
        stats = region
        for key, value in list(region.items()):
            area = len(value)
            X, Y = (1 / area) * np.sum(value, axis=0)
            center = (np.uint8(X), np.uint8(Y))
            stats[key] = []
            stats[key].append(center)
            stats[key].append(area)
            # print(stats)
        return stats
    def mark_image_regions(self, image, stats):
        """Creates a new image with computed stats
        Make a copy of the image on which you can write text. 
        takes as input
        image: Input binary image
        stats: stats regarding location and area
        returns: image marked with center and area"""
        comp_image = image
        # comp_image = np.uint8(255 - image)

        # color=(125, 246, 55)
        for key, value in list(stats.items()):
            centroid = value[0]
            area = value[1]
            # cv2.putText(comp_image, '*' + str(key) + ',' + str(area), (centroid[1], centroid[0]),
            #             cv2.FONT_HERSHEY_DUPLEX, 0.3, 80)
            cv2.putText(comp_image, '*' + str(key) + ',' + str(area), (centroid[1], centroid[0]),
                                     cv2.FONT_HERSHEY_DUPLEX, 0.3,
                                     (255, 0, 0))

        return comp_image
