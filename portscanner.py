# The socket Lib basically allows us establish
# A connection over the internet
import socket
# Install IPy using pip3 install IPy
# Use apt install python3-pip to install pip3
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '^_^ Scanning Target ^_^ ' + str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(sock):
    # The socket.recv function receives data from an open port
    # s.recv(1024) is the amount of data we receive from the port in
    # bytes as we don't need more in order to get and print the banner
    return sock.recv(1024)


# We Try to connect to the target using socket in a try and except rule
# Read more on socket to understand the Lib
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        # We set timeout because it takes longer to connect to certain
        # Ports than other ports
        # Note: the lower the timeout the lower the accuracy
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is Open')
    except:
        pass


if __name__ == "__main__":
    targets = input('[+] Enter Target/s IP/Domain To Scan(Split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
