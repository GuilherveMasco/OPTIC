import os, json

#IPv4 output data
path_to_json = 'output-ipv4/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

cont = 0
avg_sev_ipv4 = 0
avg_exp_ipv4 = 0
avg_imp_ipv4 = 0

for item in json_files:
    item_name = 'output-ipv4/' + item
    file = open(item_name, 'r')
    values = json.load(file)
    
    #average severity score for IPv4
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
    avg_sev_ipv4 += uiReq

    #average exploitability score for IPv4
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["exploitabilityScore"]
    avg_exp_ipv4 += uiReq

    #average impact score for IPv4
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["impactScore"]
    avg_imp_ipv4 += uiReq

    cont += 1

#average values for severity, exploitability and impact scores (IPv4)
avg_sev_ipv4 = avg_sev_ipv4/cont
avg_exp_ipv4 = avg_exp_ipv4/cont
avg_imp_ipv4 = avg_imp_ipv4/cont


#IPv6 output data
path_to_json = 'output-ipv6/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

cont = 0
avg_sev_ipv6 = 0
avg_exp_ipv6 = 0
avg_imp_ipv6 = 0

for item in json_files:
    item_name = 'output-ipv6/' + item
    file = open(item_name, 'r')
    values = json.load(file)
    
    #average severity score for IPv6
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
    avg_sev_ipv6 += uiReq

    #average exploitability score for IPv6
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["exploitabilityScore"]
    avg_exp_ipv6 += uiReq

    #average impact score for IPv6
    uiReq = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["impactScore"]
    avg_imp_ipv6 += uiReq

    cont += 1

#average values for severity, exploitability and impact scores (IPv6)
avg_sev_ipv6 = avg_sev_ipv6/cont
avg_exp_ipv6 = avg_exp_ipv6/cont
avg_imp_ipv6 = avg_imp_ipv6/cont

#print data for average scores
print('Average scores for IPv4 and IPv6:')
print('\n')
print(f'Average IPv4 severity score:\t\t {avg_sev_ipv4}')
print(f'Average IPv6 severity score:\t\t {avg_sev_ipv6}')
print('\n')
print(f'Average IPv4 exploitability score:\t {avg_exp_ipv4}')
print(f'Average IPv6 exploitability score:\t {avg_exp_ipv6}')
print('\n')
print(f'Average IPv4 impact score:\t\t {avg_imp_ipv4}')
print(f'Average IPv6 impact score:\t\t {avg_imp_ipv6}')