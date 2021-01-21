# Importing the module.
import cv2
import numpy

# Creatng an empty image.
img = numpy.zeros((600, 600, 3), numpy.uint8)

# Adding differet elements.
img = cv2.line(img, (50, 50), (150, 150), (255, 255, 0), 2, cv2.LINE_AA)

img = cv2.rectangle(img, (150, 150), (300, 400), (0, 255, 255), 2, cv2.LINE_AA)

img = cv2.circle(img, (255, 275), 30, (255, 0, 255), 2, cv2.LINE_AA)

img = cv2.ellipse(img, (500, 500), (100, 60), 30, 0, 360, (255, 255, 255), 2)

img = cv2.putText(img, "Hello, I am Malay", (100, 500),
                  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Displaying the image.
cv2.imshow("MY Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
