from collections import defaultdict

from parseCSV import parseCSV
from writeToCSV import writeToCSV
from packetData import ipInfo
from parseArgs import parseArgs


def main():
    infile, outfile = parseArgs()
    if not outfile.endswith(".csv"):
        outfile = outfile + ".csv"

    try:
        IPsInfo: defaultdict[str, ipInfo] = parseCSV(infile)
    except:
        printErr("Could not properly parse file " + infile)
        exit(1)

    try:
        writeToCSV(outfile, IPsInfo)
    except:
        printErr("Could not write to file " + outfile)
        exit(1)


def printErr(message: str) -> None:
    print("[ERROR]", message)


if __name__ == "__main__":
    main()
