PROMETHEUS_URL = 'http://18.117.222.226:9090'
INSTANCE = '54.233.219.114:9100'
JOB = 'nutbox-service'
QUERY_INTERVAL = '1m0s'
QUERY_STEP = 0.2

class LogSettings:
    @classmethod
    def default(cls) -> None:
        return cls(PROMETHEUS_URL,INSTANCE,JOB,QUERY_INTERVAL,QUERY_STEP)

    def __init__(self, prometheus_url, instance, job, query_interval, query_step) -> None:
        self.prometheus_url = prometheus_url
        self.instance = instance
        print()
        self.job = job
        self.query_interval = query_interval
        self.query_step = query_step