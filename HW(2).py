def is_haiku(poem):
    poem_ = poem.split('/')
    a = 0
    for word in poem_:
        y = 0
        word_ = word.split(',')
        for e in word_:
            y += 1
        if a == 0 and y ==5:
            a +=1
        elif a == 1 and y == 7:
            a += 1
        elif a == 2 and y == 5:
            print('True')
            a += 1
        elif a ==0 and y != 5:
            print('Warning:The first line is not 5 syllables long')
            print('False')
            break
        elif a ==1 and y != 7:
            print('Warning:The second line is not 7 syllables long')
            print('False')
            break
        elif a ==2 and y != 5:
            print('Warning:The third line is not 5 syllables long')
            print('False')
            break

is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon ")
is_haiku("clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ")