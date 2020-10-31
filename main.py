import cv2
import imutils
import numpy as np


def read_video_file():
    # filename = input("Enter video file name: ")
    filename = "resources/sample-5.mp4"
    return cv2.VideoCapture(filename)

def display_video_result():
    capture = read_video_file()
    while capture.isOpened():
        ret, frame = capture.read()

        frame = imutils.resize(frame, width=400)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)

        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30,
                                   minRadius=0, maxRadius=0)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            print(len(circles[0, :]))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(frame, center, 1, (0, 10, 10), 3)
                # circle outline
                radius = i[2]
                cv2.circle(frame, center, radius, (255, 0, 255), 3)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_video_result()
