#!/usr/bin/python3
"""
Main file for testing
"""
import time

makeChange = __import__('0-making_change').makeChange

start = time.perf_counter()
print(makeChange([1, 2, 25], 37))
print(f"Executed in {time.perf_counter() - start}")

start = time.perf_counter()
print(makeChange([1256, 54, 48, 16, 102], 1453))
print(f"Executed in {time.perf_counter() - start}")