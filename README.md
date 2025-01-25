# PacketAnalyser
This is a program to analyse csv file produced by my other project [PacketSniffer](https://github.com/LaJope/PacketSniffer.git).

## Help
usage: packetAnalyser [-h] -i INFILE [-o OUTFILE]

Parse csv file in format:  
srcIP,dstIp,srcPort,dstPort,numPackets,totalSize  

and outputs info in csv file in format:  
IP,packetsRec,bytesRec,packetsSend,bytesSend  

options:  
  -h, --help             show this help message and exit  
  -i, --infile INFILE    input csv file  
  -o, --outfile OUTFILE  output csv file  

## Dependencies
There are no dependencies apart from python3 (version 3.7+ for dataclass).  
You can install it (if it is not installed automatically) using your prefered package manager.  
For example:
#### Ubuntu
```bash
sudo apt install python3
```
#### Arch linux
```bash
sudo pacman -S python
```
## Run
To run, you need to type in your terminal the following:
```bash
python3 packetAnalyser.py
```
and supply it with arguments.
