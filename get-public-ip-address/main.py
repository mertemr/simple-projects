# Get public IP address from command line
import requests


ip = requests.get('https://checkip.amazonaws.com').text.strip()
print(ip)