import random




class Fake_User_Agent():
    def __init__(self):
        pass

    def random_browser_version(self):
        versions = [
            '125',
            '126',
            '127',
            '128',
            '129',
            '130',
            '131',
            '132',
            '133',
            '134',
            '135'
        ]
        
        browser_version = versions.pop(random.randint(0,len(versions)-1))
        useragent = f"Mozilla/5.0 Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36"

        return useragent, browser_version
    

    def random_timezone(self):
        timezones = [
            "America/New_York",
            "America/Chicago",
            "America/Los_Angeles",
            "America/Phoenix",
            "Europe/London",
            "Europe/Paris",
            "Europe/Berlin",
            "Asia/Tokyo",
            "Asia/Singapore",
            "Australia/Sydney",
        ]
        return timezones.pop(random.randint(0, len(timezones)-1))


    def random_args(self):
        base_args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--password-store=basic",
            "--use-mock-keychain",
            "--disable-software-rasterizer",
            "--disable-gpu-sandbox",
            "--no-default-browser-check",
            "--allow-running-insecure-content",
        ]

        optional_args = [
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-site-isolation-trials",
            "--disable-setuid-sandbox",
            "--ignore-certificate-errors",
            "--disable-accelerated-2d-canvas",
            "--disable-bundled-ppapi-flash",
            "--disable-logging",
            "--disable-notifications",
            ]

        args = base_args.copy()
        random_header = optional_args[random.randint(0, len(optional_args)-1)]
        args.append(random_header)
        
        return args

    
    def ultra(self):
        useragent, browser_version = self.random_browser_version()
        timezone = self.random_timezone()
        args = self.random_args()

        return useragent, browser_version, timezone, args



        



