import socket
from IPy import IP
from colorama import Fore, Style, Back

print(Back.LIGHTGREEN_EX + Fore.BLACK + """=====My simple port scanner=====""" + Style.RESET_ALL)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


ipAddress = input(Fore.YELLOW + '[+] Enter the target to scan: ' + Style.RESET_ALL)

def scan_port(IP, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipAddress,port))
        print( Fore.GREEN + f'[+] Port {port} of the target is open' + Style.RESET_ALL)
    except:
        print(Fore.RED + f'[-] Port {port} of the target is closed' + Style.RESET_ALL)

converted_ip = check_ip(ipAddress)

for i in range(60,90):
    scan_port(converted_ip, i)