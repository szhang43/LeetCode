def findPoisionDuration(timeSeries, duration): 
    seconds = 0
    if duration == 0: 
        return 0
    for i in range(len(timeSeries)): 
        if (timeSeries[i] + duration - 1) in timeSeries:
            seconds += 1
            print(i)
        else: 
            seconds += duration 
    return seconds

# print(findPoisionDuration([1, 4], 2))
# print(findPoisionDuration([1, 2], 2))
print(findPoisionDuration([1, 2, 3, 4, 5], 5))
# print(findPoisionDuration([1,2,3,4,5,6,7,8,9], 1))
