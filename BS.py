# -*- coding: utf-8 -*-
from math import * 
from scipy.stats import norm
from scipy.optimize import fmin

# Black Sholes Function
def BlackSholes(S, K, T, r, v, callPutFlag = 'c'):
    d1 = (log(S / K) + (r + 0.5 * v**2) * T) / (v * sqrt(T))
    d2 = d1 - v * sqrt(T)
    if (callPutFlag == 'c') or (callPutFlag == 'C'):
        return S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    else:
        return K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
#Calc Implied volatility        
def ImpliedVolatility(price ,S, K, T, r, callPutFlag = 'c'):
    Objective = lambda x: (price - BlackSholes(S, K, T, r, x, callPutFlag))**2    
    return fmin(Objective, 0.01, disp = False)[0]
#test
if __name__ == '__main__':
    #correct : call 3.68
    print BlackSholes(49.0, 50.0, 1.0, 0.01, 0.2, 'C')
    #correct : put 4.18
    print BlackSholes(49.0, 50.0, 1.0, 0.01, 0.2, 'P')
    #correct : 0.2
    print ImpliedVolatility(3.68, 49.0, 50.0, 1.0, 0.01, 'C')
    #correct : 0.2
    print ImpliedVolatility(4.18, 49.0, 50.0, 1.0, 0.01, 'P')