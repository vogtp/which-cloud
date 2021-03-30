import unittest
from external.which_cloud.which_cloud import WhichCloud, Providers


class WhichClould(unittest.TestCase):

    def testCloudDetectionOrig(self):
        wc = WhichCloud()
        self.assertEqual(wc.is_ip('52.94.76.10') , Providers.AWS )
        self.assertEqual(wc.is_ip('104.214.20.0') , Providers.AZURE)
        self.assertEqual(wc.is_ip('35.185.160.160') , Providers.GCP)
        self.assertEqual(wc.is_ip('52.97.147.21'), None)

    
    def testCloudDetectionNew(self):
        wc = WhichCloud()
        self.assertEqual(wc.get_info('52.94.76.10').provider , Providers.AWS )
        self.assertEqual(wc.get_info('104.214.20.0').provider , Providers.AZURE)
        self.assertEqual(wc.get_info('35.185.160.160').provider , Providers.GCP)
        self.assertEqual(wc.get_info('52.94.76.10').name , str(Providers.AWS ))
        self.assertEqual(wc.get_info('104.214.20.0').name , str(Providers.AZURE))
        self.assertEqual(wc.get_info('35.185.160.160').name , str(Providers.GCP))

if __name__ == '__main__':
    unittest.main()
