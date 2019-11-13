import urllib2
import base64
import json
import os
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='Script for downloading FASTA files from Enterobase.\nAuthor: Timo Schlueter <timo.schlueter@me.com>\nCreated: 2019-11-13', formatter_class=RawTextHelpFormatter)
requiredNamed = parser.add_argument_group('Required arguments')
requiredNamed.add_argument('-d', '--database', help='The database containing the assemblies (eg. clostridium)', required=True)
requiredNamed.add_argument('-t', '--token', help='Enterobase API-Token (see: https://enterobase.readthedocs.io/en/latest/api/api-getting-started.html)', required=True)
requiredNamed.add_argument('-l', '--list', help='The list of barcodes to dump', required=True)
args = parser.parse_args()

# API Token
# Getting started: https://enterobase.readthedocs.io/en/latest/api/api-getting-started.html
API_TOKEN = args.token

# Base endpoint
baseEndpoint = 'http://enterobase.warwick.ac.uk/api/v2.0/%s/assemblies?orderby=barcode&only_fields=download_fasta_link&barcode=%s&limit=1&offset=0&sortorder=asc'

def createAuthenticatedRequest(address):
    request = urllib2.Request(address)
    base64string = base64.encodestring('%s:%s' % (API_TOKEN,'')).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    return request

def getFastaLink(barcode):
    response = urllib2.urlopen(createAuthenticatedRequest(baseEndpoint % (args.database, barcode)))
    data = json.load(response)
    if data["Assemblies"]:
        if data["Assemblies"][0]["download_fasta_link"]:
            return (data["Assemblies"][0]["download_fasta_link"])
        else:
            print("failed.")
    else:
        print("failed.")
        
def writeFastaToDisk(barcode, link):
    response = urllib2.urlopen(createAuthenticatedRequest(link))
    outputfile = response.read()
    if not os.path.exists("download"):
        try:
            os.makedirs("download")
            print("done.")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                print("failed.")
                raise
    else:
        with open("download/" + barcode + ".fasta", 'wb') as f:
            f.write(outputfile)
            print("done.")
    
def downloadFasta(barcode):
    writeFastaToDisk(barcode, getFastaLink(barcode))

with open(args.list) as f:
    for line in f:
        barcode = line.strip()
        print "Downloading FASTA for barcode %s..." % barcode,
        downloadFasta(barcode)