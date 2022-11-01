#!/usr/bin/env python3.10

import redis
r = redis.Redis(
    password='19260817',
    host='124.223.13.92',
    port='6379'
    )

keys = r.keys('*')
for key in keys:
    if key == b'test':
        continue
    all = r.hgetall(key)
    print(
        all[b'title'].decode(),
        all[b'image'].decode(),
        )

# str.encode('raw_unicode_escape').decode()
