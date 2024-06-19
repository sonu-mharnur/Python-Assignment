from rest_framework.test import APITestCase
from .models import Task

class TaskAPITestCase(APITestCase):
    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'Test Task', 'description': 'Test Description', 'status': 'PENDING'})
        self.assertEqual(response.status_code, 201)

    def test_list_tasks(self):
        Task.objects.create(title='Test Task', description='Test Description', status='PENDING')
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
