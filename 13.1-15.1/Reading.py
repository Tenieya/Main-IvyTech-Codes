from datetime import datetime
import multiprocessing
import time
import random

# 13.1 Write the current date as a string to the text file today.txt

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("today.txt", "w") as file:
    file.write(current_date)


# 13.2 Read the text file today.txt into the string today_string

with open("today.txt", "r") as file:
    today_string = file.read().strip()
    print(today_string)


# 13.3 Parse the date from today_string

time_format = "%Y-%m-%d %H:%M:%S"
parsed_date = datetime.strptime(today_string, time_format)
print(f"Current date: {parsed_date}")


# 15.1 Create three processes, where each waits for a random time between 0 and 1 second, prints the current time, and then exits.

def print_time():
    wait_time = random.uniform(0, 1) 
    time.sleep(wait_time)
    print(f"Current time: {datetime.now().strftime('%H:%M:%S')}, waited for {wait_time:.2f} seconds.")

if __name__ == '__main__':
    processes = [multiprocessing.Process(target=print_time) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
