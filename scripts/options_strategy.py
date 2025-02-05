import numpy as np

def calculate_straddle_payoff(sT,strike_price,premium_long_call, premium_long_put):
    payoff_long_call = np.maximum(sT - strike_price, 0) - premium_long_call
    payoff_long_put = np.maximum(strike_price - sT, 0) - premium_long_put
    return payoff_long_call + payoff_long_put