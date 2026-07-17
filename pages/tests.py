from django.core import mail
from django.test import TestCase
from django.urls import reverse
from .models import MessageContact

class SiteTests(TestCase):
    def test_main_pages(self):
        for name in ("pages:home","pages:about","pages:services","pages:contact","joueurs:list","actualites:list"):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200)
    def test_detail_pages(self):
        self.assertEqual(self.client.get(reverse("joueurs:detail", args=["yannick-koffi"])).status_code, 200)
        self.assertEqual(self.client.get(reverse("actualites:detail", args=["jean-eudes-aka-signe-au-stade-rennais"])).status_code, 200)
    def test_contact_validation_and_submission(self):
        url = reverse("pages:contact")
        response = self.client.post(url, {"nom":"","email":"incorrect","message":""})
        self.assertContains(response, "Le nom est requis.")
        response = self.client.post(url, {"nom":"Awa","email":"awa@example.com","sujet":"Projet","message":"Bonjour"}, follow=True)
        self.assertContains(response, "Message envoyé")
        self.assertEqual(MessageContact.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
