import random
from loguru import logger
import time

from modules.logo import show_logo
from modules.faucet import Faucet
from modules.utilits import  proxy_checker, get_address
from modules.userangent_randomiser import Fake_User_Agent
from config import SHUFFLE, DELAY
from tasks import task_generate


show_logo()
client_data: dict = task_generate()
failed = []

if SHUFFLE == True:
     random.shuffle(client_data)


i = 0 
while i < len(client_data)-1:
    try:
        private = client_data[i]["private_key"]
        proxy = client_data[i]["proxy"]
        games_amount = client_data[i]["games_amount"]
        faucet_status = client_data[i]["faucet"]

        proxy_line = f"{proxy[1]}:{proxy[2]}@{proxy[0]}"
        
        # Proxy work check 
        result = proxy_checker(proxy=proxy)
        if result == False:
            raise Exception(f"Proxy {proxy[0]} is not working ")

        faucet_module = Faucet()

        address = get_address(private_key=private)

        logger.info(f"Working on wallet with address {address}")
        fake_useragent = Fake_User_Agent()
        useragent, browser_version, timezone, args = fake_useragent.ultra()
        # Faucet
        if faucet_status == True:
                faucet_module.claim_faucet(address=address,useragent=useragent, browser_version=browser_version,proxy=proxy)
        timesleep = random.randint(DELAY[0], DELAY[1])
        logger.debug(f"Sleeping untill next wallet for {timesleep} seconds")
        time.sleep(timesleep)
        i+=1

            
    except Exception as err:
         logger.error(err)
         failed.append(client_data[i])




