#IPv4 unique data
with open('ipv4_unique_oc.csv', 'w', newline='') as csvfile:
    flag = 0
    input_ipv4 = open('ipv4_oc.csv', 'r')
    for item_ipv4 in input_ipv4:
        input_ipv6 = open('ipv6_oc.csv', 'r')
        for item_ipv6 in input_ipv6:
            if ((item_ipv4.replace("\n", "")) == (item_ipv6.replace("\n", ""))):
                flag = 1
                break
        if (flag == 0):
            csvfile.write(item_ipv4)
        flag = 0

#IPv6 unique data
with open('ipv6_unique_oc.csv', 'w', newline='') as csvfile:
    flag = 0
    input_ipv6 = open('ipv6_oc.csv', 'r')
    for item_ipv6 in input_ipv6:
        input_ipv4 = open('ipv4_oc.csv', 'r')
        for item_ipv4 in input_ipv4:
            if ((item_ipv6.replace("\n", "")) == (item_ipv4.replace("\n", ""))):
                flag = 1
                break
        if (flag == 0):
            csvfile.write(item_ipv6)
        flag = 0