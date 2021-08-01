from browser.websocket import WebSocket
from browser import alert

class Server:
	def __init__(self, url):
		ws = WebSocket(url)
		ws.bind('open',    self.open)
		self._socket = ws
	def open(self, event):
		ws = self._socket
		ws.bind('message', self.message)
		ws.bind('close',   self.close)
		ws.bind('error',   self.error)
	def send(self, message):
		self._socket.send(message)
	def recv(self, message): pass
	def message(self, event):
		self.recv(event.data)
	def close(self, event): pass
	def error(self, event): pass
