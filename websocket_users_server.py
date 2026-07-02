import asyncio
import websockets

async def handle_client(websocket):
    try:
        async for message in websocket:
            print(f"Получено сообщение от пользователя: {message}")
            for i in range(1, 6):
                response = f"{i} Сообщение пользователя: {message}"
                await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        pass

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
