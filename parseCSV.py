from collections import defaultdict
import csv

from packetData import ipInfo, transactionInfo


def parseCSV(filename: str) -> defaultdict[str, ipInfo]:
    res: defaultdict[str, ipInfo] = defaultdict(ipInfo)
    with open(filename, newline='', mode='r') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            srcIP = row['srcIP']
            dstIP = row['dstIP']
            trInfo = transactionInfo(numPackets=int(row['numPackets']),
                                     totalSize=int(row['totalSize']))
            res[srcIP].packetsSend += trInfo.numPackets
            res[srcIP].bytesSend += trInfo.totalSize
            res[dstIP].packetsRec += trInfo.numPackets
            res[dstIP].bytesRec += trInfo.totalSize
    return res
