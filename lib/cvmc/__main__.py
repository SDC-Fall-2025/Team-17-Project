import cv2
import numpy as np

def gpt_example():
    cap = cv2.VideoCapture(0)

    # store the previous frame to compare motion
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    circle_x, circle_y = 320, 240

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        motion = cv2.moments(thresh)

        # compute the "center" of motion
        if motion["m00"] > 0:
            cx = int(motion["m10"] / motion["m00"])
            cy = int(motion["m01"] / motion["m00"])
            # move the circle toward motion center
            circle_x = int(0.9 * circle_x + 0.1 * cx)
            circle_y = int(0.9 * circle_y + 0.1 * cy)

        # draw things
        cv2.circle(frame, (circle_x, circle_y), 40, (0, 255, 0), -1)
        cv2.imshow("Motion mapped to circle", frame)

        prev_gray = gray

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    gpt_example()
