import ipaddress

def validate_ip(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

print(validate_ip("192.168.1.1"))
print(validate_ip("999.999.1.1"))
