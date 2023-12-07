import requests
import discord
import os
import json

import time

with open("Resource.Json") as config_file:
    config = json.load(config_file)

bot_token = config["bot_token"]
lsm_id = config["lsm_id"]
