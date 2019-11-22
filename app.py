import cv2
import numpy as np

Camera = cv2.VideoCapture(0)

settings = np.zeros([100, 700], np.uint8)
cv2.namedWindow('Settings')


def Callback(x=0):
    pass


cv2.createTrackbar('L - h', 'Settings', 0, 179, Callback)
cv2.createTrackbar('U - h', 'Settings', 179, 179, Callback)
cv2.createTrackbar('L - s', 'Settings', 0, 255, Callback)
cv2.createTrackbar('U - s', 'Settings', 255, 255, Callback)
cv2.createTrackbar('L - v', 'Settings', 0, 255, Callback)
cv2.createTrackbar('U - v', 'Settings', 255, 255, Callback)


while True:
    _, frame = Camera.read()  # Get camera freams

    frame = cv2.flip(frame, flipCode=1)  # Flip frame vertically

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get filter settings
    l_h = cv2.getTrackbarPos('L - h', 'Settings')
    u_h = cv2.getTrackbarPos('U - h', 'Settings')
    l_s = cv2.getTrackbarPos('L - s', 'Settings')
    u_s = cv2.getTrackbarPos('U - s', 'Settings')
    l_v = cv2.getTrackbarPos('L - v', 'Settings')
    u_v = cv2.getTrackbarPos('U - v', 'Settings')

    lower_background = np.array([l_h, l_s, l_v])
    upper_background = np.array([u_h, u_s, u_v])

    hideMask = cv2.inRange(hsv, lower_background, upper_background)
    showMask = cv2.bitwise_not(hideMask)

    show = cv2.bitwise_and(frame, frame, mask=showMask)

    cv2.setWindowProperty(
        'Camera', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Camera", show)  # Create window and show camera frames

    keyPressCode = cv2.waitKey(30)

    if keyPressCode == 27:  # If pressed key be ESC
        break


Camera.release()
cv2.destroyAllWindows()
