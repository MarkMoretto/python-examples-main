
"""
Summary: Convert IPv4 address to decimal value.

Date created: 2020-09-12

Contributor(s):
    Mark Moretto
    
Ref:
    https://mkyong.com/java/java-convert-ip-address-to-decimal-number/
"""


def ipv4_to_dec(ip_address: str):
    """Convert IP to decimal value."""
    BASE: int = 256
    
    tokens = list(map(int, ip_address.split(".")))[::-1]
    
    tkn_len = len(tokens)
    
    return sum([tokens[i] * BASE ** i for i in range(tkn_len)])


def dec_to_ip(dec):
    """Convert decimal number back to IPv4 format.
    
    This uses bit-shifting, which could also be used in conversion to a decimal value.
    """
    return f"{(dec >> 24) & 0xFF}.{(dec >> 16) & 0xFF}.{(dec >> 8) & 0xFF}.{dec & 0xFF}"
    
    
if __name__ == "":
    # Some simple assertions of differences between IP addresses
    assert ((ipv4_to_dec("10.0.0.50") - ipv4_to_dec("10.0.0.0")) == 50), "Error: Test 1"
    assert ((ipv4_to_dec("10.0.1.0") - ipv4_to_dec("10.0.0.0")) == 256), "Error: Test 2"
    assert ((ipv4_to_dec("20.0.1.0") - ipv4_to_dec("20.0.0.10")) == 246), "Error: Test 3"
