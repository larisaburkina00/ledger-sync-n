import time
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"}]'

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

contract = w3.eth.contract(address=w3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)
latest_block = w3.eth.block_number

def monitor_mints():
    global latest_block
    print(f"🔍 Watching NFT mint activity at {CONTRACT_ADDRESS}...")
    while True:
        try:
            new_block = w3.eth.block_number
            if new_block > latest_block:
                events = contract.events.Transfer().get_logs(fromBlock=latest_block + 1, toBlock=new_block)
                for e in events:
                    if e['args']['to'] != '0x0000000000000000000000000000000000000000':
                        print(f"🆕 NFT Minted! To: {e['args']['to']}, TokenID: {e['args']['tokenId']}")
                latest_block = new_block
            time.sleep(10)
        except Exception as ex:
            print(f"⚠️ Error: {ex}")
            time.sleep(30)

if __name__ == "__main__":
    monitor_mints()
