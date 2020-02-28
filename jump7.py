for i in range(1,101):
    if i%7!=0:
        stri=str(i)
        for x in stri:
            if x!='7':
                iprint=True
            else:
                iprint=False
                break
        if iprint==True:
            print('{}\r'.format(i))
