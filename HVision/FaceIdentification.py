import sys
import cv2
from FaceRecognitionModule import FaceRec


sfr = FaceRec()
sfr.load_encoding_images("Faces/")

def main():
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        face_location, face_names = sfr.detect_known_faces(img)
        for face_loc, name in zip(face_location, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1],face_loc[2], face_loc[3]

            cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,200), 2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,200), 4)

            if name != "Unknown" and not None:
                return name


        #cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

if __name__ == "__main__":
    main()


