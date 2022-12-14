#!/usr/bin/env python3.10


import redis

r = redis.Redis(
    password='19260817',
    host='124.223.13.92',
    port=6379,
    charset='utf-8',
    decode_responses=True,
    db=0
)
# 获取v所有键值
keys = r.keys('*')
for key in keys:

    if 'BV' not in key:
        print("UP:", r.hgetall(key)['name'])  # .decode()
        continue
    all_key = r.hgetall(key)
    print(
        "VIDEO:",
        all_key['title'],  # .decode(),
        "\n",
        all_key['image'],  # .decode(),
    )
