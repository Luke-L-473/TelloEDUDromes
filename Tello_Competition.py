# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nLucas Luscomb & Luke Lenzinger")
print("Program Name: ")
print("Date: ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 8)
        sendmsg('takeoff')

        # Commit Message First Hoop - Stable
        sendmsg('forward 215', 4)
        # Commit Message Second hoop - Stable
        sendmsg('go 235 0 70 100', 4)

        # Commit Message: Third Hoop - Stable
        sendmsg('curve 155 155 0 0 290 0 60', 4)
        sendmsg('curve -155 -155 0 0 -290 0 60', 4)
        # Commit Message: Final Hoop - Stable
        sendmsg('go -230xx 0 -70 100', 4)

        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program

        sendmsg('land', 4)

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
