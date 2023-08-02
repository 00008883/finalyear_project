import cv2
import HandLandMarkModule as HLModule
import PoseDetectionModule as PDModule
import DetectionModule as DM
import DatabaseModule as DBM
import SuggestionModule as SM
import time

def main():
    cap = cv2.VideoCapture(0)
    handDetector = HLModule.HandDetector(detectionCon=0.75, trackCon=0.75)
    poseDetector = PDModule.PoseDetector()
    chestDetectedTimes = 0
    eyeDetectedTimes = 0
    foreheadDetectedTimes = 0
    start = time.time()
    delayTime = 3

    while True:
        success, img = cap.read()
        imgHand = handDetector.findHands(img)
        imgPose = poseDetector.findPose(img)
        HandLmList = handDetector.findPosition(imgHand)
        PoseLmList = poseDetector.findPosePosition(imgPose)

        if len(PoseLmList) != 0:
            # cv2.circle(img, (PoseLmList[12][1], PoseLmList[12][2]), 5, (255, 0, 0), cv2.FILLED)
            # print(PoseLmList[11])
            # print(PoseLmList[12])

            if len(HandLmList) != 0:
                handDetector.findOverallPosition(img)
                # Max and min position of hand
                HMax_X, HMin_X, HMax_Y, HMin_Y = handDetector.findHandMinMax()
                detection = DM.BehaviorDetector(HMax_X, HMin_X, HMax_Y, HMin_Y,
                                                 PoseLmList[11], PoseLmList[12], PoseLmList[3],
                                                 PoseLmList[6], PoseLmList[7], PoseLmList[8], PoseLmList[9])

                # Function to call handsOnChest function which will return True if the hand is detected on chest
                chestDetected = detection.handsOnChest()
                # Increment detected times by one if hands detected on chest
                if chestDetected:
                    chestDetectedTimes += 1
                    #print("Chest: ", chestDetectedTimes)

                # Function to call handsOnEyes function which will return True if the hand is detected on eyes
                eyeDetected = detection.handsOnEyes()
                # Increment detected times by one if hands detected on eyes
                if eyeDetected:
                    eyeDetectedTimes += 1
                    #print("Eyes: ", eyeDetectedTimes)

                # Function to call handsOnForehead function which will return True if the hand is detected on forehead
                foreheadDetected = detection.handsOnForehead()
                # Increment detected times by one if hands detected on forehead
                if foreheadDetected:
                    foreheadDetectedTimes += 1
                    #print("Forehead: ", foreheadDetectedTimes)

                # List of detection times
                detectedTimesList = [foreheadDetectedTimes, eyeDetectedTimes, chestDetectedTimes]
                #print(detectedTimesList)


        if time.time() - start >= delayTime:
            if foreheadDetectedTimes != 0 or eyeDetectedTimes != 0 or chestDetectedTimes != 0:
                Insert = DBM.InsertData(detectedTimesList)
                SM.FindSuggestion()
            # reset the values
            foreheadDetectedTimes = 0
            eyeDetectedTimes = 0
            chestDetectedTimes = 0
            # reset the start time
            start = time.time()


        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

if __name__ == "__main__":
    main()