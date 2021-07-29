import socket


def ip_interna():
	return socket.gethostbyname( socket.gethostname() ) ;

def ip_externa():
    conexion = socket.socket(
        socket.AF_INET
        , socket.SOCK_DGRAM
    )
    try:       
        conexion.connect(  
            ('10.255.255.255', 1)  
        )
        IP = conexion.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        conexion.close()
    return IP

