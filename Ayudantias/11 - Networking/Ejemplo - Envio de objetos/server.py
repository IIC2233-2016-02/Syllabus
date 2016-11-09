import socket
from pickle import dumps, loads
from random import randint, random
from sys import exit
from threading import Thread

DEFAULT_HOST = socket.gethostname()
DEFAULT_PORT = 1234


class Server:

    def __init__(self, host=None, port=None):
        """
        Esta clase representa al servidor, que se ubicara en 
        host:port. Intercambia contenido con el cliente
        """
        host = DEFAULT_HOST if host is None else host
        port = DEFAULT_PORT if port is None else port
        # AF: AddressFamily => AF_INET: Par (host, port) o direccion IPv4
        # SOCK: SocketKind => SOCK_STREAM: TCP, SOCK_DGRAM: UDP
        # Por lo tanto, conexion TCP con un par (host, port) es:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._current_list = list()
        self.is_alive = True
        # Coloca el programa en la direccion indicada
        self._socket.bind((host, port))
        # Numero maximo de conexiones "en espera"
        self._socket.listen(5)
        # Guardamos a quienes se conectan a nuestro servidor
        self._connections = list()
        self._acceptor = Thread(target=self._accept_client)
        self._acceptor.daemon = True
        self._acceptor.start()

    def _accept_client(self):
        """
        Esta funcion es la que 'despierta' cuando un cliente se 
        conecta al servidor
        """
        while self.is_alive:
            client_socket, client_address = self._socket.accept()
            client_thread = Thread(target=self._hear_message_from_client, args=(client_socket, ))
            client_thread.daemon = True
            client_thread.start()
            print("Nuevo cliente: {}".format(client_address))
            self._connections.append((client_socket, client_thread))

    def _hear_message_from_client(self, client_socket):
        """
        Esta funcion es la que estara atenta a si el cliente
        envia algo al servidor
        """
        while self.is_alive:
            data = client_socket.recv(1024)
            content = loads(data)
            self._current_list = content
            print("Client: {}".format(content))

    def send_message_to_clients(self, new_element):
        """
        Esta funcion recibe un mensaje, lo serializa
        y luego lo envia al cliente indicado
        """
        self._current_list.append(new_element)
        print("Enviando... {}".format(self._current_list))
        final_content = dumps(self._current_list)
        for client_socket, client_thread in self._connections:
            client_socket.send(final_content)

    def disconnect(self):
        """
        Esta funcion deberia cerrar la conexion
        """
        self.is_alive = False
        self._socket.close()

if __name__ == '__main__':
    server = Server()
    while server.is_alive:
        new_element = input()
        server.send_message_to_clients(new_element)
