from collections import defaultdict
import csv

from packetData import ipInfo


def writeToCSV(filename: str, IPsInfo: defaultdict[str, ipInfo]) -> None:
    fieldnames = ["IP", "packetsRec", "bytesRec", "packetsSend", "bytesSend"]
    with open(filename, newline="", mode="w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ip, info in IPsInfo.items():
            writer.writerow(
                {
                    "IP": ip,
                    "packetsRec": info.packetsRec,
                    "bytesRec": info.bytesRec,
                    "packetsSend": info.packetsSend,
                    "bytesSend": info.bytesSend,
                }
            )


if __name__ == "__main__":
    print("This is a helper file. Don't run it on it's own.")
