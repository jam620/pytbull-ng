#!/usr/bin/env python
###
# @author $Author: sebastiendamaye $
# @version $Revision: 7 $
# @lastmodified $Date: 2011-05-24 13:34:19 +0200 (Tue, 24 May 2011) $
#
import configparser

class BadTraffic():
    def __init__(self, target, cnf):
        # Read configuration
        self.config = configparser.RawConfigParser()
        self.config.read(cnf)

        self._target = target
        self.payloads = []

    def getPayloads(self):

        ### Nmap Xmas Scan
        self.payloads.append([
            "Nmap Xmas scan",
            "command",
            "%sudo% %nmap% -sX -p 80 %target%",
            ""
            ])

        ### Malformed Traffic
        # ihl=2 - Internet Header Length, it should be min 5 (so malformed)
        # version=3 - IP Version, it should be 4 or 6 (so malformed)
        self.payloads.append([
            "Malformed Traffic",
            "scapy",
            """send(IP(dst="%target%", ihl=2, version=3)/ICMP(), verbose=0)""",
            ""
            ])

        ### [TO REMOVE] Land Attack
        # attack from 1997, works on Windows XP SP2
        # self.payloads.append([
        #     "Land Attack",
        #     "scapy",
        #     """send(IP(src="%target%",dst="%target%")/TCP(sport=135,dport=135), verbose=0)""",
        #     ""
        #     ])

        return self.payloads

if __name__ == "__main__":
    print(BadTraffic("192.168.100.48",'config.cfg').getPayloads())
