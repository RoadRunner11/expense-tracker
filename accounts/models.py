from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER= [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
]

SECURITY_QUESTIONS= [
    ('1', 'What is your birthdate'),
    ('2', 'What is your old phone number'),
    ('3', 'What is your PET name'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles')
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=30,choices=GENDER,  null=True)
    phone_no = models.CharField(max_length=1000, null=True)
    security_q =models.CharField(max_length=30,choices=SECURITY_QUESTIONS, null=True)
    security_a = models.CharField(max_length=1000, null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()