lowNum=2
highNum=9
mul=3


for i in range(lowNum,highNum+1,1):
    if mul>=lowNum and mul<=highNum:
        if i%mul==0:
            print(i)