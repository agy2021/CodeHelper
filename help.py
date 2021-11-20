import cv2
import time

def main_help():
    time.sleep(1)

    cap = cv2.VideoCapture("help.mov")

    while True:
        ret, frame = cap.read()

        cv2.imshow("Press Any Key to Close", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()