def isIPv4Address(inputString):
# split the string by its dots
# each element mus be between 0 and 255

# Tests
# inputString: "1.1.1.1a" false         (minha respsota True)
# inputString: "172.316.254.1" false    (minha resposta True)
# inputString: "0..1.0" false           (minha resposta True)
    
    ip4_numbers = inputString.split(".")

    ip4v = True
    if len(ip4_numbers) != 4:
        ip4v = False
    
    try:
        for n in ip4_numbers:
            if int(n) >= 0 and int(n) <= 255:
                ip4v = True
            else:
                ip4v = False
    except ValueError:
        ip4v = False
    return ip4v

# Opção 2
def isIPv4Address(inputString):
# split the string by its dots
# each element mus be between 0 and 255
    
    ip4_numbers = inputString.split(".")
    isIpv4 = True
    
    if len(ip4_numbers) != 4:
        isIpv4 = False
    for n in ip4_numbers:
        if not n.isdecimal():
            isIpv4 = False
        elif int(n) >= 0 and int(n) <= 255:
            isIpv4 = True
        else:
            isIpv4 = False
    return isIpv4