import asyncio
import websockets
import json
import MetaTrader5 as mt5
import numpy as np

connected_clients = set()
current_symbol = "EURUSD"
update_interval = 10  # 100ms update interval

def serialize_mt5_data(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

async def send_mt5_data():
    mt5.initialize()

    while True:
        if connected_clients:  # Only fetch data if there are connected clients
            timeframe = mt5.TIMEFRAME_H1
            num_bars = 500

            bars = mt5.copy_rates_from_pos(current_symbol, timeframe, 0, num_bars)

            data = {
                "symbol": current_symbol,
                "bars": [
                    {
                        "time": int(bar[0]),
                        "open": float(bar[1]),
                        "high": float(bar[2]),
                        "low": float(bar[3]),
                        "close": float(bar[4]),
                        "tick_volume": int(bar[5]),
                        "spread": int(bar[6]),
                        "real_volume": int(bar[7])
                    }
                    for bar in bars
                ]
            }

            websockets.broadcast(connected_clients, json.dumps(data, default=serialize_mt5_data))

        await asyncio.sleep(update_interval)

async def handle_client(websocket):
    global current_symbol
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            if "symbol" in data:
                current_symbol = data["symbol"]
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    await asyncio.gather(server.wait_closed(), send_mt5_data())

if __name__ == "__main__":
    asyncio.run(main())
