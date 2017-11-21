'''
1. get Windows local IP address - method 1
2. get Windows local IP address - method 2
3. get Linux local IP address
4. get Linux MAC address
5. IP address format check
6. Convert Interger to IP with socket
7. Convert Interger to IP without socket
8. Convert IP to Interger without socket
9. IP translation with IPy
'''


import socket
from IPy import IP


'''
get Windows local IP address - method 1
'''

localIP = socket.gethostbyname_ex(socket.gethostname())
for i in localIP:
    print("local ip:%s "%i)

'''
get Windows local IP address - method 2
'''

localName = socket.getfqdn(socket.gethostname())
localIP = socket.gethostbyname(localName)
print('local ip: %s:%s' %(localName,localIP) )

'''
get Linux local IP address
'''
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


#def get_ip_address(ifname):
#    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    print skt
#    print ifname[:15]
#    pktString = fcntl.ioctl(skt.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
#    print pktString
#    ipString  = socket.inet_ntoa(pktString[20:24])
#    return ipString

print get_ip_address('eth0')
print get_ip_address('lo')

'''
get Linux MAC address
'''
import uuid
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

'''
IP address format check
'''
ip_input = eval(input('Please input an IP:'))

def ipFormatChk(ip_input):
    pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    if re.match(pattern, ip_input):
        return True
    else:
        return False
# or 

ip_str=input('input IP: ')
ip_split = ip_str.split('.')

if (len(ip_split) == 4) and (int(ip_split[0]) != 0):
    for i, x in enumerate(ip_split):
        try:
            int_x = int(x)
            if int_x < 0 or int_x > 255:
                print('either it\'s negative or bigger than 255')
        except ValueError as e:
            print('error')
    print('it\'s an IP address')
else:
    print('IP needs 4 numbers and first one can\'t be 0')
    

'''
Convert Interger to IP with socket
'''
import struct
import socket

int_ip = eval(input('Please input an integer:'))
ip = socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))
ip_toint = socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])

print (ip)
print (ip_toint)

'''
Convert Interger to IP without socket
'''
#def Int_to_IP(num):
#    s = []s
#    for i in range(4):
#        t1=num % 256
#        s.append(str(t1))
#        num //= 256
#    return '.'.join(s[::-1])

ip_input = eval(input('Please input an integer:'))
IntIP = lambda x: '.'.join([str(x//(256**i)%256) for i in range(3,-1,-1)])
IntIP(ip_input)

'''
Convert IP to Interger without socket
'''
ip_input = eval(input('Please input an IP address:'))
IPInt = lambda x:sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])
IPInt(ip_input)

'''
ip translation with IPy
'''
ip_s = input('Please input an IP or net-range: ')
ips = IP(ip_s)

for x in ips:
    print(x)

# calculate ip numbers with len()
print(len(ips))
#input a net-range
if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))

# input an ip address
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
