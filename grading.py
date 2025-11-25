
student_records = []
stats = {"test", 0}

def collector():
    i = 0
    while i < 3:
        print("Please enter your name...")
        input1 = input()
        print("Please enter your score...")
        input2 = input()
        
        student_records.append([input1, input2])
        i = i + 1

collector()

print(student_records)


def statistics():
    highest = 0
    highestUser = ""
    
    for score in student_records:
        if score[1] > highest:
            highest = score[1]
            highestUser = score[0]

    lowest = 0
    lowestUser = ""
    
    for score in student_records:
        if score[1] < lowest:
            lowest = score[1]
            lowestUser = score[0]

    
    average = 0
    
    for score in student_records:
        average = average + score
        
        
    average = average / len(student_records)
    
    stats.setdefault("highest Score", highest)
    stats.setdefault("lowest Score", lowest)
    stats.setdefault("average Score", average)


for keys,values in stats.items():
    print(keys)
    print(values)
