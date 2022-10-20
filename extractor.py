import yake, csv, json

#IPv4 keywords
file_ipv4 = open('ipv4_unique_oc.csv', 'r')

with open('ipv4_keywords.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for item in file_ipv4:
        item_name = 'output-ipv4/' + item.replace("\n", "") + ".json"
        file = open(item_name, 'r')
        values = json.load(file)

        text = values["result"]["CVE_Items"][0]["cve"]["description"]["description_data"][0]["value"]

        kw_extractor = yake.KeywordExtractor(top = 5)
        keywords = kw_extractor.extract_keywords(text)

        index = 0
        kw_array = ["", "", "", "", ""]
        for kw in keywords:
            kw_array[index] = kw[0]
            index = index + 1

        writer.writerow([item.replace("\n", "").strip('.json'), kw_array[0], kw_array[1], kw_array[2], kw_array[3], kw_array[4]])

#IPv6 keywords
file_ipv6 = open('ipv6_unique_oc.csv', 'r')

with open('ipv6_keywords.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for item in file_ipv6:
        item_name = 'output-ipv6/' + item.replace("\n", "") + ".json"
        file = open(item_name, 'r')
        values = json.load(file)

        text = values["result"]["CVE_Items"][0]["cve"]["description"]["description_data"][0]["value"]

        kw_extractor = yake.KeywordExtractor(top = 5)
        keywords = kw_extractor.extract_keywords(text)

        index = 0
        kw_array = ["", "", "", "", ""]
        for kw in keywords:
            kw_array[index] = kw[0]
            index = index + 1

        writer.writerow([item.replace("\n", "").strip('.json'), kw_array[0], kw_array[1], kw_array[2], kw_array[3], kw_array[4]])
            