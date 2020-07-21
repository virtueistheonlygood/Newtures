import bot1
import bot2
import bot3
from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
import threading
import time

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour = '0-23', minute = '0-59')
    def trx():
        bot1.main()
    def bat():
        bot2.main()
    def bnb():
        bot3.main()

    try:
        t1 = threading.Thread(target=bnb)
        t2 = threading.Thread(target=bat)
        t3 = threading.Thread(target=trx)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
    except:
        print ("error")
sched.start()