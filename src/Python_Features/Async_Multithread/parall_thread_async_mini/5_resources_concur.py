import multiprocessing
import time
from pathlib import Path


def write_to_file(file_path, process_id):
    with open(file_path, "a") as file:
        text = "-" * 20000
        file.write(f"process id is {process_id}. {text}\n")


if __name__ == "__main__":
    file_path = Path(__file__).parent / "0_shared_file.txt"
    processes = []
    start = time.time()
    for i in range(500):
        process = multiprocessing.Process(target=write_to_file, args=(file_path, i))
        processes.append(process)

    for process in processes:
        process.start()


    for process in processes:
        process.join()

    print(time.time() - start)
    print("Done")
