import time 

i = 0






while True:
    i+=1

    print(i)
    time.sleep(0.5)
    
    if i == 10:
        raise Exception("reached 10")