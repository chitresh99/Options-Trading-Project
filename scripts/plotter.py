import matplotlib.pyplot as plt

plt.ion()

def visualise_chart(x_vals, y_vals):
    plt.clf()  
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b', label="Straddle Payoff")
    
    plt.xlabel("Stock Price")
    plt.ylabel("Straddle Payoff")
    plt.title("Live Straddle Payoff Chart")
    plt.legend()
    plt.grid(True)
    
    plt.pause(0.1) 
