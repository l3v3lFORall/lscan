import nmap
import optparse

def nmapScan(targHost,targPort):
    pscan_nmap = nmap.PortScanner()
    pscan_nmap.scan(targHost,targPort)
    targ = pscan_nmap[targHost]
    state = [targHost,targ.state(),targ.all_tcp()]

def run():
    nmapScan("127.0.0.1",'21')



run()