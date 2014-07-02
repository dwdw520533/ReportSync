#enc

import web
import os
import logging
import platform
from sqlalchemy import create_engine

#web.config.debug = True

iswindows = False
if platform.system() == "Windows":
    iswindows = True

HERE = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(HERE)
logpath = os.path.join(PARENT_DIR, 'log').replace('\\', '/')
DBN = r'mysql://root:123456@172.16.1.194/BCSourceData_OM?charset=utf8'
engine = create_engine(DBN, echo=False, pool_recycle=7200)

MEDIA_ROOT = os.path.join(PARENT_DIR, 'media').replace('\\', '/')

if not os.path.exists(logpath):
    os.mkdir(logpath)
logfile = os.path.join(logpath, 'report_sync.txt')
#print logfile
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(filename)s]: %(levelname)s - %(message)s',
                    #datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%Y-%m-%d %X',
                    filename=logfile,
                    filemode='a')