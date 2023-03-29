import DatabaseModule as DBM

def FindSuggestion():
    lastDetection = DBM.GetDetection()
    print(lastDetection)

    foreheadTimes = lastDetection[0]
    eyeTimes = lastDetection[1]
    chestTimes = lastDetection[2]
    Limit = 1
    ExtremeLimit = 30

    fsuggestion = "Forehead suggestion 1"
    fxsuggestion = "ALERT FOREHEAD"
    esuggestion = "Eye suggestion 1"
    exsuggestion = "ALERT EYES"
    csuggestion = "Chest suggestion 1"
    cxsuggestion = "ALERT CHEST"

    if Limit <= foreheadTimes < ExtremeLimit:
        print(fsuggestion)
    elif foreheadTimes > ExtremeLimit:
        print(fxsuggestion)

    if Limit <= eyeTimes < ExtremeLimit:
        print(esuggestion)
    elif eyeTimes > ExtremeLimit:
        print(exsuggestion)

    if Limit <= chestTimes < ExtremeLimit:
        print(csuggestion)
    elif chestTimes > ExtremeLimit:
        print(cxsuggestion)



def main():
    FindSuggestion()

if __name__ == "__main__":
    main()