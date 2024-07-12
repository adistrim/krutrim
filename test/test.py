import asyncio
import websockets
import requests

async def websocket_client(session_id):
    uri = f"ws://localhost:8000/ws/{session_id}"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                user_message = input("User: ")
                
                if user_message.lower() == 'exit':
                    print("Closing connection...")
                    break
                
                await websocket.send(user_message)
                
                response = await websocket.recv()
                print(f"\n{response}\n")
    except websockets.exceptions.ConnectionClosedError as exc:
        print(f"Connection closed unexpectedly: {exc}")

def get_session_id():
    response = requests.get("http://localhost:8000/api/v1/generate_session_id/")
    response_data = response.json()
    return response_data.get("session_id")

def main():
    session_id = get_session_id()
    if session_id:
        print(f"Generated session ID: {session_id}")
        asyncio.run(websocket_client(session_id))
    else:
        print("Failed to fetch session ID.")

if __name__ == "__main__":
    main()
