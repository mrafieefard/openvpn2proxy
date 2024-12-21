import os
from type import Config

import sys
import subprocess

from env import OVPN_PASSWORD,OVPN_USERNAME

configs = os.path.join(os.curdir,"configs")
auth_path = os.path.join(os.curdir,"auth.txt")
def get_configs_list():
    list = []

    for config in os.listdir(configs):
        if config.endswith(".ovpn"):
            list.append(Config(name=config.split(".")[0]))
            
    return list

def active_config(name : str):
    try:
        deactive()
        if OVPN_USERNAME and OVPN_PASSWORD:
            subprocess.run(["openvpn","--config",os.path.join(configs,name+".ovpn"),"--auth-user-pass",auth_path],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        else:
            subprocess.run(["openvpn","--config",os.path.join(configs,name+".ovpn")],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        return True
    except Exception as e:
        print(e)
        return False
    
def deactive():
    subprocess.run(["killall","openvpn"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

def start_up():
    if OVPN_USERNAME and OVPN_PASSWORD:
        open("auth.txt","w+").write(f"{OVPN_USERNAME}\n{OVPN_PASSWORD}")
    os.makedirs(configs,exist_ok=True)