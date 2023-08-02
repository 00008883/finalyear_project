import cv2
import mediapipe as mp

class PoseDetector():

    def __init__(self, mode=False, complexity=1, smoothLandmarks=True,
                 enableSeg=False, smoothSeg=True, detectionConf=0.5, trackConf=0.5):
        """

        :param mode: Whether to treat the input images as a batch of static
        and possibly unrelated images, or a video stream
        :param complexity: Complexity of the pose landmark model: 0, 1 or 2. Default is 1
        :param smoothLandmarks: Whether to filter landmarks across different input
        images to reduce jitter. Default is True
        :param enableSeg: Whether to predict segmentation mask. Default is False
        :param smoothSeg: Whether to filter segmentation across different input
        images to reduce jitter. Default is True
        :param detectionConf: Minimum confidence value ([0.0, 1.0]) for person
        detection to be considered successful. Default is 0.5
        :param trackConf: Minimum confidence value ([0.0, 1.0]) for the
        pose landmarks to be considered tracked successfully. Default is 0.5
        """
        self.mode = mode
        self.complexity = complexity
        self.smoothLandmarks = smoothLandmarks
        self.enableSeg = enableSeg
        self.smoothSeg = smoothSeg
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smoothLandmarks,
                                     self.enableSeg, self.smoothSeg, self.detectionConf, self.trackConf)

    def findPose(self, img, draw=True):
        """

        :param img: image or video caption
        :param draw: Pose drawing with all points (default)
        :return: image, video caption
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosePosition(self, img):
        """

        :param img: image or video caption
        :return: list[id, X, Y] coordinates of all pose positions
        """
        self.poseLmList = []
        #If results are available then we use for loop to detect position
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #Adding positions to the list
                self.poseLmList.append([id, cx, cy])
                #cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.poseLmList
