import requests
import discord
import random
import os
import json
import meeting
import time

with open("Resource.Json") as config_file:
    config = json.load(config_file)

bot_token = config["bot_token"]
server_id = config["server_id"]
