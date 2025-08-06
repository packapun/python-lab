# Hello world

def canDrive(history, currentTime):
    history.sort()
    print(history[-1][1])
    if currentTime >= (history[-1][1]+8):
        return True

    totalDriveTime = 0 
    didTakeBreak = False
    minBreakDuration = 8
    for i in range(len(history)):   
        event = history[i]
        totalDriveTime += event[1] - event[0]
        if i > 0:
            breakDuration = event[0] - history[i-1][1]
            print("Break duration {}".format(breakDuration))
            if breakDuration >= minBreakDuration:
                didTakeBreak = True
        if didTakeBreak:
            totalDriveTime = 0
        print(totalDriveTime, didTakeBreak)
    return totalDriveTime < 12


history = [[14,24],[2,6]]
history2 = [[2,8],[12,16], [20,22]]
history3 = [[0,4],[6,10], [12,16]]

print(canDrive(history, 24)) # Should return true
print()
print(canDrive(history2, 24)) # Should return false
print()
print(canDrive(history3, 24))