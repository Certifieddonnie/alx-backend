#!/usr/bin/python3
"""
Test
"""
import sys

try:
    FIFOCache = __import__('1-fifo_cache').FIFOCache

    my_cache = FIFOCache()
    my_cache.print_cache()
    my_cache.put("test1", "myValue")
    my_cache.print_cache()
    my_cache.put(None, "myValue")
    my_cache.print_cache()
    my_cache.put("test1", None)
    my_cache.print_cache()
except:
    print(sys.exc_info()[1])
