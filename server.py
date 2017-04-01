#!/usr/bin/env python
# encoding: utf-8
# Revisión 2014 Carlos Bederián
# Revisión 2011 Nicolás Wolovick
# Copyright 2008-2010 Natalia Bidart y Daniel Moisset
# $Id: server.py 656 2013-03-18 23:49:11Z bc $

import optparse
import socket
import connection
from constants import *


class Server(object):
    """
    El servidor, que crea y atiende el socket en la dirección y puerto
    especificados donde se reciben nuevas conexiones de clientes.
    """

    def __init__(self, addr=DEFAULT_ADDR, port=DEFAULT_PORT,
                 directory=DEFAULT_DIR):
        print "Serving %s on %s:%s." % (directory, addr, port)
	self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creacion del socket
	self.s.bind((addr,port)) #asocio el socket a la direccion IP(addr) y al puerto(port)
	self.s.listen(1) #puede conectarse solo un cliente
        self.s.buffer = '' #buffer que va a almacenar los datos que va recibiendo del cliente
	self.s.client = None #variable que almacena al cliente del cual recibo el pedido
	self.s.ip_client = None #variable que almacena la IP del cliente atendido
	# FALTA: Crear socket del servidor, configurarlo, asignarlo
        # a una dirección y puerto, etc.

    def serve(self):
        """
        Loop principal del servidor. Se acepta una conexión a la vez
        y se espera a que concluya antes de seguir.
        """
        while True:
		self.client, self.ip_client = self.s.accept() #acepto la conexion del cliente
		self.buffer = "" #inicializo el buffer
		while True #mientras el cliente este conectado...
			self.recv_server()
		
			# Aqui creo, deberia en primer lugar parsear el pedido del cliente y
			# si todo esta bien, ejecutar cada comando en el orden en que los
			# envio el cliente :)


            # FALTA: Aceptar una conexión al server, crear una
            # Connection para la conexión y atenderla hasta que termine.



    def recv_server(self):
	""" Recibe los datos y los acumula en buffer """
	data_recv = '' #variable que almacena el pedido del cliente
	while not eol in data_recv
		data_recv = data_recv + self.client.recv(1024) #voy recibiendo el pedido
		if len(data_recv) = 0  #si no recibio nada, hace un break
			break
	self.buffer = self.buffer + data_recv #almacena en el buffer lo recibido hasta el momento



def main():
    """Parsea los argumentos y lanza el server"""

    parser = optparse.OptionParser()
    parser.add_option(
        "-p", "--port",
        help=u"Número de puerto TCP donde escuchar", default=DEFAULT_PORT)
    parser.add_option(
        "-a", "--address",
        help=u"Dirección donde escuchar", default=DEFAULT_ADDR)
    parser.add_option(
        "-d", "--datadir",
        help=u"Directorio compartido", default=DEFAULT_DIR)

    options, args = parser.parse_args()
    if len(args) > 0:
        parser.print_help()
        sys.exit(1)
    try:
        port = int(options.port)
    except ValueError:
        sys.stderr.write(
            "Numero de puerto invalido: %s\n" % repr(options.port))
        parser.print_help()
        sys.exit(1)

    server = Server(options.address, port, options.datadir)
    server.serve()

if __name__ == '__main__':
    main()
