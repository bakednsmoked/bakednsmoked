const HOST = "ws://localhost:8090";

export default async function() {
    let sock = new WebSocket(HOST)

    sock.onopen = () => console.log("Socket opened success");
    sock.onmessage = (msg) => alert(msg.data);
    sock.onerror = (err) => console.error(err)
}