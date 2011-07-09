# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from black_sholes import implied_volatility
from option import CallOption
from model import HestonModel

#Number of time steps
num_steps = 150
#Number of monte carlo paths
num_paths = 100
#Strike
K = np.arange(0.8, 2.0, 0.2)
#maturity
T = 5.0
#Initial stock price
s0 = 1.0
#Initial volatility
v0 = 0.1
#risk free rate
r = 0.05
#long term volatility(equiribrium level)
theta = 0.1
#Mean reversion speed of volatility
kappa = 1.1
#lambda(volatility of Volatility)
lamda = 0.4
#rho
rho = -0.6

#simulation
imp_vol = np.array([])
for k in K:
    call_option = CallOption(k, T)
    heston = HestonModel(num_steps, num_paths, s0, v0, r, theta, kappa, lamda, rho)
    price = heston.price(call_option)
    #calc implied volatility
    imp_vol = np.append(imp_vol, implied_volatility(price, s0, k, T, r, 'C'))

#plot result
plt.plot(K, imp_vol)
plt.xlabel('Strike (K)')
plt.ylabel('Implied volatility')
plt.title('Volatility skew by Heston model')
plt.show()