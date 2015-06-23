#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Iga sona twitter bot
import twitter

api = twitter.Api(consumer_key="put",
                  consumer_secret="your",
                  access_token_key="keys",
                  access_token_secret="here")

with open("arv") as f:
    arv = int(f.read())

with open("sonad") as f:
    sonad = f.read().decode("utf-8").splitlines()
    sona = sonad[arv]

for i in range(50):
    try:
        api.PostUpdate(sona)
        break
    except: # sometimes it returns an error
        pass

with open("arv", "w") as f:
    f.write(str(arv + 1))
