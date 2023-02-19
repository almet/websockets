from __future__ import annotations


try:
    from socket import create_server as socket_create_server
except ImportError:  # pragma: no cover
    import socket

    def socket_create_server(address, family=socket.AF_INET):  # type: ignore
        """Simplified backport of socket.create_server from Python 3.8."""
        sock = socket.socket(family, socket.SOCK_STREAM)
        try:
            sock.bind(address)
            sock.listen()
            return sock
        except socket.error:
            sock.close()
            raise


__all__ = ["socket_create_server"]
