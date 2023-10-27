import asyncio


async def fetch_data(url):
    # print('start fetching', url)
    await asyncio.sleep(2)  # 模拟IO操作
    # print('done fetching', url)
    return {'data': url}


async def main():
    print('start')
    task1 = asyncio.create_task(fetch_data('url1'))
    task2 = asyncio.create_task(fetch_data('url2'))
    print('tasks created')
    res1 = await task1
    res2 = await task2
    print('results:', res1, res2)


async def main2(i: int):
    task = asyncio.create_task(fetch_data('url{}'.format(i)))
    res = await task
    return res

for i in range(5):
    res = asyncio.run(main2(i))
    res2 = asyncio.run(main2(i+1))
    print(res)
    print(res2)

# asyncio.run(main())