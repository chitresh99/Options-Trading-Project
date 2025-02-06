import asyncio
import json
import websockets
import os
from dotenv import load_dotenv


load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")


async def fetch_realtime_stock_price(symbol):
    url = f"wss://ws.finnhub.io?token={FINNHUB_API_KEY}"

    try:
        async with websockets.connect(url) as ws:
            
            await ws.send(json.dumps({"type": "subscribe", "symbol": symbol}))
            print(f"Subscribed to {symbol}")

            while True:
                response = await ws.recv() 
                data = json.loads(response)

                if "data" in data:
                    for stock in data["data"]:
                        if stock["s"] == symbol:
                            yield stock["p"]  
                await asyncio.sleep(1) 
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed: {e}")
    except Exception as e:
        print(f"Error in WebSocket connection: {e}")

if __name__ == "__main__":
    async def test():
        async for price in fetch_realtime_stock_price("AAPL"):
            print(f"Live Price: ${price:.2f}")

    asyncio.run(test())
