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


def gpt_example_1():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        # Define region of interest (ROI)
        roi = frame[100:400, 100:400]
        cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)

        # Preprocess ROI
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        gesture = "No hand"

        if contours:
            cnt = max(contours, key=cv2.contourArea)

            # Draw contour
            cv2.drawContours(roi, [cnt], -1, (255, 0, 0), 2)

            # Convex hull
            hull = cv2.convexHull(cnt)
            cv2.drawContours(roi, [hull], -1, (0, 255, 0), 2)

            # Convexity defects
            hull_indices = cv2.convexHull(cnt, returnPoints=False)
            if len(hull_indices) > 3:
                defects = cv2.convexityDefects(cnt, hull_indices)
                if defects is not None:
                    finger_count = 0
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(cnt[s][0])
                        end = tuple(cnt[e][0])
                        far = tuple(cnt[f][0])
                        a = np.linalg.norm(np.array(end) - np.array(start))
                        b = np.linalg.norm(np.array(far) - np.array(start))
                        c = np.linalg.norm(np.array(end) - np.array(far))
                        angle = np.degrees(np.arccos((b**2 + c**2 - a**2) / (2 * b * c)))
                        if angle <= 90 and d > 10000:
                            finger_count += 1
                            cv2.circle(roi, far, 8, (0, 0, 255), -1)

                    if finger_count == 0:
                        gesture = "Fist"
                    elif finger_count == 1:
                        gesture = "One"
                    elif finger_count == 2:
                        gesture = "Two"
                    elif finger_count == 3:
                        gesture = "Three"
                    elif finger_count == 4:
                        gesture = "Open palm"
                    else:
                        gesture = "Unknown"

        cv2.putText(frame, f"Gesture: {gesture}", (50, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

        cv2.imshow("Gesture Recognition", frame)
        cv2.imshow("Threshold", thresh)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    gpt_example_1()
