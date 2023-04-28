#!/usr/bin/python3
from datetime import time, datetime
import os

"""
Algorithm
=========
1. Create an array with sites to be blocked,
   the items should have this format: "<IP>  <domain_name>"
2. Open the hosts file
3. Read the file contents
4. Open the same file with write mode
5. (a)Populate the opened file with the original content first
   (b)then add the sites to be blocked

6. Define break-time: give a duration
7. Check the current time
8. If current time is not within break time execute step 5(b)
"""

def it_is_rest_period(start_break, end_break):
    time_now = datetime.now().time()
    if time_now > start_break and time_now < end_break:
        return True
    else:
        return False

def file_contains_blocked_sites(file_contents, block_list, quantity):
    if quantity == "all":
        for item in block_list:
            if "{}\n".format(item) not in file_contents:
                return False
        return True
    if quantity == "any":
        for content in file_contents:
            if content.strip("\n") in block_list:
                return True
        return False

def site_blocker():
    start_break = time(12, 30)
    end_break = time(18, 00)

    filepath = "example.txt"
    block_list = [
            "127.0.0.1  twitter.com",
            "127.0.0.1  facebook.com",
            "127.0.0.1  snapchat.com",
            "127.0.0.1  myspace.com"
            ]

    with open(filepath) as file:
        file_contents = file.readlines()

    print(it_is_rest_period(start_break, end_break))
    print(file_contains_blocked_sites(file_contents, block_list, quantity="any"))
    print(file_contains_blocked_sites(file_contents, block_list, quantity="all"))
    if (it_is_rest_period(start_break, end_break) and
            file_contains_blocked_sites(
                file_contents, block_list, quantity="any")
            ):
        for content in file_contents.copy():
            if content.strip('\n') in block_list:
                file_contents.remove(content)
        print(file_contents)
        print("blocked_sites removed")

    if (it_is_rest_period(start_break, end_break) is False and
            file_contains_blocked_sites(
                file_contents, block_list, quantity="all") is False
            ):
        for item in block_list:
            if "{}\n".format(item) not in file_contents:
                file_contents.append("{}\n".format(item))
        print("blocked sites added")

    if (it_is_rest_period(start_break, end_break) is False and
            file_contains_blocked_sites(
                file_contents, block_list, quantity="all")
            ):
        for content in file_contents.copy():
            if file_contents.index(content) > file_contents.index("\n"):
                if content.strip("\n") not in block_list:
                    file_contents.remove(content)
        print("removed blocked sites not contained in the block list")

    with open(filepath, 'w') as file:
        for content in file_contents:
            if (content.strip("\n") == block_list[0] and
                    file_contents[file_contents.index(content)-1] != "\n"
               ):
                file.write("\n")
            file.write(content)


site_blocker()
