import cv2 as cv


def get_pixel_rgb(image, x, y):
    (B, G, R) = image[x, y]
    return R, G, B


def get_image_region(image, x, y):
    return image[y[0]:y[1], x[0]:x[1]]


def resize(image, x, y):
    return cv.resize(image, (x, y))