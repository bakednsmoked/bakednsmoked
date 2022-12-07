let HOST: string | undefined;
let sock: WebSocket;

export async function start_socket() {
  if (process.env.NODE_ENV === "production") {
    HOST = "ws://localhost:8030/websock";
  } else {
    HOST = "ws://localhost:21134/";
  }

  sock = new WebSocket(HOST);
  sock.onopen = () => {
    console.log("Socket opened");
    sock.send("Hello from client");
  };

  sock.onmessage = (msg: MessageEvent) => console.log(msg.data);
  sock.onerror = (err: Event) => console.error(`WebSocket problem: ${err}`);
  sock.onclose = () => console.log("Socket closed");
}
