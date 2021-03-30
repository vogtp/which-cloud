import unittest
from external.which_cloud.which_cloud import WhichCloud, Providers


class WhichClould(unittest.TestCase):

    def testCloudDetectionOrig(self):
        wc = WhichCloud()
        self.assertEqual(wc.is_ip('52.94.76.10') , Providers.AWS )
        self.assertEqual(wc.is_ip('104.214.20.0') , Providers.AZURE)
        self.assertEqual(wc.is_ip('35.185.160.160') , Providers.GCP)

    
    def testCloudDetectionNew(self):
        wc = WhichCloud()
        self.assertEqual(wc.get_info('52.94.76.10').provider , Providers.AWS )
        self.assertEqual(wc.get_info('104.214.20.0').provider , Providers.AZURE)
        self.assertEqual(wc.get_info('35.185.160.160').provider , Providers.GCP)
        self.assertEqual(wc.get_info('52.94.76.10').name , str(Providers.AWS ))
        self.assertEqual(wc.get_info('104.214.20.0').name , str(Providers.AZURE))
        self.assertEqual(wc.get_info('35.185.160.160').name , str(Providers.GCP))

    def testCloudDetectionAdd(self):
        wc = WhichCloud()
        wc.add_addr(Providers.MICROSOFT, '52.97.147.21', "ms")
        self.assertEqual(wc.get_info('52.97.147.21').name, "ms")
        self.assertEqual(wc.get_info('52.97.147.21').provider, Providers.MICROSOFT)
        self.assertEqual(wc.get_info('52.97.147.22').provider, None)
        wc.add_addr(Providers.MICROSOFT, '52.96.0.0/12')
        wc.add_addr(Providers.MICROSOFT, '52.97.147.21', "ms")
        self.assertEqual(wc.get_info('52.97.147.21').name, "ms")
        self.assertEqual(wc.get_info('52.97.147.21').provider, Providers.MICROSOFT)
        self.assertEqual(wc.get_info('52.97.147.22').provider, Providers.MICROSOFT)

    def testPrivateNetworks(self):
        wc = WhichCloud()
        self.assertEqual(wc.get_info('10.0.0.0').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('10.43.32.5').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('10.0.30.2').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('172.16.0.0').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('172.16.10.10').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('172.1.0.0').provider , None )
        self.assertEqual(wc.get_info('192.168.10.10').provider , Providers.PRIVATE )
        self.assertEqual(wc.get_info('192.23.10.10').provider ,None )

        
    def testPrivateNetworks(self):
        wc = WhichCloud()
        self.assertEqual(wc.get_info('127.30.04.088').provider , Providers.LOCAL )

if __name__ == '__main__':
    unittest.main()
