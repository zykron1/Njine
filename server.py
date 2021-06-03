import socket
import threading
PORT = 5050
SERVER = "10.0.0.103"
ADDR = (SERVER,PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONECT_MESAGE = "!LEAVE"
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def send(msg):
    mesage = msg.encode(FORMAT)
    msglen=len(mesage)
    sendlength = str(msglen).encode(FORMAT)
    sendlength +=b" "*(HEADER-len(sendlength))
    server.send(sendlength)
    server.send(mesage)
def handle_client(conn,addr):
    print(f"[USER CONECTIONS]{addr} conected")
    c=True
    while c:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONECT_MESAGE:
                break
            print(f"[{addr}] {msg}")
            send("hello")
      
    conn.close()
def start():
     server.listen()
     print(f"[LISTENING] Server is listining on {SERVER}")
     while True:
         conn, addr =  server.accept()
         thread = threading.Thread(target=handle_client, args=(conn, addr))
         thread.start()
         print(f"[THREAD INFO] Thread created total conections are now {threading.active_count()-1}")
print("[SYSTEM-BOOT]Server Is starting...")
start()
