class BehaviorDetector():
    def __init__(self, handMax_X, handMin_X, handMax_Y, handMin_Y,
                 shoulderL, shoulderR, eyeOuterL, eyeOuterR,
                 earL, earR,  mouth_L):
        """

        :param handMax_X: position of Hand
        :param handMin_X: position of Hand
        :param handMax_Y: position of Hand
        :param handMin_Y: position of Hand
        :param shoulderL: position of Shoulder
        :param shoulderR: position of Shoulder
        :param eyeOuterL: position of Eye
        :param eyeOuterR: position of Eye
        :param earL: position of Ear
        :param earR: position of Ear
        :param mouth_L: position of Mouth
        """
        self.optimizerChest = 60
        self.optimizerForeHead_Y = 30
        self.optimizerForeHead_X = 30
        self.handMax_X = handMax_X
        self.handMin_X = handMin_X
        self.handMax_Y = handMax_Y
        self.handMin_Y = handMin_Y
        self.mouth_Y = mouth_L[2]
        self.shoulderL_X = shoulderL[1]
        self.shoulderL_Y = shoulderL[2]
        self.shoulderR_X = shoulderR[1]
        self.shoulderR_Y = shoulderR[2] + self.optimizerChest
        self.eyeL_X = earL[1]
        self.eyeOuterL_Y = eyeOuterL[2]
        self.eyeR_X = earR[1]
        self.eyeOuterR_Y = eyeOuterR[2]
        self.foreheadL_Y = self.eyeOuterL_Y - self.mouth_Y + self.eyeOuterL_Y - self.optimizerForeHead_Y
        self.foreheadR_Y = self.eyeOuterL_Y - self.mouth_Y + self.eyeOuterR_Y - self.optimizerForeHead_Y
        self.foreheadL_X = self.eyeL_X + self.optimizerForeHead_X
        self.foreheadR_X = self.eyeR_X - self.optimizerForeHead_X

    def handsOnChest(self):
        """

        :return: True if detected
        """
        if (self.shoulderL_X > self.handMax_X > self.shoulderR_X) or (
                self.shoulderL_X > self.handMin_X > self.shoulderR_X):
            if (self.handMax_Y > self.shoulderR_Y > self.handMin_Y) or (self.handMax_Y > self.shoulderL_Y > self.handMin_Y):
                return True



    def handsOnEyes(self):
        """

        :return: True if detected
        """
        if (self.eyeL_X > self.handMax_X > self.eyeR_X) or (
                self.eyeL_X > self.handMin_X > self.eyeR_X):
            if (self.handMax_Y > self.eyeOuterR_Y > self.handMin_Y) or (
                self.handMax_Y > self.eyeOuterL_Y > self.handMin_Y):
                return True

    def handsOnForehead(self):
        """

        :return: True if detected
        """
        if (self.foreheadL_X > self.handMax_X > self.foreheadR_X) or (
                self.foreheadL_X > self.handMin_X > self.foreheadR_X):
            if (self.handMax_Y > self.foreheadL_Y > self.handMin_Y) or (
                self.handMax_Y > self.foreheadR_Y > self.handMin_Y):
                return True