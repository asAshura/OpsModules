'''
1. Domain to IP with socket
2. Domain to IP with dns.resolver
'''
##### install dnspython
# pip -install dnspython
# or
# git clone https://github.com/rthalley/dnspython.git
# cd dnspython
# python setup.py install
'''
1. Domain to IP with socket
'''
import sys, socket
DNStoIP = socket.getaddrinfo("jpuyy.com", 80, 0, 0, socket.SOL_TCP)
print(DNStoIP)

'''
2. Domain to IP with dns.resolver
'''
import dns.resolver

domain = input('Please input an domain: ')
# A记录
dns  = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        if isinstance(j, dns.rdtypes.IN.A.A):
            print('\t %s' % j.address)

        if isinstance(j, dns.rdtypes.ANY.CNAME.CNAME):
            print('CNAME: %s' % j)


domain = input('Please input an domain: ')
# 指定查询类型为MX记录
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print('MX preference=', i.preference, ' mail exchanger=', i.exchange)

#指定查询类型为NS记录
NS = dns.resolver.query(domain,'NS')
for i in NS.response.answer:
     for j in i.items:
         print(j)

 #指定查询类型为CNAME记录
CNAME = dns.resolver.query(domain,'CNAME')
for i in CNAME.response.answer:
    for j in i.items:
         print(j)

'''

'''


