import os



print('How many statements?')
#statements = input()
statements = 1
print('How many respondents?')
#respondents = input()
respondents = 7


for statementno in range(statements):
    statementno = statementno + 1
    print(f'Analyzing statement {statementno}...')
    ratings = []
    for respondentno in range(respondents):
        respondentno = respondentno + 1
        print(f'Analyzing respondent #{respondentno}')
        print(f'What is his/her rating for {statementno}?')
        rating = input()
        ratings = ratings + [rating]
    ratings.sort()
    print(ratings)
    addRating = 0
    for rating in ratings:
        rating = int(rating)
        addRating = addRating + rating
    print(addRating)
    average = addRating / respondents
    average = round(average, ndigits=2)
    print(f'The average is: {average}')
    counter = []
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for rating in ratings:
        #print(rating)
       
        if rating == '1':
            one = one + 1
        if rating == '2':
            two = two + 1
        if rating == '3':
            three = three + 1
        if rating == '4':
            four = four + 1
        if rating == '5':
            five = five + 1

    #print(one)
    counter = [one, two, three, four, five]
    counter.sort()

    singler = []

    for counte in counter:
        if counte in singler:
            continue
        singler = singler + [counte]

    dictCounter = {'one':one, 'two':two, 'three':three, 'four':four, 'five':five}
    
    singler.sort(reverse=True)
    ranks = len(singler)

    rank = 0
    for single in singler:
        rank = rank + 1
        print(f'This is rank {rank}')
        for kay in dictCounter.keys():
            #print(kay)
            #print(dictCounter[kay])
            #print(single)
            #input()

            if dictCounter[kay] == single:
                print(kay)
                    

    print(singler)



    #dictCounter = {'one':one, 'two':two, 'three':three, 'four':four, 'five':five}
    counter.sort()

    

'''
    print(f'one = {one}')
    print(f'two = {two}')
    print(f'three = {three}')
    print(f'four = {four}')
    print(f'five = {five}')
'''
#print(counter)
    



'''
for statementno in range(15):
    statementno = statementno + 1
    strStatementno = str(statementno)
    print(f'Analyzing statement {statementno}...')
    '''