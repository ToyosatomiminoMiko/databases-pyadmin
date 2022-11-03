#!/usr/bin/env python3.10


import redis

r = redis.Redis(
    password='19260817',
    host='124.223.13.92',
    port=6379,
    charset='utf-8',
    decode_responses=True
)

keys = r.keys('*')
for key in keys:
    if key == 'test':
        continue
    if 'BV' not in key:
        print("UP:", r.hgetall(key)['name'])
        continue
    all_key = r.hgetall(key)
    print(
        "VIDEO:",
        all_key['title'],
        "\n",
        all_key['image'],
    )
    
    # str.decode()用于处理字符串hex
    
