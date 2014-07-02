# -*- coding: utf-8 -*-
import web
import os
import settings

urls = ("/weagent", "weagent.weagent",
        '/weagent/media/(.*)', 'media_file',
        )

class media_file:
    def GET(self, path):
        try:
            fpath = os.path.join(settings.MEDIA_ROOT, path).replace('\\', '/')
            f = open(fpath, 'rb')
            web.header('Content-Type', 'application/octet-stream')
            return f.read()
        except Exception, ex:
            return ex.strerror

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == '__main__':
    app.run()