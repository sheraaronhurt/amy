from datetime import date

from django.urls.base import reverse

from communityroles.models import (
    CommunityRole,
    CommunityRoleConfig,
    CommunityRoleInactivation,
)
from workshops.models import Award, Person
from workshops.tests.base import TestBase


class TestCommunityRoleMixin:
    def setUp(self):
        self.config = CommunityRoleConfig.objects.create(
            name="test",
            display_name="Test Role",
            link_to_award=True,
            link_to_membership=False,
            additional_url=True,
        )
        self.person = Person.objects.create(
            personal="Test",
            family="Family",
            email="test.person@example.org",
        )
        self.inactivation = CommunityRoleInactivation.objects.create(
            name="Lack of activity"
        )
        self.community_role = CommunityRole.objects.create(
            config=self.config,
            person=self.person,
        )


class TestCommunityRoleDetailsView(TestCommunityRoleMixin, TestBase):
    def setUp(self):
        super().setUp()
        super()._setUpUsersAndLogin()

    def test_view(self):
        # Arrange
        url = reverse("communityrole_details", args=[self.community_role.pk])
        # Act
        page = self.client.get(url)
        # Assert
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context["object"], self.community_role)
        self.assertEqual(page.context["title"], str(self.community_role))


class TestCommunityRoleCreateView(TestCommunityRoleMixin, TestBase):
    def setUp(self):
        super().setUp()
        super()._setUpAirports()
        super()._setUpLessons()
        super()._setUpBadges()
        super()._setUpInstructors()
        super()._setUpUsersAndLogin()
        self.data = {
            "communityrole-config": self.config.pk,
            "communityrole-person": self.person.pk,
            "communityrole-award": Award.objects.first().pk,
            "communityrole-start": date(2021, 11, 26),
            "communityrole-end": date(2022, 11, 26),
            "communityrole-inactivation": self.inactivation.pk,
            "communityrole-membership": "",
            "communityrole-url": "http://example.org",
        }

    def test_view(self):
        # Arrange
        url = reverse("communityrole_add")
        # Act
        page = self.client.post(url, self.data)
        redirect = CommunityRole.objects.last().get_absolute_url()
        # Assert
        self.assertEqual(page.status_code, 302)  # should redirect to new object
        self.assertRedirects(page, redirect)


class TestCommunityRoleUpdateView(TestCommunityRoleMixin, TestBase):
    def setUp(self):
        super().setUp()
        super()._setUpAirports()
        super()._setUpLessons()
        super()._setUpBadges()
        super()._setUpInstructors()
        super()._setUpUsersAndLogin()
        self.data = {
            "communityrole-config": self.config.pk,
            "communityrole-person": self.person.pk,
            "communityrole-award": Award.objects.first().pk,
            "communityrole-start": date(2021, 11, 26),
            "communityrole-end": date(2022, 11, 26),
            "communityrole-inactivation": self.inactivation.pk,
            "communityrole-membership": "",
            "communityrole-url": "http://example.org",
        }

    def test_view(self):
        # Arrange
        url = reverse("communityrole_edit", args=[self.community_role.pk])
        # Act
        page = self.client.post(url, self.data)
        redirect = self.community_role.get_absolute_url()
        # Assert
        self.assertEqual(page.status_code, 302)  # should redirect to new object
        self.assertRedirects(page, redirect)


class TestCommunityRoleDeleteView(TestCommunityRoleMixin, TestBase):
    def setUp(self):
        super().setUp()
        super()._setUpUsersAndLogin()

    def test_view(self):
        # Arrange
        url = reverse("communityrole_delete", args=[self.community_role.pk])
        redirect = "/dashboard/admin/"
        # Act
        page = self.client.post(f"{url}?next={redirect}")
        # Assert
        self.assertEqual(page.status_code, 302)  # should redirect to `?next`
        self.assertRedirects(page, redirect)
