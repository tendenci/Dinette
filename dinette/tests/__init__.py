#Auto created tests via DJango test utils

from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model
from django.core.urlresolvers import reverse
class Testmaker(TestCase):
    fixtures = ['test_data']

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        """Check if the homepage is accessible by all"""
        r = self.client.get(reverse('dinette_category'), {})
        self.assertEqual(r.status_code, 200)

    def test_new_topics(self):
        r = self.client.get(reverse('dinette_new_for_user'))
        #check for redirection for guest users 
        self.assertEqual(r.status_code,302)
        #check for results in case of loggedin users
        r = self.client.login(username='plaban',password='plaban') #this is in test fixture
        self.assertEqual(r,True) 
        r = self.client.get(reverse('dinette_new_for_user'))
        self.assertEqual( len(r.context['new_topic_list']),0) # as there are no entry in the db

    def test_unanswered_topics(self):
        r = self.client.get(reverse('dinette_unanswered'))
        
        
    def test_user_profile(self):
        response = self.client.get('/forum/users/plaban')
        user =  response.context['user_profile']
        self.assertEqual(user.email,'plaban.nayak@gmail.com')
    
    def test_category(self):
        response = self.client.get('/forum/dinette/')
        category =  response.context['category']
        self.assertEqual(category.name,"Dinette")
        self.assertEqual(category.description,"Dinette is the best forum app for Django, Period. You are using it right now.")
        supercategory = category.super_category
        self.assertEqual(supercategory.name,"Python and Django")
        
