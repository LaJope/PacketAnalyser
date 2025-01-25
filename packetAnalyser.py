from collections import defaultdict
import textwrap
import argparse

from parseCSV import parseCSV
from writeToCSV import writeToCSV
from packetData import ipInfo

def main():
    infile, outfile = parseArgv()
    try:
        IPsInfo: defaultdict[str, ipInfo] = parseCSV(infile)
    except:
        printErr("Could not properly parse file " + infile)
        exit(1)

    try:
        writeToCSV(outfile, IPsInfo)
    except:
        printErr('Could not write to file ' + outfile)
        exit(1)


def printErr(message: str) -> None:
    print('[ERROR]', message)


def parseArgv() -> tuple[str, str]:
    parser = argparse.ArgumentParser(
            prog='packetAnalyser',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                    Parse csv file in format:
                    srcIP,dstIp,srcPort,dstPort,numPackets,totalSize

                    and outputs info in csv file in format:
                    IP,packetsRec,bytesRec,packetsSend,bytesSend'''))
    parser.add_argument('-i', '--infile', help='input csv file',
                        required=True, type=str)
    parser.add_argument('-o', '--outfile', help='output csv file',
                        required=False, type=str)
    args = parser.parse_args()
    return (args.infile, args.outfile)


if __name__ == '__main__':
    main()

