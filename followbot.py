import tweepy
import time

# menu
run: bool = True

# options
version: int = 1 # available: [1]
offset: int = 1

# accounts followers to follow
accounts: str = ["BarackObama", "katyperry", "elonmusk", "CInsiderAlerts"]
# follows per loop
follows_per_loop: int = 30
# amount of time in seconds between each loop of n amount
# 3600 = 1 hour
loop_interval: int = 3600

# V1 Settings: follows_per_loop = 20, loop_interval = 3600

# Authenticate to Twitter
auth = tweepy.OAuthHandler("client_key", "client_token")
auth.set_access_token("access_key", "access_token")
api = tweepy.API(auth, wait_on_rate_limit=True, retry_delay=100)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

def get_followers(name):
    user = api.get_follower_ids(screen_name=name)
    return user

def follow_user_by_id(id):
    api.create_friendship(user_id=id)


def follow_account_followers(name, q: int):
    x = get_followers(name)
    i: int = 0
    while i <= (follows_per_loop):
        try:
            follow_user_by_id(x[i + offset*30])
            print(f"Followed {x[i + offset*30]}. Next follow in: {6.5*(i+1)} seconds")
            if i % 10 == 0 and i != 0:
                print(f"Loop Update: {i} followed in loop {q}.")
                print(f"Total Update: {((q-1)*follows_per_loop)+i} followed.")
        except:
            print("Error. Sleeping for 15min.")
            time.sleep(60*15)
        i += 1
        time.sleep(6.5*(i+1)) 
    print("Completed.")

i: int = 0
while run:
    if version == 1:
        print("Executing: follow bot [V1]")
        #follows_per_loop = 20
        #loop_interval = 3600
        o = i + 1
        follow_account_followers(accounts[i], o)
        print(f"Loop {i + 1}/{len(accounts)} Completed.")
        i += 1
        if i == len(accounts) - 1:
            run = False
            print("Killed follow bot. [run=False]")
        print(f"Next action in {loop_interval//60} minutes.")
        time.sleep(loop_interval)
    else:
        print("Error: No program found. Running latest version.")
        version -= 1