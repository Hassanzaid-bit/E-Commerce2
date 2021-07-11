from django.test import TestCase
from .models import Portable, Desktop

# Create your tests here.

def PortableModelTest(TestCase):

    def test_string_representation(self):
        portable = Portable(Brand="HP", series= "1234567", memory="8GB",model="AFE34SHJD")
        self.assertEqual(str(portable), portable.Brand, portable.series, portable.memory, portable.model)

