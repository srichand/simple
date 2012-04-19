import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
proc_name = "www.srichand.net/blog"
pidfile = "/tmp/www.srichand.net.blog.pid"
daemon = True

