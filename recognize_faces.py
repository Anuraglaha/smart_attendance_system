import cv2
import face_recognition
import os
import numpy as np
#from attendance_system import markAttendance
from database import markAttendanceDB


def run_attendance(is_running, on_marked):
    # ===== LOAD KNOWN IMAGES =====
    path = "images"
    images = []
    classNames = []

    for file in os.listdir(path):

        # Skip non-image files
        if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        img_path = os.path.join(path, file)
        img = face_recognition.load_image_file(img_path)

        images.append(img)

        name = os.path.splitext(file)[0].split("_")[0]
        classNames.append(name)


    # ===== ENCODE KNOWN FACES =====
    def findEncodings(images):
        encodeList = []

        for img in images:
            encodings = face_recognition.face_encodings(img)

            if len(encodings) > 0:
                encodeList.append(encodings[0])
            else:
                print("No face found in one image")

        return encodeList


    encodeListKnown = findEncodings(images)
    print("Encoding Complete")


    # ===== START WEBCAM =====
    cap = cv2.VideoCapture(0)

    while is_running():
        success, img = cap.read()

        imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgSmall)
        encodesCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)


        # ===== COMPARE FACES =====
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace
            )

            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace
            )

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                markAttendanceDB(name)
                on_marked(name)
            else:
                name = "UNKNOWN"

            # Scale coordinates back
            y1, x2, y2, x1 = faceLoc
            y1 *= 4
            x2 *= 4
            y2 *= 4
            x1 *= 4

            # Draw box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Label box
            cv2.rectangle(img, (x1, y2 - 35),
                          (x2, y2), (0, 255, 0), cv2.FILLED)

            cv2.putText(img, name, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)


        cv2.imshow("Live Recognition", img)

        # ESC to exit
        if cv2.waitKey(1) == 27:
            break


    cap.release()
    cv2.destroyAllWindows()

#run_attendance() #for testing

'''
# ===== LOAD KNOWN IMAGES =====

path = "images"
images = []
classNames = []


for file in os.listdir(path):

    # Skip non-image files
    if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    img_path = os.path.join(path, file)
    img = face_recognition.load_image_file(img_path)

    images.append(img)

    # Extract name before underscore
    name = os.path.splitext(file)[0].split("_")[0]

    classNames.append(name)


# ===== ENCODE KNOWN FACES =====

def findEncodings(images):
    encodeList = []

    for img in images:
        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:
            encodeList.append(encodings[0])
        else:
            print("No face found in one image")

    return encodeList


encodeListKnown = findEncodings(images)
print("Encoding Complete")


# ===== START WEBCAM =====

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()

    # Resize for speed
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)

    # Convert BGR → RGB
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    # Detect faces
    facesCurFrame = face_recognition.face_locations(imgSmall)

    # Encode faces
    encodesCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)


    # ===== COMPARE FACES =====

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

        matches = face_recognition.compare_faces(
            encodeListKnown, encodeFace
        )

        faceDis = face_recognition.face_distance(
            encodeListKnown, encodeFace
        )

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # Mark attendance in Db
            markAttendanceDB(name)

        else:
            name = "UNKNOWN"

        # Scale coordinates back
        y1, x2, y2, x1 = faceLoc
        y1 *= 4
        x2 *= 4
        y2 *= 4
        x1 *= 4

        # Draw box
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Label box
        cv2.rectangle(img, (x1, y2 - 35),
                      (x2, y2), (0, 255, 0), cv2.FILLED)

        cv2.putText(img, name, (x1 + 6, y2 - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 255), 2)


    cv2.imshow("Live Recognition", img)

    # ESC to exit
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()

'''