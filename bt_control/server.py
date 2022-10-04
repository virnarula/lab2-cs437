import bluetooth
import threading
import time
# import picar_4wd as fc

# hostMACAddress = "E4:5F:01:3C:05:37" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
# port = 1
# backlog = 1
# size = 1024
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.bind((hostMACAddress, port))
# s.listen(backlog)
# print("listening on port ", port)
# try:
#     client, clientInfo = s.accept()
#     while 1:   
#         print("server recv from: ", clientInfo)
#         data = client.recv(size)
#         if data:
#             print(data)
#             client.send(data) # Echo back to client
# except: 
#     print("Closing socket")
#     client.close()
#     s.close()

client = None
msg_size = 1024

def send_telemetry():
    while True:
        data = "This is telemetry info"
        client.send(data)
        time.sleep(1)
    pass

def receive_controls():
    while True:
        data = client.recv(msg_size)
        if data:
            print(data)
            print(type(data))
    pass

if __name__ == "__main__":
    hostMACAddress = "E4:5F:01:3C:05:37" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
    port = 1
    backlog = 1
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    print("listening on port ", port)

    try:
        client_connection, clientInfo = s.accept()
        client = client_connection
        
        telementry = threading.Thread(target=send_telemetry)
        controls = threading.Thread(target=receive_controls)

        telementry.start()
        controls.start()

        telementry.join()
        controls.join()

    except:
        print("Closing socket")
        client.close()
        s.close()