import socket
from colors import Colors
from threading import Thread, Event
import math

def scan_ports(ip, start_port, end_port, verbose, stop_event):
    for port in range(start_port, end_port):
        if stop_event.is_set():
            break
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = socket.getservbyport(port)
                print(f'Port {port} is open and running {service}')

            else:
                if verbose == True:
                    print(f'Port {port} is closed')

            sock.close()
        except Exception as e:
            pass

def scan_host(ip, start_port, end_port, num_threads, verbose):
    total_ports = end_port - start_port
    chunk_size = math.ceil(total_ports / num_threads)

    threads = []
    stop_event = Event()
    for i in range(0, total_ports, chunk_size):
        start = start_port + i
        end = min(start_port + i + chunk_size, end_port)
        t = Thread(target=scan_ports, args=(ip, start, end, verbose, stop_event))
        t.start()
        threads.append(t)

    while True:
        user_input = input('Press "q" to stop scanning: ')
        if user_input == 'q':
            stop_event.set()
            break

    for t in threads:
        t.join()

#ip = input("Enter the IP address or hostname to scan: ")
#start_port = int(input("Enter the starting port to scan: "))
#end_port = int(input("Enter the ending port to scan: "))
#num_threads = int(input("Enter the number of threads to use: "))
#scan_host(ip, start_port, end_port, num_threads, verbose=False)
