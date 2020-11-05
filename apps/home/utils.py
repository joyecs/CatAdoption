import string, random, os, datetime, logging


"""
create secret key using official utils
"""
def get_random_secret_key():
    from django.utils.crypto import get_random_string as grs
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return grs(50, chars)
"""
get rando string with size, and extra=[] with string.letters and string.digits
"""
def get_random_str(size=6, extra=[]):
    letters = string.ascii_letters + string.digits
    if extra: letters += extra
    return ''.join(random.choice(letters) for i in range(size))
#=====end get random str

'''
get random date from s to e with format of "yyyymmdd"
Or it will be a random date from now to three years a gao
'''
def get_random_date(s=None, e=None):
    if s and e:
        s = datetime.strptime(s,"%Y%m%d").timestamp()
        e = datetime.strptime(e,"%Y%m%d").timestamp()
        random_timestamp = random.randint(int(s), int(e))
        return datetime.datetime.fromtimestamp(random_timestamp)
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(days=3*365)
    s = int(ago.timestamp())
    e = int(now.timestamp())
    rd = random.randint(s,e)
    return datetime.datetime.fromtimestamp(rd)
#===end of random date

"""
log to file log.log, BASE DIR/log.log or WHERE-RUNING/log.log
"""
def log_file(msg:str,):
    dir_ = getattr(settings,'BASE_DIR', os.path.dirname(os.path.abspath(__file__)))
    fp = os.path.join(dir_, "log.log")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(fp,'a+', encoding='utf-8') as f:
        f.write(f"{now} -- {msg}\n")
    print(dir_)
#=====end of log file

"""
log message into base/log.log
"""
def log_debug(msg, request=None):
    if not settings.DEBUG:
        return
    if request != None:
        try:
            msg = msg + " GET: {}; POST: {}".format(request.GET, request.POST)
        except:
            msg = msg + "request data error"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = os.path.join(settings.BASE_DIR, "log.log")
    logging.basicConfig(
        filename=file,
        filemode='a',
        format='%(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    logging.debug(str(now) + ':  ' + str(msg))
#===end of log debug

