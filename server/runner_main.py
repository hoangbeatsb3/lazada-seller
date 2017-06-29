import time
from runners.price_automatically_worker import PriceAutomaticallyWorker
from config import RunnerConfig


if __name__ == "__main__":

  starttime=time.time()
  worker = PriceAutomaticallyWorker()

  while True:
    worker.execute()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

