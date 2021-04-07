import time
import matplotlib.pyplot as plt
import numpy as np
# start_time = time.time()
# time.sleep(2)
# timestamp = time.time() - start_time
# print(timestamp)
# time.sleep(3)
# print(time.time() - start_time)

zero_time = time.time()
start_time = time.time()
x = 0
for i in range(100):
    
    time.sleep(2)
    if(i%3==0):
        x+=1
    timestamp = time.time() - start_time
    if(timestamp > 5):
        plt.bar(np.arange(0,int(time.time()-zero_time)), height=x)
        plt.show(block=False)
        plt.pause(3)
        plt.close('all')
        start_time = time.time()
