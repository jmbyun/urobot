import tornado.ioloop
import tornado.web
import tornado.websocket
import threading
import queue
import webbrowser
import asyncio
import time
import socket
import pkg_resources
from .json_drawer import JsonDrawer

def get_free_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port

class MainWebHandler(tornado.web.RequestHandler):
    def get(self, matched_part=None):
        target_path = 'index.html' if matched_part is '' else matched_part
        web_template = pkg_resources.resource_string('web_templates', target_path)
        if target_path.endswith('htm') or target_path.endswith('html'):
            content_type = 'text/html'
        elif target_path.endswith('css'):
            content_type = 'text/css'
        else:
            content_type = 'text/plain';
        self.set_header("Content-Type", content_type)
        self.write(web_template)

class TaskWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.periodic_callback = tornado.ioloop.PeriodicCallback(self.check_queue, 100)
        self.periodic_callback.start()
        self.socket_semaphore.release() # Release the WebDrawer instance constructor.

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
    def __init__(self, port, task_queue, socket_semaphore):
        super().__init__()
        self.task_queue = task_queue
        self.socket_semaphore = socket_semaphore
        self.port = port

    def make_app(self):
        class ThreadTaskWebSocketHandler(TaskWebSocketHandler):
            def __init__(sub_self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                sub_self.task_queue = self.task_queue
                sub_self.socket_semaphore = self.socket_semaphore

        return tornado.web.Application([
            (r'/websocket', ThreadTaskWebSocketHandler),
            (r"/(.*)$", MainWebHandler),
        ])

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.app = self.make_app()
        self.app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

class WebDrawer(JsonDrawer):
    def __init__(self, port=8888):
        super().__init__()
        self.port = get_free_port() if port is None else port
        self.task_queue = queue.Queue()
        self.socket_semaphore = threading.Semaphore(value=0)
        self.web_thread = WebThread(
            port=port, 
            task_queue=self.task_queue,
            socket_semaphore=self.socket_semaphore)
        self.web_thread.start()
        self.open_browser()

    def open_browser(self):
        webbrowser.open_new('http://localhost:%d' % self.port)
        self.socket_semaphore.acquire() # Wait until the web socket connection is opened.

    def print(self, s):
        self.task_queue.put(s)