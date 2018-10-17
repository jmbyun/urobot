import sys
import os; sys.path.insert(0, os.path.abspath('..'))
import urobots


import tornado.ioloop
import tornado.web
import tornado.websocket
import threading
import queue
import webbrowser
import asyncio
import time

f = open('./test-web.html', 'r')
web_cont = f.read()
f.close()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(web_cont)

class TaskWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print('WebSocket opened')
        self.periodic = tornado.ioloop.PeriodicCallback(self.check_queue, 100)
        self.periodic.start()

    def on_message(self, message):
        self.write_message(u'You said: ' + message)

    def on_close(self):
        self.periodic.stop()
        print('WebSocket closed')
        
    def check_queue(self):
        while True:
            try:
                task = self.task_queue.get_nowait()
                self.write_message(u'Check-queue: ' + str(task))
            except queue.Empty:
                break

class WebThread(threading.Thread):
    def __init__(self, port, task_queue):
        super().__init__()
        self.task_queue = task_queue
        self.port = port

    def make_app(self):
        class ThreadTaskWebSocket(TaskWebSocket):
            def __init__(sub_self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                sub_self.task_queue = self.task_queue

        return tornado.web.Application([
            (r'/websocket', ThreadTaskWebSocket),
            (r"/", MainHandler),
        ])

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.app = self.make_app()
        self.app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

class WebDrawer(urobots.JsonDrawer):
    def __init__(self, port=8888):
        super().__init__()
        self.port = port
        self.task_queue = queue.Queue()
        self.web_thread = WebThread(port=port, task_queue=self.task_queue)
        self.web_thread.start()
        self.open_browser()

    def open_browser(self):
        webbrowser.open_new('http://localhost:%d' % self.port)
        time.sleep(1)

    def print(self, s):
        self.task_queue.put(s)

world = urobots.World(drawer=WebDrawer(), walls=[urobots.Wall(urobots.Position(1, 0), urobots.Position(2, 0))])

robot = urobots.Robot()
world.add_piece(robot)
robot.move()

