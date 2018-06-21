import worker
result = ""

def work(data):
    global result
    result = data

worker.do_work(work)

print(result)

