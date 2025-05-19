import requests
from twocaptcha import TwoCaptcha
from loguru import logger
from config import TWO_CAPTCHA_API_KEY


class Faucet():

    def claim_faucet(self, address, useragent, browser_version, proxy):
        twocaptcha_proxy = f"{proxy[1]}:{proxy[2]}@{proxy[0]}"
        requests_proxy = {
               "https": f"http://{proxy[1]}:{proxy[2]}@{proxy[0]}"   
        }

        url = "https://irys.xyz/faucet"

        # Solve captcha
        site_key = "0x4AAAAAAA6vnrvBCtS4FAl-"
        solver = TwoCaptcha(apiKey=TWO_CAPTCHA_API_KEY)


        
        result = solver.turnstile(
            sitekey=site_key,
            url=url,
            useragent=useragent,
            proxy={"type":"HTTPS","uri":twocaptcha_proxy}
            )
        
        c_token = result["code"]
        
        payload = {
            "captchaToken": c_token,
            "walletAddress": address
        }

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "content-length":"1024",
            "content-type": "application/json",
            "origin": "https://irys.xyz",
            "priority": "u=1, i",
            "referer": "https://irys.xyz/faucet",
            "sec-ch-ua": f'"Google Chrome";v={browser_version}, "Chromium";v={browser_version}',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows", 
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site":"same-origin",
            "sec-gpc": "1",
            "user-agent": useragent
        }

        result = requests.post(
               url="https://irys.xyz/api/faucet",
               proxies=requests_proxy,
               headers=headers,
               json=payload
        )

        if result.status_code == 200:
              logger.success(f"Successfully requested tokens for {address}")
        elif result.status_code == 500:
              logger.error("Too many requests for IP (Check proxy uniqueness) or faucet was claimed today")
        
   