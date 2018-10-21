import tornado.ioloop
import tornado.web
import tornado.websocket
import threading
import queue
import webbrowser
import asyncio
import time
import pkg_resources
from .json_drawer import JsonDrawer

web_template = pkg_resources.resource_string('templates', 'web.html')

class MainWebHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(web_template)

class TaskWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.periodic_callback = tornado.ioloop.PeriodicCallback(self.check_queue, 100)
        self.periodic_callback.start()

    def on_message(self, message):
        pass

    def on_close(self):
        self.periodic_callback.stop()
        
    def check_queue(self):
        while True:
            try:
                task = self.task_queue.get_nowait()
                self.write_message(task)
            except queue.Empty:
                break

class WebThread(threading.Thread):
    def __init__(self, port, task_queue):
        super().__init__()
        self.task_queue = task_queue
        self.port = port

    def make_app(self):
        class ThreadTaskWebSocketHandler(TaskWebSocketHandler):
            def __init__(sub_self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                sub_self.task_queue = self.task_queue

        return tornado.web.Application([
            (r'/websocket', ThreadTaskWebSocketHandler),
            (r"/", MainWebHandler),
        ])

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.app = self.make_app()
        self.app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

class WebDrawer(JsonDrawer):
    def __init__(self, port=8888):
        super().__init__()
        self.port = port
        self.task_queue = queue.Queue()
        self.web_thread = WebThread(port=port, task_queue=self.task_queue)
        self.web_thread.start()
        self.open_browser()

    def open_browser(self):
        # webbrowser.open_new('http://localhost:%d' % self.port)
        time.sleep(1)

    def print(self, s):
        self.task_queue.put(s)