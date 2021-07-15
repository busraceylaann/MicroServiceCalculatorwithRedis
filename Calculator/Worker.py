from rq import Connection, Queue, Worker
from redis import Redis

redis = Redis(host='redis')

if __name__ == '__main__':
    with Connection(connection=redis): #verilerimizi bu baglantıda işliyoruz
        q = Queue()
        Worker(q).work()