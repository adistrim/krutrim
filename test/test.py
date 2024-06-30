import asyncio
import websockets
import requests

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

response = requests.get("http://localhost:8000/api/v1/generate_session_id/")
response_data = response.json()
session_id = response_data["session_id"]
print(f"Generated session ID: {session_id}")

asyncio.run(websocket_client(session_id))
