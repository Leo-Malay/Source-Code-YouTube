# Importing the module.
import cv2

# Getting the hold of the camera.
vid = cv2.VideoCapture(0)

# Setting the codec.
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Output_file.avi", fourcc, 20.0, (640, 480))

# Displaying the video.
while True:
    # Reading frame by frame
    ret, frame = vid.read()

    # Displaying.
    cv2.imshow("Video Frame", frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
vid.release()
cv2.destroyAllWindows()
