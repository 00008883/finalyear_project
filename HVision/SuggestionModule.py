import DatabaseModule as DBM
from SpeechRecognitionModule import SpeechRec
import speech_recognition as sr

def FindSuggestion():
    lastDetection = DBM.GetDetection()

    #print(lastDetection)

    # Assigning corresponding values to detections
    foreheadTimes = lastDetection[0]
    eyeTimes = lastDetection[1]
    chestTimes = lastDetection[2]
    Limit = 1
    ExtremeLimit = 30

    # Suggestion if detected headache
    fsuggestion = "Headache \n" \
                  "1. Please pull over the to the safe place and stop the vehicle \n" \
                  "2. If you feel bad, take medication immediately \n" \
                  "3. Get some rest but make sure that you have stopped the vehicle \n" \
                  "4. Drink water \n" \
                  "5. If headache does not stop I can call emergency \n"
    # Emergency case for forehead problems
    fxsuggestion = "ALERT FOREHEAD \n"

    # Suggestion for vision problems
    esuggestion = "Vision \n" \
                  "1. Stop driving and pull over to the safe place \n" \
                  "2. If you have diabetes treat your blood sugar \n" \
                  "3. Try to exercise your eyes and check for vision problems \n"
    # Emergency case in vision problem
    exsuggestion = "ALERT EYES \n"

    # Suggestion for pain in the chest
    csuggestion = "Chest \n" \
                  "1. Stop the vehicle in the safe place \n" \
                  "2. If you have your medication you should take them \n" \
                  "3. Try to relax and breathe without panic \n" \
                  "4. If there is still problem I will call an emergency \n"
    # Emergency case in problem with chest
    cxsuggestion = "ALERT CHEST \n"
    extremeCalling = "EMERGENCY CALL ...."

    # Calling speech recognition function
    answer = speechRecognition()

    # Check number of times hand occurred on forehead
    if Limit <= foreheadTimes < ExtremeLimit:
        # If more than given limit but below extreme limit do following
        if answer:
            print(fsuggestion)
    elif foreheadTimes > ExtremeLimit:
        # If more than given extreme limit do following
        if answer:
            # Suggestion with calling emergency
            print(fxsuggestion, extremeCalling)
        # If no answer then do emergency call
        elif answer == None:
            print (extremeCalling)
    if Limit <= eyeTimes < ExtremeLimit:
        if answer:
            print(esuggestion)
    elif eyeTimes > ExtremeLimit:
        if answer:
            print(exsuggestion, extremeCalling)
        elif answer == None:
            print(extremeCalling)

    if Limit <= chestTimes < ExtremeLimit:
        if answer:
            print(csuggestion)
    elif chestTimes > ExtremeLimit:
        if answer:
            print(cxsuggestion, extremeCalling)
        elif answer == None:
            print(extremeCalling)

def speechRecognition():
    # Getting speech recognition module
    srm = SpeechRec()
    try:
        # Voice recognition online or offline mode: True means offline, False is online
        text = srm.getUserSpeech(False)
        # User input into ML
        answer = srm.analyzeText(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    if answer == "agree":
        return True
    elif answer == "not agree":
        return False
    else:
        return None
def main():
    FindSuggestion()

if __name__ == "__main__":
    main()