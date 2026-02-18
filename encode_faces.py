import face_recognition
import os

# Path to images folder
path = "images"

images = []
classNames = []

# Load images and names
for file in os.listdir(path):
    img_path = os.path.join(path, file)
    img = face_recognition.load_image_file(img_path)

    images.append(img)

    # Remove extension -> name
    name = os.path.splitext(file)[0]
    classNames.append(name)

print("Names found:", classNames)

'''
# Function to encode faces
def findEncodings(images):
    encodeList = []

    for img in images:
        enc = face_recognition.face_encodings(img)[0]
        encodeList.append(enc)

    return encodeList
'''
def findEncodings(images):
    encodeList = []

    for img in images:
        encodings = face_recognition.face_encodings(img)

        if len(encodings) > 0:
            encodeList.append(encodings[0])
        else:
            print("No face found in one image — skipped")

    return encodeList


encodeListKnown = findEncodings(images)

print("Encoding Complete")
print("Total faces encoded:", len(encodeListKnown))
