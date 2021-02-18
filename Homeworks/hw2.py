grades=[]
names=[]
averages=[]
for x in range(5):
    temporary=[]
    name=input('please enter your name and surname: ')
    midterm=int(input('please enter your midterm grade :'))
    final=int(input('please neter your final grade: '))
    homework=int(input('please enter your homework grade: '))
    temporary.insert(0,midterm)
    temporary.insert(1,final)
    temporary.insert(2,homework)
    grades.append(temporary)
    names.append(name)
dictin={names[i]:grades[i] for i in range(len(names))}
dic_ave=dictin.copy()
for i in range(len(grades)):
    add=0
    ave=0
    for t in(grades[i]):
        add+=t
    ave=add/3
    averages.append(ave)
    dic_ave={ave:names[i] for i in range(len(names))}
averages.sort()
averages.reverse()
print(dictin)
print(averages)
print('congratilation',dic_ave.get(averages[0]),'you are the one')




                
