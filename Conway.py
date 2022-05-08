import copy , time

print("space enter is alive and enter is dead")
print("matrix backbone")
mainlist = []
column = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']
print(end='   ')
for j in column:
    print(j , end=' ')
print("\n")
for i in range(6):
    print( i+1 , ' -'*6 )
for i in range(6):
    row=[]
    for j in column:
        print("you want cell ",j,str(i+1), "live or dead?" , end =' ')
        t = input()
        if t == "":
            row.append(' ')
        else:
            row.append('#') 
    mainlist.append(row)
for i in range(6):
    print(mainlist[i] , '\n')

mainlist.append([' ',' ',' ',' ',' ',' '])
mainlist.insert(0,[' ',' ',' ',' ',' ',' '])
for i in range(8):
    mainlist[i].append(' ')
    mainlist[i].insert(0,' ')


def conway(sidelist):
    for i in range(1,7):
        for j in range(1,7):
            count=0
            spam = [sidelist[i-1][j-1] , sidelist[i-1][j] , sidelist[i-1][j+1] ,\
                    sidelist[i][j-1] ,                      sidelist[i][j+1] ,\
                    sidelist[i+1][j-1] , sidelist[i+1][j] , sidelist[i+1][j+1]]

            for t in spam:
                if t == '#':
                    count = count +1
                else:
                    continue 
            
            if count >= 3:
                if sidelist[i][j] ==' ':
                    sidelist[i][j] ='#'
            else:
                if sidelist[i][j] =='#':
                    sidelist[i][j] =' '
    for i in range(1,7):
        print(sidelist[i])
    print('\n')
    time.sleep(2)
    conway(sidelist)
    
try:
    conway(mainlist) 
except KeyboardInterrupt :
    print("you stopped the program")             

    
        

    

