import time 
def rand(low , hi, size):
    retList = []
    numLoop = 0
    
    while True:
        final = []
        final_str = ''

        for  i in range(10):
            first = str(time.time_ns())
            time.sleep(0.000001)
            second = str(time.time_ns())
            num = 0
            final_str += str (int(second) - int(first))
        fIndex = 0
        sIndex = len(str(hi))
        while True:
            num = 1
            for i in final_str[fIndex:sIndex]:
                if i == "0":
                    num *= 2
                    continue
                if numLoop % 2 == 0:
                    num *= int(i)
                else:
                    num /= int(i)
            final.append(num)
            #fIndex += 1
            sIndex += 1
            if sIndex > len(final_str):
                break
        for i in reversed(range(low,hi)):
            if i in final:
                retList.append(i)
                if len(retList) == size:
                    return retList
        numLoop += 1
print(rand(10,100,20))