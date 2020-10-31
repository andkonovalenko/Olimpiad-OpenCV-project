import cv2
import imutils
import numpy as np


def save_video_result():
    filename = "resources/sample-5.mp4"
    output = "out.avi"

    capture = cv2.VideoCapture(filename)
    fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
    video_recorder = cv2.VideoWriter(output, fourcc, 20.0, (int(capture.get(3)), int(capture.get(4))))

    while capture.isOpened():
        ret, frame = capture.read()
        # frame = imutils.resize(frame, width=400)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=40, minRadius=50, maxRadius=100)
        count = 0
        if circles is not None:
            print(len(circles[0, :]))
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                count += 1
                center = (i[0], i[1])
                # circle center
                cv2.circle(frame, center, 1, (0, 10, 10), 3)
                # circle outline
                radius = i[2]
                cv2.circle(frame, center, radius, (255, 0, 255), 3)
                font = cv2.FONT_HERSHEY_SIMPLEX

                font_scale = 2
                thickness = 3
                color = (255, 0, 0)

                cv2.putText(frame, str(count), center, font, font_scale, color, thickness, cv2.LINE_AA)
        video_recorder.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save_video_result()
