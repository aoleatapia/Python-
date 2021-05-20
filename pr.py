import random as rnd

my_preguntas = [
 ('The Berlin Wall taken down ', 1989),
 ('Theodore Roosevelt\'s first day in office as President ', 1901),
 ('President Lincoln assassinated ', 1865),
 ('The United States Constitution signed ', 1783),
 ('The first personal computer introduced ', 1975),
 ('The beginning of World War II ', 1939),
 ('The start of the Revolutionary War ', 1775),
 ('The Russian Revolution', 1917),
 ('El Grito de Dolores ', 1825),
 ('The Battle of Puebla', 1862),
 
]

rnd.shuffle(my_preguntas)

points = 0,
for pr in my_preguntas:
        question = input('What year was ' + pr[0] + '?')
        try:
            user_ans = int(question)
        except:
            print('your score is: ' + str(points))
                 

        check = abs(user_ans - pr[1])
        print(check)
        if check == points:
            print('Fantastic Job! Keep a Streak going! :)')
            points+= 10
        elif check <= 5 and not check == str:
            print('Sorry buddy, nice try, off by a couple years. :(')
            print('5 points is your reward');
            
            
            points+= 5 
        elif check <= 10 and not check == 0:
            print('Well it aint the right answer, try again.:(')
            print('2 points is your reward')
            points+= 2
        elif check <= 20 and not check == 0:
            print('Getting Colder, you\'re killing me, please try again, and....think...please.:(')
            print('I mean 1 point, but between us 2, you should not even be getting a point. >:(')
            points+= 1
        else:
            print('I mean what can I say besides you\'re wrong, I mean come on, you are letting the team down!')

            print('You get Nothing.Why? You dont deserve it, Think it slowly and then answer once more.')
        

print('Congratulations, you have completed the quiz! This is how many points you earned. Thanks for Playing ' + points)














































































































