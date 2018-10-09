import socket



class ClientConnection:
    def __init__(self, name, address, port):
        self.socket = socket.socket()
        self.server_name = name
        self.socket.connect((address,port))

    def read_response(self):
        message = ""
        raw_char_message = self.socket.recv(1024)
        while raw_char_message != b'':
            char_message = raw_char_message.decode()
            message += char_message
        # seccion critica
        print("Server %s respondio:\n", self.server_name)
        print(message)
        # seccion critica

    def write_command(self,command):
        command_byte = command.encode()
        self.socket.send(command_byte)

def mainclient():
    servers = dict()

    servers_data = input("Ingrese la informacion de los servers (o la direccion del json) en una linea:\n")
    servers_data_split = servers_data.split(" ")
    if servers_data_split.__len__() == 1:
        pass
        # procesar json
    else:
        i = 0
        while i < len(servers_data_split):
            name = servers_data_split[i]
            address = servers_data_split[i+1]
            port = int(servers_data_split[i+2])
            servers[name] = ClientConnection(name, address, port)
    



def client(servers_name):
    pass

servers_data = input('Ingrese los datos de los servers en una linea\n')
print(type(servers_data))
servers_data_split = servers_data
while True:
    message =input('-> ')
    print (message)