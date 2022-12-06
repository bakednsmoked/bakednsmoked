const HOST = "ws://socket";

export async function start_socket_server() {
    let sock = new WebSocket(HOST)

    sock.onopen = () => sock.send("Hello");
    sock.onmessage = (msg) => console.log(msg.data);
    sock.onerror = (err) => console.error(err);
    sock.onclose = () => console.log("Socket closed");
}