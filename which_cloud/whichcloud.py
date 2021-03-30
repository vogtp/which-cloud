import os
import pickle
from typing import Tuple

from netaddr.ip.sets import IPSet

from .providers import Providers

class NetType:
    
    def __init__(self, provider):
        self.name = str(provider)
        self.provider = provider

class WhichCloud:
    """
    >>> whichCloud = WhichCloud()
    >>> whichCloud.is_ip('123.123.123.123')
    """

    NO_NET_TYPE = NetType(None)

    def __init__(self):
        self.__types = {}
        self.__types['aws'] = NetType(Providers.AWS)
        self.__types['azure'] = NetType(Providers.AZURE)
        self.__types['gcp'] = NetType(Providers.GCP)
        self.__types['aws'].ips, self.__types['azure'].ips, self.__types['gcp'].ips = WhichCloud.__load_data()

    @staticmethod
    def __load_data() -> Tuple[IPSet, IPSet, IPSet]:
        pkg_dir = os.path.abspath(os.path.dirname(__file__))
        data_file = os.path.join(pkg_dir, "data", "data.pickle")
        with open(data_file, "rb") as f:
            aws_ips, azure_ips, gcp_ips = pickle.load(f)
            return aws_ips, azure_ips, gcp_ips

    def get_info(self, ip):
        for p in self.__types.values():
            if ip in p.ips:
                return p
        return self.NO_NET_TYPE

    def is_ip(self, ip):
        return self.get_info(ip).provider