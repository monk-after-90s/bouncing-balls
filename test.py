import asyncio


async def main():
    asyncio.create_task(asyncio.sleep(1), name='sleep')
    print(repr(asyncio.all_tasks()))
    asyncio.get_running_loop().run_in_executor()

asyncio.run(main())
