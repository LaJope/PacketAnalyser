from dataclasses import dataclass

@dataclass
class ipInfo:
    packetsRec: int = 0
    bytesRec: int = 0
    packetsSend: int = 0
    bytesSend: int = 0

@dataclass
class transactionInfo:
    numPackets: int
    totalSize: int
