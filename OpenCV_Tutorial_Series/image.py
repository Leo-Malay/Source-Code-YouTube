# Importing the modules.
import cv2

# Readng the image.
img = cv2.imread("./res/malay_1.jpg")


# Getting the shape of the mimage.
shape = img.shape

# Getting the number of pixels in images.
size = img.size

print("Shape of Image(h,w,c): ", shape)
print("Number of Pixels: ", size)

# Reducing the size(1/8)
red_img = cv2.resize(img, (int(shape[1]/8), int(shape[0]/8)))

# Convert to gray scale.
gray = cv2.cvtColor(red_img, cv2.COLOR_BGR2GRAY)

# Displaying the images.
while True:
    cv2.imshow("Name of the window", gray)

    if cv2.waitKey(0) == ord('q'):
        break
    elif cv2.waitKey(0) == ord('s'):
        # Save the image.
        cv2.imwrite("./test.jpg", gray)

cv2.destroyAllWindows()
