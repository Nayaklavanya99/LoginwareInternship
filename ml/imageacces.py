import cv2
import time

img = cv2.imread("test2.jpg", cv2.IMREAD_COLOR)
if img is None:
    print("Error: Could not load image")
    exit()
height, width = img.shape[:2]
max_width = 1024
max_height = 768

scale = min(max_width / width, max_height / height)

new_width = int(width * scale)
new_height = int(height * scale)

resized_img = cv2.resize(img, (new_width, new_height))
cv2.imshow("image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
