import logging

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

from codigofacilito import unreleased

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug('>>> Ejecutando')
    workshops= unreleased()
    logging.debug(workshops)
    logging.debug('>>> Finalizando')