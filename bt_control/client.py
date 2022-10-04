import threading
import bluetooth

# host = "E4:5F:01:3C:05:37" # The address of Raspberry PI Bluetooth adapter on the server.
# port = 1
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# sock.connect((host, port))
# while 1:
#     text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     sock.send(text)

#     data = sock.recv(1024)
#     print("from server: ", data)

# sock.close()

def send_controls():
    while True:
        result = input("\nEnter control")
        if (result in {"f", "b", "l", "r", "s"} ):
            sock.send(result)
        elif result == "quit":
            sock.send(result)   
            break 
        else:
            print("not a valid command!")
    

def receive_stats():
    while True:
        data = sock.recv(1024)
        print("\nfrom server: ", data)
        if not data:
            break


if __name__ == "__main__":
    host = "E4:5F:01:3C:05:37"  # The address of Raspberry PI Bluetooth adapter on the server.
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    
    client = threading.Thread(target=send_controls)
    server = threading.Thread(target=receive_stats)

    client.start()
    server.start()

    client.join()
    server.join()

    sock.close()