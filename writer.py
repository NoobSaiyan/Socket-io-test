def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        

with open("/home/chand/techneith/projects/joel/socket-flask/static/log/job.log", 'w') as f:
    for i in infinite_sequence():
        print(i)
        f.write(str(i)+'\n')