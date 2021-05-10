def biggie_size(List):
    for i in range(0,len(List),1):
        if List[i]>0:
            List[i]="big"
    return List


print(biggie_size([-1, 3, 5, -5]))
