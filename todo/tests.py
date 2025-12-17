from django.test import TestCase
from .models import TodoItem

class TodoModelTest(TestCase):
    def test_task_creation(self):
        task = TodoItem.objects.create(subject="Test Task", notes="Test Notes")
        self.assertEqual(task.subject, "Test Task")
        self.assertTrue(isinstance(task, TodoItem))