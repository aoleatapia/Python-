import random as rnd

my_qa = [
    ('the start of the Revolutionary War ', 1775),
    ('the United States Constitution signed ', 1783),
    ('President Lincoln assassinated ', 1865),
    ('Theodore Roosevelt\'s first day in office as President of the United States ', 1901),
    ('the beginning of World War II ', 1939),
    ('the first personal computer introduced ', 1975),
    ('the Berlin Wall taken down ', 1989),

    ('the atomic bombing of Hiroshima and Nagasaki ', 1945),
    ('the sinking of the Lusitania ', 1915),
    ('the Stock Market Crash ', 1929)
]

rnd.shuffle(my_qa)

points = 0
for qa in my_qa:
        question = input('What year was ' + qa[0] + '?')
        try:
            user_ans = int(question)
        except:
            exit('your score was: ' + str(points))

        check = abs(user_ans - qa[1])
        print(check)
        if check == 0:
            print('spot on! you got 10 points')
            points+= 10
        elif check <= 5 and not check == 0:
            print('so close! just by a few years')
            print('you got 5 points')
            points+= 5
        elif check <= 10 and not check == 0:
            print('ooohhh almost there but not quite')
            print('you got 2 points')
            points+= 2
        elif check <= 20 and not check == 0:
            print('mmmmmm so close yet so far')
            print('you got 1 points')
            points+= 1
        else:
            print('you not even close brah')
            print('you get 0 point')
        

print('you finished the quiz: ' + points)