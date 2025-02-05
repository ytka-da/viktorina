score=0
print('Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!')

question1 = "Кто придумал эчпочмак?"
question2 = "Луковый суп — это блюдо какой кухни?"
question3 = "Где родина начос?"
question4 = "Как называются китайские пельмени?"
question5 = "В национальную кухню какой страны входят драники?"
question6=''

true_answer1 = "татары"
true_answer2 = "франция"
true_answer3 = "мексика"
true_answer4 = "гёдза"
true_answer5 = "беларусь"
true_answer6=''

answer1 = input(question1)
if answer1.lower()==true_answer1:
    score+=1
answer2 = input(question2)
if answer2.lower()==true_answer2:
    score+=1
answer3 = input(question3)
if answer3.lower()==true_answer3:
    score+=1
answer4 = input(question4)
if answer4.lower()==true_answer4:
    score+=1
answer5 = input(question5)
if answer5.lower()==true_answer5:
    score+=1
answer6 = input(question6)
if answer6.lower()==true_answer6:
    score+=1
print(score)
if score>=3:
    print(f'вы набрали {score} очков вы прошли игру')
else:
    print(f'вы набрали {score} очков этого не достаточно')