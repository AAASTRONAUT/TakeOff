import random

int(input('Guess the number of streaks of 6 heads or 6 tails formed in a row when a coin is tossed 100 times and this experiment is repeated 10000 times:'))
streakcount=0
fav=['H' , 'T']
for i in range(10000):
    outcomes=[]
    for j in range(100):
        outcomes.append(random.choice(fav))
    count =0
    for i in range (99):
        if outcomes[i] == outcomes[i+1]:
            count +=1
            if count == 5:
                streakcount += 1
        else:
            count = 0
            continue
print('Actual number of streaks formed:',streakcount)







