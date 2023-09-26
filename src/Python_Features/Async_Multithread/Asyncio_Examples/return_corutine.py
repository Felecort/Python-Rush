import asyncio


async def sleepy_alarm(person, time):
    await asyncio.sleep(time)
    print(f"{person} -- wake up!")


async def wake_up_gang():
    tasks = [
        asyncio.create_task(sleepy_alarm("Bob", 3), name="Wake up Bob"),
        asyncio.create_task(sleepy_alarm("Yudi", 4), name="Wake up Yudi"),
        asyncio.create_task(sleepy_alarm("Doris", 2), name="Wake up Doris"),
        asyncio.create_task(sleepy_alarm("Kim", 3), name="Wake up Kim"),
    ]
    await asyncio.gather(*tasks)


# loop = asyncio.new_event_loop()
# 
# alarm = sleepy_alarm(3)
asyncio.run(wake_up_gang())
