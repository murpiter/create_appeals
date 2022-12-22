from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

from .sender import send_message, init_sender, destroy_sender


class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', ' PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        self.set_status(204)
        self.finish()


class MainHandler(BaseHandler):
    channel = None

    def post(self):
        if self.request.headers['Content-Type'] == 'application/json':
            send_message(self.channel, self.request.body)


def make_app():
    return Application([
        (r"/", MainHandler),
    ])


def main():
    app = make_app()
    app.listen(8888)

    connection, channel = init_sender()

    MainHandler.channel = channel

    IOLoop.current().start()

    destroy_sender(connection, channel)
