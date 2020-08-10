#Install these packages first.
#pip install --upgrade pip aiohttp aiofiles

#Sequential program example

import time

def make_coffee():
	print("Start Making Coffee...")
	time.sleep(10)
	print("Finish Making Coffee...")

def make_toast():
	print("Start making toast...")
	time.sleep(10)
	print("Finish making toast...")


def morning_routine():
	make_coffee()
	make_toast()


t1 = time.perf_counter()
morning_routine()
elapsed = time.perf_counter() - t1
print(f"Time Taken: {elapsed:0.2f} seconds.")

#async program example

import asyncio
import time

async def make_coffee():
	print("Start Making Coffee...")
	await asyncio.sleep(10)
	print("Finish Making Coffee...")

async def make_toast():
	print("Start making toast...")
	await asyncio.sleep(10)
	print("Finish making toast...")

async def morning_routine():
	await asyncio.gather(make_coffee(), make_toast())


t1 = time.perf_counter()
asyncio.run(morning_routine())
elapsed = time.perf_counter() - t1
print(f"Time Taken: {elapsed:0.2f} seconds.")
