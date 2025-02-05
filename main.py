import asyncio
from collections import deque
from scripts.data_fetcher import fetch_realtime_stock_price
from scripts.options_strategy import calculate_straddle_payoff
from scripts.plotter import visualise_chart

async def main():
    ticker = "AAPL"
    strike_price = 235  
    premium_long_call = 0.91
    premium_long_put = 8

    prices = deque(maxlen=50)   
    payoffs = deque(maxlen=50) 

    print(f"Stock price for : {ticker}...")

    async for live_price in fetch_realtime_stock_price(ticker):
        payoff = calculate_straddle_payoff(live_price, strike_price, premium_long_call, premium_long_put)

        prices.append(live_price)
        payoffs.append(payoff)

        print(f"Live Price: ${live_price:.2f}, Straddle Payoff: ${payoff:.2f}")

        visualise_chart(prices, payoffs) 

if __name__ == "__main__":
    asyncio.run(main())
