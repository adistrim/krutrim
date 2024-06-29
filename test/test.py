import asyncio
import websockets

async def websocket_client(session_id):
    uri = f"ws://localhost:8000/ws/{session_id}"
    async with websockets.connect(uri) as websocket:
        while True:
            user_message = input("Enter your message ('exit' to quit): ")
            await websocket.send(user_message)
            
            if user_message.lower() == 'exit':
                print("Closing connection...")
                break
            
            response = await websocket.recv()
            print(f"Response from server: {response}")

asyncio.run(websocket_client("your_session_id"))
