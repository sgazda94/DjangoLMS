from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for dj_schulx.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    # objects = CustomUserManager()
    USER_TYPE_CHOICES = (
        (1, "guardian"),
        (2, "teacher"),
        (3, "manager"),
        (4, "superuser"),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return self.email


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("guardian-detail", args=[str(self.id)])

    def delete(self, *args, **kwargs):
        user = User.objects.filter(id=self.user_id)
        user.delete()
        super(Teacher, self).delete(*args, **kwargs)


class Student(models.Model):
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=9, blank=True)
    guardian = models.ForeignKey(
        Guardian, on_delete=models.CASCADE
    )  # related_name = 'guardians'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=9)
    street = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=255, blank=True)
    bank_account_number = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        user = User.objects.filter(id=self.user_id)
        user.delete()
        super(Teacher, self).delete(*args, **kwargs)


# Zastanowić się czy w przyszłości podczas tworzenia Managera nie zrobić przy okazji Teachera dla jednego usera
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=9)

    # website for school

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        user = User.objects.filter(id=self.user_id)
        user.delete()
        super(Teacher, self).delete(*args, **kwargs)
