import cv2
from cv2 import imshow
import dlib
# read image
img = cv2.imread('image.jpeg')
# convert image to grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# dlib:  load face recognition detector
face_detector = dlib.get_frontal_face_detector()
# load predictor
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# use detector to find face landmarks
faces = face_detector(gray)
print('There are ' + str(len(faces)) + ' faces')

for face in faces:
    x1 = face.left()  # left point
    y1 = face.top()  # top point
    x2 = face.right()  # right point
    y2 = face.bottom()  # bottom point
    # draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(
        x2, y2), color=(0, 255, 0), thickness=2)

    face_features = predictor(image=gray, box=face)
    # loop through all 68 points
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y
        # draw circle
        cv2.circle(img=img, center=(x, y), radius=2,
                   color=(0, 0, 255), thickness=1)
# show the image
cv2.imshow(winname='Face Recognition', mat=img)
# wait for the key pressed to exit
cv2.waitKey(delay=0)
# close all windows
cv2.destroyAllWindows()
