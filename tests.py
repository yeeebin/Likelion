
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_new_view(self):
        response = self.client.get(reverse('post_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')

        response = self.client.post(reverse('post_new'), {
            'title': 'New Post',
            'content': 'This is a new post.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[2]))

    def test_post_edit_view(self):
        response = self.client.get(reverse('post_edit', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')

        response = self.client.post(reverse('post_edit', args=[self.post.pk]), {
            'title': 'Updated Post',
            'content': 'This is an updated post.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_detail', args=[self.post.pk]))

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_confirm_delete.html')

        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post_list'))
