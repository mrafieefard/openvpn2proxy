import os
from type import Config

import sys
import subprocess

configs = os.path.join(os.curdir,"configs")

def get_configs_list():
    list = []

    for config in os.listdir(configs):
        if config.endswith(".ovpn"):
            list.append(Config(name=config.split(".")[0]))
            
    return list

def active_config(config : Config):
    try:
        subprocess.run(["openvpn","--config",os.path.join(configs,config.name+".ovpn")])
        return True
    except:
        return False
    
def deactive():
    subprocess.run(["killall","openvpn"])

def start_up():
    os.makedirs(configs,exist_ok=True)