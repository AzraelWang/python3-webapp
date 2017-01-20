#!/usr/bin/env python3
#coding=utf-8

import orm
import asyncio

from models import User, Blog, Comment

async def test():
    await orm.create_pool(loop=loop ,user='www-data', password='www-data', db='awesome')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close

