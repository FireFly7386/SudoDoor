import listener
import payloadgen
import portscan

from colors import Colors
import os


running = True

while running:
    try:

        cmd = input(Colors.RESET + "(" + Colors.RED + "SudoDoor" + Colors.RESET + ") ")

        if cmd == "help":
            print("""
    List of commands:
    listen <port> --- starts a listener on given port
    payload <ip> <port> <language> --- generate payload
    payload show --- show payloads
    scan <ip> <threads> --- scans the open ports from the ip with n threads
    """)

        elif cmd.startswith("listen"):
            portNum = None
            port = cmd[7:]
            try:
                portNum = int(port)
            except:
                print("Usage: listen <port>")
                continue

            listener.listen("0.0.0.0", portNum)

        elif cmd.startswith("payload"):
            try:
                args = cmd.split(" ")
                if args[1] == "show":
                    payloadgen.showPayloads()
                else:
                    print(payloadgen.generate_payload(args[1], args[2], args[3]))
            except:
                print("Usage: payload <ip> <port> <language> or payload show")
                continue
        
        elif cmd.startswith("scan"):
            #try:
                args = cmd.split(" ")
                if args.__len__() == 3:
                    portscan.scan_host(args[1], 1, 65535, int(args[2]), False)

                elif args.__len__() == 4:
                    portscan.scan_host(args[1], 1, 65535, int(args[2]), bool(args[3]))


                else:
                    portscan.scan_host(args[1], 1, 65535, 10000, False)

            #except:
               # print("Usage: scan <host> <threads>")
                #continue

    except KeyboardInterrupt:
        print(Colors.BLUE + "\n[+] " + Colors.RESET + "Shutting down SudoDoor...")
        running = False
