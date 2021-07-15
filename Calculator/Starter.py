#kütüphanelerimizi tanımlıyoruz
import os
import time
from rq import Connection, Queue
from redis import Redis
from Calculate import calculate


def main():
    while True:
        redis = Redis(host='redis') #host olarak tanımladık
        problem = input("Problemi Girin : ")
        q = Queue(connection=redis) #tanımlamış olduğumuz hostla kuyruk oluşturduk.

        start_time = time.time()
        asycn_result = q.enqueue(calculate,problem) #kuyruğa gelen görev eklenir.ona iletmek istediğiniz
                                                    # argümanlarla birlikte istenen işlevi kuyruğa alırız.

        done = False
        while not done:
            os.system('clear')
            print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
            done = True
            job_result = asycn_result.return_value #dönen değeri job_result degiskenine attık
            if job_result is None:
                done = False
                job_result = 'Hesaplanıyor'
            print('Sonuç = %s' % (job_result))
            time.sleep(0.2)

if __name__ == '__main__':
    with Connection():
        main()