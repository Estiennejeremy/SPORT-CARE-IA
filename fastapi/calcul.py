import statistics


def stateCalcul(allRmssd):
    maxRmssd = 0
    minRmssd = 0
    values = []
    for rmssd in allRmssd:
        if minRmssd == 0 & maxRmssd == 0:
            minRmssd = rmssd
            maxRmssd = rmssd
        if rmssd > maxRmssd:
            maxRmssd = rmssd
        if rmssd < minRmssd:
            minRmssd = rmssd
        
        if minRmssd != maxRmssd:
            result =  (minRmssd / maxRmssd) *100
            values.append(result)

    res = calcul(values)
    return res

def calcul(result):
    res = result[::-1] #reversing using list slicing
    last5 = result[0:5]
    print(last5)
    mean = statistics.mean(last5)
    print(mean)
    value = (mean/result[0]) *100
    return value
    
