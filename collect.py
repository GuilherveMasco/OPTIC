import requests, json

#IPv4 data
file_ipv4 = open('ipv4_oc.csv', 'w')

url = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

api_token = "<YOUR API TOKEN HERE>"

headers = {
    "apiKey": api_token,
    "startIndex": str(0),
    "keyword": "ipv4"
}

headers_id = {
    "apiKey": api_token
}

response = requests.get(url, params=headers)
    
response_json = response.json()

qnt = int(response_json["totalResults"])
repeater = int(qnt/20)

print("IPv4 results:")

for i in range(repeater + 1):
    headers["startIndex"] = (i*20)
    
    response = requests.get(url, params=headers)
    response_json = response.json()
    size = int(response_json["resultsPerPage"])
    for j in range(size):
        item = response_json["result"]["CVE_Items"][j]["cve"]["CVE_data_meta"]["ID"]
        print("Index " + str(i*20 + j + 1) + ": " + item)
        file_ipv4.write(item)
        file_ipv4.write('\n')

        url_id = "https://services.nvd.nist.gov/rest/json/cve/1.0/" + item
        response_id = requests.get(url_id, params=headers_id)
        response_json_id = response_id.json()
        response_string_id = json.dumps(response_json_id)
        output = './output-ipv4/' + item + '.json'

        with open(output, 'w') as outfile:
            outfile.write(response_string_id)

file_ipv4.close()

print('\n')

#IPv6 data
file_ipv6 = open('ipv6_oc.csv', 'w')

url = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

headers["keyword"] = "ipv6"

response = requests.get(url, params=headers)
    
response_json = response.json()

qnt = int(response_json["totalResults"])
repeater = int(qnt/20)

print("IPv6 results:")

for i in range(repeater + 1):
    headers["startIndex"] = (i*20)
    
    response = requests.get(url, params=headers)
    response_json = response.json()
    size = int(response_json["resultsPerPage"])
    for j in range(size):
        item = response_json["result"]["CVE_Items"][j]["cve"]["CVE_data_meta"]["ID"]
        print("Index " + str(i*20 + j + 1) + ": " + item)
        file_ipv6.write(item)
        file_ipv6.write('\n')

        url_id = "https://services.nvd.nist.gov/rest/json/cve/1.0/" + item
        response_id = requests.get(url_id, params=headers_id)
        response_id = requests.get(url, params=headers_id)
        response_json_id = response_id.json()
        response_string_id = json.dumps(response_json_id)
        output = './output-ipv6/' + item + '.json'

        with open(output, 'w') as outfile:
            outfile.write(response_string_id)

file_ipv6.close()