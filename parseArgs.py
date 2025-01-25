import textwrap
import argparse


def parseArgs() -> tuple[str, str]:
    parser = argparse.ArgumentParser(
        prog="packetAnalyser",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """\
                    Parse csv file in format:
                    srcIP,dstIp,srcPort,dstPort,numPackets,totalSize

                    and outputs info in csv file in format:
                    IP,packetsRec,bytesRec,packetsSend,bytesSend"""
        ),
    )
    parser.add_argument(
        "-i", "--infile", help="input csv file", required=True, type=str
    )
    parser.add_argument(
        "-o",
        "--outfile",
        help="output csv file",
        required=False,
        type=str,
        default="paan",
    )
    args = parser.parse_args()
    return (args.infile, args.outfile)
