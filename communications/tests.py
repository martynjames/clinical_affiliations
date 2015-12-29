from django.test import TestCase

from models import Institution, Contact

# Create your tests here.


class TestCommunications(TestCase):
    """ Test class for checking that communications models work correctly """

    def setUp(self):
        self.institution1 = Institution.objects.create(
            name="Norwood Hospital",
            address_1="123 Washington Street",
            city="Norwood",
            state="MA",
            postal_code="02062",
        )
        self.institution2 = Institution.objects.create(
            name="Newton/Wellesley Hospital",
            address_1="2014 Washington Street",
            city="Newton",
            state="MA",
            postal_code="02462",
        )

    def test_single_options(self):
        first_contact = Contact.objects.create(
            institution=self.institution1,
            first_name="Martyn",
            last_name="James",
            title="Eventually, not CEO",
            email="mj@mj.com",
            phone="123-456-7890",
            ceo=True,
            primary_contact=True,
            administrative_contact=True,
        )

        # Make sure that we get back the contact when searching
        ceos_in_institution1 = Contact.objects.filter(institution=self.institution1, ceo=True)
        self.assertEqual(ceos_in_institution1.count(), 1)
        self.assertEqual(ceos_in_institution1[0].id, first_contact.id)

        real_ceo = Contact.objects.create(
            institution=self.institution1,
            first_name="Monica",
            last_name="Parker",
            title="The only CEO",
            email="moni@mj.com",
            phone="123-456-7891",
            ceo=True,
        )

        # Make sure that we get back only the second contact when searching
        ceos_in_institution1 = Contact.objects.filter(institution=self.institution1, ceo=True)
        self.assertEqual(ceos_in_institution1.count(), 1)
        self.assertNotEqual(ceos_in_institution1[0].id, first_contact.id)
        self.assertEqual(ceos_in_institution1[0].id, real_ceo.id)

        primaries_in_institution1 = Contact.objects.filter(institution=self.institution1, primary_contact=True)
        self.assertEqual(primaries_in_institution1.count(), 1)
        self.assertEqual(primaries_in_institution1[0].id, first_contact.id)

        real_primary_contact = Contact.objects.create(
            institution=self.institution1,
            first_name="Maggie",
            last_name="James",
            title="The only Primary Contact",
            email="maggie@mj.com",
            phone="123-456-7892",
            primary_contact=True,
        )
        primaries_in_institution1 = Contact.objects.filter(institution=self.institution1, primary_contact=True)
        self.assertEqual(primaries_in_institution1.count(), 1)
        self.assertNotEqual(primaries_in_institution1[0].id, first_contact.id)
        self.assertEqual(primaries_in_institution1[0].id, real_primary_contact.id)

        admin_in_institution1 = Contact.objects.filter(institution=self.institution1, administrative_contact=True)
        self.assertEqual(admin_in_institution1.count(), 1)
        self.assertEqual(admin_in_institution1[0].id, first_contact.id)

        real_admin_contact = Contact.objects.create(
            institution=self.institution1,
            first_name="Libby",
            last_name="James",
            title="The only Administrative Contact",
            email="libby@mj.com",
            phone="123-456-7893",
            administrative_contact=True,
        )
        admin_in_institution1 = Contact.objects.filter(institution=self.institution1, administrative_contact=True)
        self.assertEqual(admin_in_institution1.count(), 1)
        self.assertNotEqual(admin_in_institution1[0].id, first_contact.id)
        self.assertEqual(admin_in_institution1[0].id, real_admin_contact.id)

        ceos = Contact.objects.filter(ceo=True)
        self.assertEqual(ceos.count(), 1)

        Contact.objects.create(
            institution=self.institution2,
            first_name="Caroline",
            last_name="James",
            title="CEO",
            email="cal@mj.com",
            phone="123-456-7894",
            ceo=True,
        )

        # Make sure that we allow others in other institutions
        ceos = Contact.objects.filter(ceo=True)
        self.assertEqual(ceos.count(), 2)
