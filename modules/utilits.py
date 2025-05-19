import requests
from web3 import Web3

FOLDER_PATH = "C:/Users/User/Desktop/Scripts/DP_Bas_Gainet/Irys/data"


def _read_file(file_name):
        with open(f"{FOLDER_PATH}/{file_name}") as f:
            temp_dict = []
            lines = f.readlines()
            for line in lines:
                temp_dict.append(line.strip())
            f.close
            return temp_dict


def proxy_checker(proxy: dict):
    try:
        requests_proxy = {
               "https": f"http://{proxy[1]}:{proxy[2]}@{proxy[0]}"  
        }
        requests.get("http://httpbin.io/ip", proxies=requests_proxy)
        return True
    except Exception as err:
        return False
    

def reader():
    privates = _read_file("private_keys.txt")
    proxies = _read_file("proxies.txt")
    if len(privates) != len(proxies):
        raise Exception("Amount of privates and proxies different")
    
    processed_proxies = []
    for proxy in proxies:
        splited_text = proxy.split("@")
        ip_port = str(splited_text[0]).removeprefix("http://").removeprefix("https://")
        splited_text = splited_text[1].split(":")
        login = splited_text[0]
        password = splited_text[1]

        processed_proxies.append([ip_port, login, password])

    i=0
    data = []
    while i < len(privates)-1:
        data.append({
            "private_key":privates[i], 
            "proxy":processed_proxies[i],
            })
        i+=1

    return data



def get_address(private_key):
    web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))
    return Web3.to_checksum_address(web3.eth.account.from_key(private_key).address)