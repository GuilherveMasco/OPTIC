# OPTIC
Online Python Tool for Internet protocol Comparisons

## Introduction
The OPTIC tool is a Python 3 based multi-modules collector for IPv4 and IPv6 vulnerabilities informations.

OPTIC uses [NVD](https://nvd.nist.gov) as database to data collection. As a consequence, before running the tool is necessary to get an API access token from NVD and manually change the value `<YOUR API TOKEN HERE>` from the file `collect.py`

## Modules
OPTIC is divided in five different modules:
- collect.py
- get_unique.py
- compare.py
- compare_unique.py
- extractor.py

### Collect
The collect module, as the name suggests, is the module used to collect data from IPv4 and IPv6 vulnerabilities from NVD, using their CVE IDs.

This module generate different outuput files for IPv4 and IPv6 vulnerabilities data, it also download the entire JSON CVE from each vulnerability found.

### Get unique
The get_unique module was created to remove vulnerabilities cataloged from both IPv4 and IPv6 at the same time, creating files with the CVE of vulnerabilities exclusive for each IP version.

### Compare
The compare module get the score from each vulnerability from IPv4 and IPv6 and saves into differents output CSV files.

### Compare unique
The compare_unique module does the same proccess than the compare module, but with the exclusive vulnerabilities from IPv4 and IPv6.

### Extractor
The extractor uses [YAKE](https://github.com/LIAAD/yake) as keyword extractor to extract the 5 most relevants keyword from the CVE description of each vulnerability and saves a CSV with that info.
