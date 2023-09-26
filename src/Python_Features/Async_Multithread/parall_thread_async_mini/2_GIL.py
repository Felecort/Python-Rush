import threading
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_fibonacci(start, end, result):
    fib_sequence = []
    for i in range(start, end):
        fib_sequence.append(fibonacci(i))
    result.extend(fib_sequence)


def main():
    num_terms = 300
    num_threads = 16
    chunk_size = num_terms // num_threads

    threads = []
    result = []
    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else num_terms
        thread = threading.Thread(target=calculate_fibonacci, args=(start, end, result)) 
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    finish_time = time.time()
    print(result)
    print(f"time: {finish_time - start_time:.2f}s")

if __name__ == "__main__":
    main()