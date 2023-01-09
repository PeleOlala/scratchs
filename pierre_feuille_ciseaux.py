import random

def bat(joueur_1, joueur_2) :
    return (joueur_1,joueur_2) in ((2,1),(1,0),(0,2))

jue = {0:'Pierre', 1:'Feuille', 2:'Ciseaux'}

s = int(input())
random.seed(s)
point = 0
j = []
for i in range(5):
    j.append(int(input()))

for i in j:
    o = random.randint(0,2)
    if o==i:
        print(jue[o], 'annule' ,jue[i], ':', point)
    elif bat(o,i):
        point-=1
        print(jue[o], 'bat', jue[i], ':', point)
    else:
        point+=1
        print(jue[o], 'est battu par', jue[i], ':', point)
if point == 0:
    print('Nul')
elif point>0:
    print('Gagné')
else:
    print('Perdu')
