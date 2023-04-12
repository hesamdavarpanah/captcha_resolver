import numpy as np
import cv2
from PIL import Image
import extcolors
import matplotlib.pyplot as plt


class DSP:
    def __init__(self):
        self.image = Image.open("captcha.jpg")
        self.cv2img = cv2.imread("captcha.jpg")

    @property
    def get_color(self):
        colors_x = extcolors.extract_from_image(self.image, tolerance=5)
        single_color = colors_x[0][2][0]
        return single_color

    def image_editor(self, start_color_range, end_color_range):
        image_data = self.image.load()

        height, width = self.image.size
        for loop1 in range(height):
            for loop2 in range(width):
                r, g, b = image_data[loop1, loop2]
                if not (start_color_range[0] < r < end_color_range[0]) \
                        and not (start_color_range[1] < g < end_color_range[1]) \
                        and not (start_color_range[2] < b < end_color_range[2]):
                    image_data[loop1, loop2] = 0, 0, 0

        open_cv_image = np.array(self.image)

        open_cv_image = open_cv_image[:, :, ::-1].copy()
        conv_img_down0 = cv2.pyrDown(open_cv_image)
        conv_img_down3 = cv2.pyrUp(conv_img_down0)

        kernel = np.ones((2, 2), np.float32) / (2 * 2)
        conv_img = cv2.filter2D(conv_img_down3, -1, kernel)

        img = cv2.cvtColor(conv_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(img, (1, 1), 0)
        ret1, th1 = cv2.threshold(blur, 44, 255, cv2.THRESH_BINARY)
        return th1

    def image_editor2(self, color_range):
        start_range = []
        end_range = []
        for color in color_range:
            if color >= 220:
                start_range.append(color - 30)
                end_range.append(255)
            else:
                start_range.append(color - 30)
                end_range.append(color + 30)
        start_color_range = np.array(start_range)
        end_color_range = np.array(end_range)
        rgb = cv2.cvtColor(self.cv2img, cv2.COLOR_BGR2RGB)
        msk = cv2.inRange(rgb, start_color_range, end_color_range)
        krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        dlt = cv2.dilate(msk, krn, iterations=5)
        res = 255 - cv2.bitwise_and(dlt, msk)

        kernel = np.ones((2, 2), np.float32) / (2 * 2)
        conv_img = cv2.filter2D(res, -1, kernel)

        blur = cv2.GaussianBlur(conv_img, (5, 5), 0)

        ret, thresh1 = cv2.threshold(blur, 179, 255, cv2.THRESH_BINARY)

        _, black_and_white = cv2.threshold(thresh1, 127, 255, cv2.THRESH_BINARY_INV)

        n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(black_and_white, None, None, None, 8,
                                                                              cv2.CV_32S)
        sizes = stats[1:, -1]
        img2 = np.zeros(labels.shape, np.uint8)

        for i in range(0, n_labels - 1):
            if sizes[i] >= 27:
                img2[labels == i + 1] = 255

        res = cv2.bitwise_not(img2)

        return res


