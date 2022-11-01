#!/usr/bin/env python3.10


import redis
r = redis.Redis(
    password='',
    host='',
    port=6379,
    charset='utf-8'
    )

keys = r.keys('*')
for key in keys:
    if key == b'test':
        continue
    if b'BV' not in key:
        print("UP:", r.hgetall(key)[b'name'].decode())
        continue
    all_key = r.hgetall(key)
    print(
        "VIDEO:",
        all_key[b'title'].decode(),
        "\n",
        all_key[b'image'].decode(),
        )

