import os, json, csv

#IPv4 output data
path_to_json = 'output-ipv4/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

cont = 0
avg_sev_ipv4 = 0
avg_exp_ipv4 = 0
avg_imp_ipv4 = 0

with open('ipv4_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['CVE', 'Severity_score', 'Exploitability_score', 'Impact_score', 'Access_complexity', 'Severity'])

    for item in json_files:
        item_name = 'output-ipv4/' + item
        file = open(item_name, 'r')
        values = json.load(file)
        
        #average severity score for IPv4
        sev_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
        avg_sev_ipv4 += sev_score
    
        #average exploitability score for IPv4
        ex_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["exploitabilityScore"]
        avg_exp_ipv4 += ex_score
    
        #average impact score for IPv4
        imp_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["impactScore"]
        avg_imp_ipv4 += imp_score

        acc_comp = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["accessComplexity"]

        severity = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["severity"]
    
        cont += 1

        writer.writerow([item.strip('.json'), sev_score, ex_score, imp_score, acc_comp, severity])
    
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

with open('ipv6_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['CVE', 'Severity_score', 'Exploitability_score', 'Impact_score', 'Access_complexity', 'Severity'])

    for item in json_files:
        item_name = 'output-ipv6/' + item
        file = open(item_name, 'r')
        values = json.load(file)
        
        #average severity score for IPv6
        sev_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
        avg_sev_ipv6 += sev_score
    
        #average exploitability score for IPv6
        ex_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["exploitabilityScore"]
        avg_exp_ipv6 += ex_score
    
        #average impact score for IPv6
        imp_score = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["impactScore"]
        avg_imp_ipv6 += imp_score

        #access complexity
        acc_comp = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["cvssV2"]["accessComplexity"]

        severity = values["result"]["CVE_Items"][0]["impact"]["baseMetricV2"]["severity"]

        cont += 1

        writer.writerow([item.strip('.json'), sev_score, ex_score, imp_score, acc_comp, severity])

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