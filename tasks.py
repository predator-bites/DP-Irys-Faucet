import random
from loguru import logger

from modules.utilits import reader
from config import GAMES_PER_ACC, MIN_POINTS,SHUFFLE, TO_CLAIM_FAUCET

def task_generate():
    client_data: list = reader()

    i=0
    for dict_ in client_data:
        random_games_amount = random.randint(GAMES_PER_ACC[0], GAMES_PER_ACC[1])
        dict_["games_amount"] = random_games_amount

        if TO_CLAIM_FAUCET==True:
            dict_["faucet"] = True
        
        client_data[i] = dict_
        i+=1

    logger.debug("Tasks for wallets generated successfully")
    return client_data


    


