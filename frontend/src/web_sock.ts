const HOST = "ws://localhost:21134";

export async function start_socket_server() {
    let sock = new WebSocket(HOST)

    sock.onopen = () => sock.send("Hello");
    sock.onmessage = (msg) => console.log(msg.data);
    sock.onerror = (err) => console.error(err);
    sock.onclose = () => alert("Socket closed");
}