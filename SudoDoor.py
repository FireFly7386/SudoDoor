import listener
#import payloadgen
from colors import Colors


running = True

while running:
    cmd = input(Colors.RESET + "(" + Colors.RED + "SudoDoor" + Colors.RESET + ") ")
    if cmd == "listen":
        listener.listen("0.0.0.0", 9001)