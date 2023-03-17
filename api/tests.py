from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Bank, Branches

class BankTestCase(APITestCase):

    def setUp(self):
        # creating test banks and branches
        bank = Bank.objects.create(id=112233, name='TestBank')
        branch = Branches.objects.create(ifsc='ifsc0001', bank_id=bank, branch='branch1', address='address1',city='city1', district='district1', state='state1')
        bank = Bank.objects.create(id=112234, name='TestBank2')



    def test_get_banks(self):
        # api endpoint for get banks
        url = '/api/v1/getbanks/'
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.json()[0]['name'], "TestBank")
        self.assertEqual(response.json()[0]['id'], 112233)
        self.assertEqual(response.json()[1]['name'], "TestBank2")
        self.assertEqual(response.json()[1]['id'], 112234)
        self.assertEqual(len(response.json()),2)
    
    def test_get_branch(self):
        #api endpoint for branch with ifsc code ifsc0001
        url = '/api/v1/ifsc/ifsc0001/'
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.json()['ifsc'], 'ifsc0001')
        self.assertEqual(response.json()['bank_id']['id'], 112233)
        self.assertEqual(response.json()['bank_id']['name'], 'TestBank')
        self.assertEqual(response.json()['branch'], 'branch1')
        self.assertEqual(response.json()['address'], 'address1')
        self.assertEqual(response.json()['city'], 'city1')
        self.assertEqual(response.json()['district'], 'district1')
        self.assertEqual(response.json()['state'], 'state1')



