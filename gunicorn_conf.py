from multiprocessing import cpu_count

# Socket Path
bind = '0.0.0.0:8111'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/harukai/personal-site/access_log'
errorlog =  '/home/harukai/personal-site/error_log'
