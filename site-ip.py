import os
import socket
import re


class GetIP:

    def __init__(self, host='google.com'):
        self.host = host

    def slice_str(self, name: str) -> str:
        """Метод проверяет на наличие http заголовка """

        if name.startswith('h'):
            a = re.split('/', name)
            return a[2]
        return name

    def get_ip_and_country(self) -> dict:
        """Метод возвращает ip и страну хоста"""

        a = socket.gethostbyname(self.slice_str(self.host))
        c = os.popen('whois {} | {}'.format(
            a, "grep -E 'country|Country'")).read().split()
        try:
            return {'IP': a, c[0]: c[1]}
        except IndexError:
            return c


getip = GetIP(input('Enter host(default:google.com)'))

print(getip.get_ip_and_country())
