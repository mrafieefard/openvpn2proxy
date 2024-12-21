from dotenv import load_dotenv
import os
load_dotenv()

env = os.environ

OVPN_USERNAME = env["OVPN_USERNAME"]
OVPN_PASSWORD = env["OVPN_PASSWORD"]