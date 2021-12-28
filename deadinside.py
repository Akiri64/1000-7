import time 
b = 1000
i = 1007
while i > 1:
    b-= 7
    i-= 7
    time.sleep(0.08)
    print(str(i) + "-7=" +str(b))