import threading
import asyncio
import random



# this is corutine (async function)
async def very_important_task():
    wait_for = random.randint(0, 9)
    for i in range(10):
        # sleep(1) Not working
        print("I'm very busy")
        if i == wait_for:
            await asyncio.sleep(2)


async def imitate_responce():
    input("How was yr day?\n")
    print("Great!")


async def main():
    # threading.Thread(target=very_important_task).start()
    # threading.Thread(target=imitate_responce).start()
    task_1 = very_important_task()
    # print(task_1, type(task_1))
    task_2 = imitate_responce()
    await asyncio.gather(task_1, task_2)
    

if __name__ == "__main__":
    asyncio.run(main())