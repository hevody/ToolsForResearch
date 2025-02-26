import os
import time


print('*'*75)
print()
print("WELCOME TO HEVODY'S STATISTICAL ANALYZER!".center(70))
print('"let me take you to a shortcut"'.center(70))
print()
print('*'*75)
print('\n\n')




while True:
    print('How many respondents?')
    respondents = input()
    try:
        respondents = int(respondents)
        break
    except ValueError:
        print('NUMBERS ONLY!\n')

#respondents = 7
os.system('cls')

responseRaw = []
for respondentno in range(respondents):
    respondentno = respondentno + 1
    print(f'\nAnalyzing respondent #{respondentno}...')
    while True:
        print('What is the rating?')
        rating = input()
        try:
            rating = int(rating)
            if rating > 6:
                print('UP TO FIVE ONLY!\n')
                continue
            break
        except ValueError:
            print('NUMBERS ONLY!\n')
            continue
    responseRaw = responseRaw + [rating]

os.system('cls')

#print(responseRaw)

one = 0
two = 0
three = 0
four = 0
five = 0


for responseRa in responseRaw:
    if responseRa == 5:
        five = five + 1
    if responseRa == 4:
        four = four + 1
    if responseRa == 3:
        three = three + 1
    if responseRa == 2:
        two = two + 1
    if responseRa == 1:
        one = one + 1

response = [five, four, three, two, one]

#print(response)

percent = []
for respons in response:
    percenter = (respons / respondents) * 100
    percenter = round(percenter, ndigits=1)
    percent = percent + [percenter]

#print(percent)
'''
tieAvoider = []
for respon in response:
    if respon in tieAvoider:
        continue
    tieAvoider = tieAvoider + [respon]

dictResponse = {'five':five, 'four':four, 'three':three, 'two':two, 'one':one}

tieAvoider.sort(reverse=True)

ranks = len(tieAvoider)

ranky = []
rank = 0
for tieAvoid in tieAvoider:
    rank = rank + 1
    for kay in dictResponse.keys():
        if dictResponse[kay] == tieAvoid:
            ranky = ranky + [rank]
'''


#print(tieAvoider)














greater = []
for respon in response:
    if respon in greater:
        continue
    greater = greater + [respon]

greater.sort(reverse=True)

rank = 0
for greate in greater:
    rank = rank + 1
    for indexer in range(5):
        if response[indexer] == greate:
            if indexer == 0:
                fiveRank = rank
            if indexer == 1:
                fourRank = rank
            if indexer == 2:
                threeRank = rank
            if indexer == 3:
                twoRank = rank
            if indexer == 4:
                oneRank = rank

ranky = [fiveRank, fourRank, threeRank, twoRank, oneRank]
#print(ranky)



average = ((5 * response[0]) + (4 * response[1]) + (3 * response[2]) + (2 * response[3]) + (1 * response[4])) / respondents
average = round(average, ndigits=1)



# to show in the end of the analysis

print('Statement: [insert]'.ljust(20) + 'Response'.ljust(15) + '%'.ljust(7) + 'Rank')

statement = ['5', '4', '3', '2', '1']

for indexator in range(5):
    print(statement[indexator].ljust(20) + str(response[indexator]).ljust(15) + str(percent[indexator]).ljust(7) + str(ranky[indexator]))

print(f'\nMean(average): {average}')
input()