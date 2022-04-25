from __future__ import division
import unittest
import numpy as np
import scipy.stats as ss

def black_scholes(S0, K, r, sigma, T, option_type):
    '''
    Gives the Black Scholes option prices for vanilla European calls and puts
    Args:
        S0: stock spot price at t = 0
        K: option strike price
        r: risk free rate
        q: continuous dividend rate
        sigma: constant stock volatility
        T: option time to expiry
        option_type: string 'call' or 'put'
    Return:
        value: price of the vanilla European option
    '''
    d1 = (np.log(S0 / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    F = S0 * np.exp((r) * T)
    if option_type == 'call':
        value = np.exp(-r * T) * (F * ss.norm.cdf(d1) - K * ss.norm.cdf(d2))
    elif option_type == 'put':
        value = np.exp(-r * T) * (-F * ss.norm.cdf(-d1) + K * ss.norm.cdf(-d2))
    else:
        raise ValueError('option_type input is bad; input either "call" or "put"')
    return value



if __name__ == '__main__':
    print(black_scholes(100,110,0.05,0.2,1,'call'))
