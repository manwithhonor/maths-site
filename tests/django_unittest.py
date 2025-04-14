from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from proj_maths.models import CustomUser
from proj_maths.views import show_test
from unittest.mock import Mock

# assertContains(response, text, ...)  # проверяет, что в ответе сервера содержится указанный текст;
# assertTemplateUsed(response, template_name, ...)  # проверяет, что при рендеринге страницы использовался указанный шаблон;
# assertRedirects(response, expected_url, ...)  # проверяет, было ли перенаправление;

class CustomUserModelTest(TestCase):
    def setUp(self):
        CustomUser.objects.create(phone="89123123145", age=29)

    def test_user_creation(self):
        user = CustomUser.objects.get(phone="89123123145")
        self.assertEqual(user.age, 29)


class TermListViewTest(TestCase):
    def test_user_list_view(self):
        response = self.client.get(reverse('terms-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Проект про математику")


class TermListViewUnitTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_book_list_view(self):
        request = self.factory.get('/terms-list')
        response = show_test(request)
        self.assertEqual(response.status_code, 200)


class TestEmail(TestCase):
    def test_send_email(self):
        # Заменяем реальную функцию на mock-объект
        mock_send = Mock(return_value=True)
        send_email = mock_send  # Подмена (в реальности используйте patch!)

        result = send_email("test@example.com", "Hello", "Test body")

        self.assertTrue(result)
        mock_send.assert_called_once_with("test@example.com", "Hello", "Test body")