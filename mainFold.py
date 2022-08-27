import csv
import numpy
import pandas as pd 

def checkStreak(rArray, roundNo, team, strkLength):
    rNo = roundNo-1 #correcting round number to round number in array 
    for i in range(1,strkLength+1):
        for j in range(0,len(rArray[rNo-i][1:])+1):
            if rArray[rNo-i][j][1]==team:
                if int(rArray[rNo-i][j][2]) <= int(rArray[rNo-i][j][3]):
                    return False
            elif rArray[rNo-i][j][4]==team:
                if int(rArray[rNo-i][j][2]) >= int(rArray[rNo-i][j][3]):                    
                    return False
    return True

#input raw data
winChance = 0
sample = 0
accumulate = 0
nOfBet = 0
mMin = 0
# for s in ["2010-2011","2011-2012","2012-2013","2013-2014","2014-2015","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020"]:
for s in ["2020-2021"]:
    results = []
    season = s
    with open("Bundesliga2_"+season+".csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)

    results = numpy.delete(results, (0), axis=1)

    #delete "Run" odds
    i=1
    while True:
        if results[i][8] == "Run":
            results = numpy.delete(results, i, axis=0)
        else:
            i += 1 
        if (i+1) > len(results[1:]):
            break

    #delete odds of the same match
    i=1
    while True:
        if results[i+1][1] == results[i][1]:
            results = numpy.delete(results, (i+1), axis=0)
        else:
            i += 1 
        if (i+1) > len(results[1:]):
            break

    #results = numpy.delete(results, 0, axis=1)

    #put round index into results array
    arrayOfRounds = []
    for i in range(1,35):
        resultsEachRound = []
        for j in range(2,len(results[1:])+1):
            if int(results[j][0]) == i:
                resultsEachRound.append(results[j])
        if resultsEachRound:
            arrayOfRounds.append(resultsEachRound)

    rER=arrayOfRounds

    streak = 3
    m = 0
    mplot3W = []
    for i in range(streak, len(rER[1::])+1):
        for j in range(0, len(rER[i][1:])):
            c1 = checkStreak(rER,i,rER[i-1][j][1],streak)
            c2 = checkStreak(rER,i,rER[i-1][j][4],streak)
            if c1:
                m = m-1
                if int(rER[i-1][j][2]) < int(rER[i-1][j][3]):
                    m = m + float(rER[i-1][j][7])
                mplot3W.append(round(m,2))
            if c2:
                m = m-1
                if int(rER[i-1][j][2]) > int(rER[i-1][j][3]):
                    m = m + float(rER[i-1][j][5])
                mplot3W.append(round(m,2))

    streak = 3
    m = 0
    mplot3WLate = [0,0]
    startRound = 1
    endRound = len(rER[1::])+1
#     endRound = 25
    mStop = 2
    stake = 1
    stakeMax = 1
    for i in range(startRound, endRound):
        for j in range(0, len(rER[i][1:])):
            c1 = checkStreak(rER,i,rER[i-1][j][1],streak)
            c2 = checkStreak(rER,i,rER[i-1][j][4],streak)
            if c1:
                m = m-stake
                if m < mMin:
                    mMin = m
                nOfBet = nOfBet+stake
                if int(rER[i-1][j][2]) < int(rER[i-1][j][3]):
                    m = m + float(rER[i-1][j][7])*stake
                mplot3WLate.append(round(m,2))            
            if c2:
                m = m-stake
                if m < mMin:
                    mMin = m              
                nOfBet = nOfBet+stake
                if int(rER[i-1][j][2]) > int(rER[i-1][j][3]):
                    m = m + float(rER[i-1][j][5])*stake
                mplot3WLate.append(round(m,2))               
#         if c1 or c2:
#             if m < mplot3WLate[-2]:
#                 stake = stake*2                                 
        if m > mStop:
            break
        if m < mplot3WLate[-2]:
            stake = stake*2
        if m > mplot3WLate[-2]:
            stake = 1
        if stake > stakeMax:
            stakeMax = stake
      
    print(season)
    print(startRound,endRound)
    print(mplot3W)
    print(mplot3WLate)
    accumulate = accumulate + m
    if (m > 0):
        winChance = winChance + 1
    if (m != 0):
        sample = sample + 1

print('-----',round(streak,0),'W Against----------------------------')
print('Return:',round(accumulate,2))
print('ROI:',round(accumulate/nOfBet,2))
print('Win rate:',round(winChance/sample,2))
print('Min:',mMin)
print('stakeMax:',stakeMax)
#dataframe = pd.DataFrame(results)
#dataframe.to_csv(r"foo.csv")

#NEXT: delete roms with "Run" > DONE
#NEXT: group matches of each round into separate arrays > DONE
#NEXT: write checkStreak3 > DONE


