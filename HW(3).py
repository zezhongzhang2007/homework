def haiku_string_parser(poem):
    poem_ = poem.split('/')
    for word in poem_:
        for e in word:
            if e ==',':
                continue
            else:
                print(e, end='')
        print('')


haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
haiku_string_parser(haiku_string)