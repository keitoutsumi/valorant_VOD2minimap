import cv2
import numpy as np

def preprocess_image(image, threshold=103):
    binary_thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
    mask = binary_thresh > 0
    image_copy = image.copy()
    image_copy[~mask] = 0
    return image_copy

def convert_to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
