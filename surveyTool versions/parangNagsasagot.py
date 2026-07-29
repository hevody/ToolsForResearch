#respondents = 60
#questions = 20

respondents = 5
questions = 20

answersPerRespondent = []
for respondent in range(respondents):
    print(f'Analyzing respondent #{respondent + 1}')
    answers = []
    for answer in range(questions):
        print(f'Question #{answer + 1}')
        answer = input()
        print()
        answer = int(answer)
        answers = answers + [answer]    
    answersPerRespondent = answersPerRespondent + [answers]

print(answersPerRespondent)


