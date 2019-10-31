import matplotlib.pyplot as plt
'''
sport={
       "Archery": 39,
       "Badminton": 10,
       "Starcraft": 5}

fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)

plt.bar(sport.keys(),sport.values())
plt.ylabel("Medal")
plt.title("Olympic Medals")
plt.show()
'''
# ======================================
# ======================================
'''
fig2=plt.figure()
ax2=fig2.add_subplot(1,1,1)
stat={2013:500,
      2014:505}
plt.bar(stat.keys(),stat.values())
plt.axis([2012.5, 2014.5, 499, 506])
'''
# ======================================
# ======================================
'''
label=["Red","Green","Blue"]
x=[30,50,60]
explode=[0,0,0.3]

plt.pie(x,autopct="%1.1f%%", shadow=True, colors=label,labels=label,explode=explode)
'''

'''
import numpy as np
fig5=plt.figure()
ax5=fig5.add_subplot(1,1,1)

gaussian_num=np.random.randn(1000)
plt.hist(gaussian_num,bins=20)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
'''

# 산점도를 통해 인과관계를 확인할 수 없다.
fig6 = plt.figure()
ax6 = fig6.add_subplot(1, 1, 1)
friends = {
    41: 4.1,
    26: 3.3,
    90: 5.7,
    50: 4.2,
    18: 3.2,
    124: 6.4,
    5: 5.7}

plt.scatter(friends.keys(), friends.values())
plt.show()
