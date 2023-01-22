import listener
import payloadgen
from colors import Colors


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
    except KeyboardInterrupt:
        print(Colors.BLUE + "\n[+] " + Colors.RESET + "Shutting down SudoDoor...")
        running = False
