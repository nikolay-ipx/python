class Server:
    s_ip = 1
    def __init__(self):
        self.buffer = []
        self.ip = Server.s_ip
        Server.s_ip += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.ser = {}

    def link(self,server):
        self.ser[server.ip] = server
        server.router = self

    def unlink(self,server):
        s = self.ser.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.ser:
                self.ser[d.ip].buffer.append(d)
        self.buffer.clear()


class Data:
    def __init__(self, msg, ip):
        self.data = msg
        self.ip = ip





router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()