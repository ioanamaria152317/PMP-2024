#nr prim -> adaug bila neagra in urna 
#6 -> adaug bila rosie 
#altfel o bila albastra 

#apoi extrag o bila din urna 

#vreau sa aleg random un nr de la 1 la 6 

import random

def afla_prob(nr_simulari):

    prob=0
    bile_rosii_extrase=0
    
    for _ in range(nr_simulari):
        
        negre=2
        rosii=3
        albastre=4
        
        numar = random.randint(1,6)
    
        if numar ==2 or numar==3 or numar==5:
           negre+=1
        elif(numar==6):
           rosii+=1
        else:
           albastre+=1
        
        #  print(negre)
        #  print(rosii)
        #  print(albastre)
    
        bila_extrasa=random.choices(['negru','rosu','albastru'],weights=[negre,rosii,albastre])[0]
    
        if bila_extrasa=='rosu':
             bile_rosii_extrase+=1
    
    total_bile=negre+rosii+albastre
    prob=bile_rosii_extrase/nr_simulari
    return prob



print(afla_prob(10000))

#prob de a obtine o bila rosie 
#e fm prob totale -> am mai multe cazuri 
#
