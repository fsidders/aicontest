import cv2
import string
import random
import time


def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    ms = time.time_ns()
    idn = "".join(random.choice(chars) for _ in range(size))
    return "tvhelper_" + str(ms) + "_" + str(idn) + ".jpg"


def capture(directory):
    cap = cv2.VideoCapture(0)

    # Check if camera was opened correctly
    if not (cap.isOpened()):
        print("Could not open video device")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    ret, frame = cap.read()
    filename = directory + name_generator()

    cv2.imwrite(filename, frame)

    cap.release()
    cv2.destroyAllWindows()

    return filename
