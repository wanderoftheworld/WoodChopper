import asyncio

async def do_something():
    # Do something that takes a long time
    await asyncio.sleep(1)
    return "Done!"

async def main():
    tasks = [asyncio.create_task(do_something()) for _ in range(10)]
    for result in asyncio.as_completed(tasks):
        print(await result)

asyncio.run(main())
