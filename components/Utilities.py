import random
from numpy import random as np


def colorGenerator():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


def textColor(rgb):
    return [0, 0, 0] if (((rgb[0] * 299) + (rgb[1] * 587) + (rgb[2] * 114)) / 1000) > 123 else [255, 255, 255]


# function to find 1(None)*1 Pattern in the list
def find_IdlPattern(timeslots):
    for i in range(len(timeslots)):
        if timeslots[i] == [1]:
            if timeslots[i+1] == [1]:
                continue
            for j in range(i+1,len(timeslots)):
                if timeslots[j] == False:
                    break
                elif timeslots[j] == [1]:
                    yield timeslots[i:j+1]
                    break
    return []


# function to find 1(None)*1 Pattern in the list
def find_gapTimeSlot(timeslots):
    gapTimeSlot = 0
    for i in range(len(timeslots)):
        if timeslots[i] == [1]:
            if timeslots[i+1] == [1]:
                continue
            temp_gapTimeSlot = gapTimeSlot
            for j in range(i+1,len(timeslots)):
                if timeslots[j] == False :
                    gapTimeSlot = temp_gapTimeSlot
                    break
                elif timeslots[j] == [1]:
                    break
                elif timeslots[j] == None:
                  gapTimeSlot += 1

    return gapTimeSlot



if __name__ == '__main__':
    for i in range(3):
        settings = []
        settings.append(np.randint(50, 200))
        settings.append(np.randint(settings[0], 200))
        settings.append(np.randint(50, 150))
        settings.append(np.randint(1500, 4500))
        settings.append(round(np.random() / 5, 2))
        settings.append(np.randint(90, 100))
        settings.append(np.randint(0, 10))
        settings.append(np.randint(50, 75))
        print(settings)