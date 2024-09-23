import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
pollution_data=np.random.normal(100,60,1440)
import scipy.signal as ss
curr_fr=0.1
b,a=ss.butter(2,curr_fr,btype='low',fs=2)
smoothed_data=ss.filtfilt(b,a,pollution_data)
pollution=np.reshape(pollution_data,([24,60]))
average_values=np.mean(pollution,axis=1)
k=1
for i in average_values:
    print("average values for ",k ,"hour is :",i)
    k+=1
avg_exceed=[]
for i in average_values:
    if i>100:
        avg_exceed.append(i)
plt.plot(pollution_data,label="noisy_data")
plt.plot(smoothed_data,color="red",label="filtered_data")
plt.plot(avg_exceed,color="blue",marker='o',label="hazardous")
plt.title("Air quality fluctuations")
plt.xlim(0,200)
plt.ylim(0,200)
plt.legend()
plt.show()
plt.plot(avg_exceed,color="blue",marker='o',label="hazardous")
plt.show()

avg_conse=[]
k=1
for i in range(0,1440):
    if pollution_data[i]>=70:
        for j in range(i+1,i+10):
            if j<1440 and pollution_data[j]<0:
                k=0
                break;
        if k==1:
            avg_conse.extend((pollution_data[i],pollution_data[i+10]))


plt.plot(avg_conse,marker='o',linestyle='dashed')
plt.title("levels exceeded")
plt.show()

