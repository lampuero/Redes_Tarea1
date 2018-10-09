import socket


class ClientConnection:
    def __init__(self, name, address, port):
        self.socket = socket.socket()
        self.server_name = name
        self.socket.connect((address, port))

    def read_response(self):
        message = ""
        raw_char_message = self.socket.recv(1024)
        while '\n' not in message:
            char_message = raw_char_message.decode()
            message += char_message
        return "Server {} respondio:\n{}".format(
            self.server_name,
            message)

    def write_command(self, command):
        command_byte = command.encode()
        self.socket.send(command_byte)


def mainclient():
    servers_dict = dict()

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
            servers_dict[name] = ClientConnection(name, address, port)
            i += 3

    while True:
        # seccion critica 1
        command = input("Ingrese el comando:")
        servers_to_send_command = input("Ingrese el nombre de los servers:")
        servers_names = servers_to_send_command.split(" ")
        for name in servers_names:
            if name in servers_dict.keys():
                connection = servers_dict[name]
                connection.write_command(command)
                # lo siguiente debe realiarse en otro thread o similar
                response = connection.read_response()
                print(response)
            else:
                print("El nombre de server %s no es valido", name)
        # seccion critica 1


mainclient()
