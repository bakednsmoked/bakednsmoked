"""Websocket module"""

import asyncio
from websockets import server
from websockets.server import WebSocketServerProtocol
from websockets.exceptions import WebSocketException

HOST = "0.0.0.0"
PORT = 21134


async def handler(websocket: WebSocketServerProtocol):
    """Write to websocket"""

    err = None
    while err is None:
        print("Got connection on websocket")
        try:
            msg = await websocket.recv()

            print(f"Message from client: {msg}")
            await websocket.send("Hello")
        except WebSocketException as ws_err:
            print(ws_err)
            err = ws_err


async def listen():
    """Listen on websocket"""
    async with server.serve(handler, host=HOST, port=PORT):
        await asyncio.Future()


def start_ws():
    """Start websocket server"""
    return asyncio.run(listen())
