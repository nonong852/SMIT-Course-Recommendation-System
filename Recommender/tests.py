import unittest
from django.test import TestCase, Client
from .views import calculate_cosine_similarity, filter_courses, Recommender, coursedetails
from home.models import courses 
from RandR.models import RatingReview
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        # Initialize test data
        self.course1 = courses.objects.create(c_tfees=10000000, c_eligibility=80, c_rstream='Science', c_type='UG', c_img='/media/course1.jpg', c_code='1')
        self.course2 = courses.objects.create(c_tfees=700000, c_eligibility=70, c_rstream='any course', c_type='UG', c_img='/media/course2.jpg', c_code='16')
        # Add more test data as needed


    def test_calculate_cosine_similarity(self):
        # Test calculate_cosine_similarity function
        query = "some query"
        corpus = ["corpus document 1", "corpus document 2", "corpus document 3"]
        result = calculate_cosine_similarity(query, corpus)
        self.assertIsInstance(result, list)
        # Add more assertions as needed

    def test_filter_courses(self):
        # Test filter_courses function
        client = Client()
        response = client.post(reverse('filter_courses'), {'percentage': '80', 'stream': 'Science', 'courseType': 'Degree', 'minamount': '1500'})
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_Recommender(self):
        # Test Recommender function
        client = Client()
        response = client.get(reverse('Recommender'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_coursedetails(self):
        # Test coursedetails function
        client = Client()
        response = client.get(reverse('coursedetails', args=(self.course1.id,)))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
