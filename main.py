import numpy as np
import cv2
import imutils


def read_video_file():
    # filename = input("Enter video file name: ")
    filename = "/resources/sample-1.mp4"
    return cv2.VideoCapture(filename)


def display_video_result():
    capture = read_video_file()
    while capture.isOpened():
        ret, frame = capture.read()

        frame = imutils.resize(frame, width=1000)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow('frame', hsv)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_video_result()
