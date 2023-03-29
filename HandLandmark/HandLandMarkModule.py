import cv2
import mediapipe as mp
import numpy as np

class HandDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackCon=0.5):
        """

        :param mode: Whether to treat the input images as a batch of static
        and possibly unrelated images, or a video stream. By default, it is false
        :param maxHands: Maximum number of hands to detect. Default is 2
        :param model_complexity: Complexity of the hand landmark model: 0 or 1.
        Landmark accuracy as well as inference latency generally go up with the
        model complexity. Default is 1
        :param detectionCon: Minimum confidence value ([0.0, 1.0]) for hand
        detection to be considered successful. Default is 0.5
        :param trackCon: Minimum confidence value ([0.0, 1.0]) for the
        hand landmarks to be considered tracked successfully. Default is 0.5
        """
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        # Setting given values to Hands function
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """

        :param img: image or video caption
        :param draw: To draw hand landmark with all points
        :return: image
        """
        # Changing image to RGB from BRG format
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # Drawing default skeleton
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0):
        """

        :param img: image or video caption
        :param handNo: Point of the hand, one only
        :return: list[id, x, y] coordinates with id of the hand
        """
        # Creating a list for position
        self.lmList = []
        if self.results.multi_hand_landmarks:
            # Getting selected hand landmark (20 different hand landmarks available)
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
        return self.lmList

    def findOverallPosition(self, img, handsNo=21, draw=True):
        """

        :param img: image or video caption
        :param handsNo: By default there is 21 points in hands,
                        change the parameter if it is different
        :param draw: To show rectangle on the hand
        :return: To return Max Min positions use findHandMinMax function
        """
        self.listx = []
        self.listy = []
        #self.x_axis_array = np.array()
        for i in range(handsNo):
            self.listx.append(self.lmList[i][1])
            self.listy.append(self.lmList[i][2])

        self.x_max = max(self.listx)
        self.x_min = min(self.listx)
        self.y_max = max(self.listy)
        self.y_min = min(self.listy)

        if draw:
            cv2.line(img, (self.x_min, self.y_min),(self.x_min, self.y_max),(255,255,255), 4)
            cv2.line(img, (self.x_max, self.y_max),(self.x_min, self.y_max),(255,255,255), 4)
            cv2.line(img, (self.x_max, self.y_max),(self.x_max, self.y_min),(255,255,255), 4)
            cv2.line(img, (self.x_min, self.y_min),(self.x_max, self.y_min),(255,255,255), 4)

    def findHandMinMax(self):
        """
        Returns values from findOverallPosition function
        :return: X max point, X min point, Y max point, Y min point
        """
        return self.x_max, self.x_min, self.y_max, self.y_min

