from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from draw_manager_app.models import Draw


class LoggedInTestCase(TestCase):

    def setUp(self):

        self.password = 'hiro0419'

        self.test_user = get_user_model().objects.create_user(
            username='hirofumi',
            email = 'hirofumi.4.4.19@gmail.com',
            password=self.password
        )

        self.client.login(email=self.test_user.email,password=self.password)

class TestDrawCreateView(LoggedInTestCase):

    def test_create_draw_success(self):

        params = {'customer':'テスト会社', 'draw_number':'test_number', 'material':'testmaterial',
                  'material_size':'test_size', 'outsourcing':'test',
                  'outsourcing_content':'test', 'photo1':'','photo2':'', 'photo3':''}
        response = self.client.post(reverse_lazy('draw:draw_create'),params)

        self.assertRedirects(response, reverse_lazy('draw:draw_list'))

        self.assertEqual(Draw.objects.filter(draw_number='test_number').count(),1)

    def test_create_draw_failuer(self):

        response = self.client.post(reverse_lazy('draw:draw_create'))

        self.assertFormError(response, 'form','draw_number','このフィールドは必須です。')

class TestDrawUpdateView(LoggedInTestCase):

    def test_update_draw_success(self):

        draw = Draw.objects.create(user=self.test_user,draw_number='図面編集前')

        params = {'draw_number':'図面編集後'}

        response = self.client.post(reverse_lazy('draw:draw_update',kwargs={'pk':draw.pk}),params)

        self.assertRedirects(response, reverse_lazy('draw:draw_detail',kwargs={'pk':draw.pk}))

        self.assertEqual(Draw.objects.get(pk=draw.pk).draw_number,'タイトル編集後')

    def test_update_draw_failure(self):

        response = self.client.post(reverse_lazy('draw:draw_update',kwargs={'pk':999}))

        self.assertEqual(response.status_code, 404)

class TestDrawDeleteView(LoggedInTestCase):

    def test_delete_draw_success(self):

        draw = Draw.objects.create(user=self.test_user,draw_number='図面番号')

        response = self.client.post(reverse_lazy('draw:draw_delete',kwargs={'pk':draw.pk}))

        self.assertRedirects(response,reverse_lazy('draw:draw_list'))

        self.assertEqual(Draw.objects.filter(pk=draw.pk).count(),0)

    def test_delete_draw_failure(self):

        response = self.client.post(reverse_lazy('draw:draw_delete',kwargs={'pk':999}))

        self.assertEqual(response.status_code,404)

    