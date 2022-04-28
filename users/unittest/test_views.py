import imp
from urllib import response
from .test_setup import TestSetUp

class TestViews(TestSetUp):

    def test_user_can_not_login_correctly(self):
        res = self.client.post(self.login_url,self.user_data,format="multipart")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)
        
    def test_user_can_login_correctly(self):
        res = self.client.post(self.login_url,self.user_data,format="multipart")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 200)