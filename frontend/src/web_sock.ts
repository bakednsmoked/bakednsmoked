const HOST = "ws://localhost:8090";

export async function start_socket_server() {
    let sock = new WebSocket(HOST)

    sock.onopen = () => sock.send("Hello");
    sock.onmessage = (msg) => alert(msg.data);
    sock.onerror = (err) => console.error(err)

}