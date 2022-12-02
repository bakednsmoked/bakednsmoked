"""Websocket module"""

import asyncio
from websockets import server

HOST = "localhost"
PORT = 8090

async def respond(websocket):
    """Write to websocket"""
    await websocket.send("Hello")

async def listen():
    """Listen on websocket"""
    async with server.serve(respond, host=HOST, port=PORT):
        await asyncio.Future()

def start_ws():
    """Start websocket server"""
    return asyncio.run(listen())
