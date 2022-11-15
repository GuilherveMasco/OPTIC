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

## Usage
All the tool modules can be executed alone, but the recommended order to execute is the one in the `Modules` section of this document: collect, get_unique, compare, compare_unique, extractor.

To use the collect module, first you need an API token from NVD, this token can be obtained in the NVD website. The NVD token has to be manually inserted into the collect module, changing the value `<YOUR API TOKEN HERE>` with yout obtained token.

All the results can be found in the generated CSV files and in the `output_ipv4` and `output_ipv6` folders.

### Vulnerabilities occurrences
All the CVE occurrences found on NVD, for IPv4 and IPv6 can be found on the `ipv4_oc.csv` and `ipv6_oc.csv` files, after the execution of the `collect` module. The files `ipv4_unique_oc.csv` and `ipv6_unique_oc.csv` storage the CVE found for IPv4 and IPv6 exclusively (vulnerabilities cataloged only on one of the two versions, but never in both), after the execution of the `get_unique` module.

### Scores and data
After running the `compare` module, the files `ipv4_data.csv` and `ipv6_data.csv` and the similar files, `ipv4_unique_data.csv` and `ipv6_unique_data.csv` will be generated to unique vulnerabilities, after running the `compare_unique` module. This files contain scores from each vulnerability found and are divided by the columns:

- CVE: the CVE ID from the collected vulnerability
- Severity_score: each vulnerability base (severity) score
- Exploitability_score: each vulnerability exploitability score
- Impact_score: each vulnerability impact score
- Access_complexity: each vulnerability access complexity score (from LOW to HIGH)
- Severity: each vulnerability severity level (from LOW to HIGH)

Every collected data can be used, and the code changed to obtain more data, for scientific study and comparison of IP versions cataloged vulnerabilities.
