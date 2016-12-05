import requests
import time
from threading import Thread
from multiprocessing import Process

K_TIMES = 100000

def count(x, y):
    c = 0
    while c < K_TIMES:
        c += 1
        x += x
        y += y

def write(x):
    f = open("tmp/test"+str(x)+".txt", "w")

    for x in range(K_TIMES*5):
        f.write("testwrite\n")
    f.close()

def read(x):
    f = open("tmp/test"+str(x)+".txt", "r")
    lines = f.readlines()
    f.close()


def io(x, y):
    write(x)
    read(x)


_head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0: WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrom/48.0.2564.116 Safari/537.36'
}
url = "http://www.tieba.com"


def http_request():

    try:
        webpage = requests.get(url, headers=_head)
        html = webpage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}

print("Please enter (1:Sequential/T: Multithreading/P:Multiprocess")

cmd = input()

if cmd == '1':
    print("Sequential Testing...")
    t = time.time()
    for x in range(10):
        count(1,1)
    print("Line cpu", time.time() -t)

    t = time.time()
    for x in range(10):
        write(x)
        read(x)
    print("Line IO", time.time() -t)

    t = time.time()
    for x in range(10):
        http_request()
    print("Line HTTP Request", time.time() -t)
elif cmd == 'T':
    print("Mutlithreading Testing...")
    counts = []

    t=time.time()
    for x in range(10):
        thread = Thread(target=count, args=(1,1))
        counts.append(thread)
        thread.start()

    e = counts.__len__()
    while True:
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    # IO
    ios = []
    t = time.time()
    for x in range(10):
        thread = Thread(target =io, args=(x, 1))
        ios.append(thread)
        thread.start()

    e = ios.__len__()
    while True:
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    # HTTP
    https = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=http_request)
        https.append(thread)
        thread.start()

    e = https.__len__()
    while True:
        for th in https:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

elif cmd == 'P':

    print("Multiprocess Testing...")
    counts = []

    t=time.time()
    for x in range(10):
        prc = Process(target=count, args=(1,1))
        counts.append(prc)
        prc.start()

    e = counts.__len__()
    while True:
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    # IO
    ios = []
    t = time.time()
    for x in range(10):
        prc = Process(target=io, args=(x, 1))
        ios.append(prc)
        prc.start()

    e = ios.__len__()
    while True:
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    # HTTP
    https = []
    t = time.time()
    for x in range(10):
        prc = Process(target=http_request)
        https.append(prc)
        prc.start()

    e = https.__len__()
    while True:
        for th in https:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

elif cmd=="1c":
    print(http_request())



