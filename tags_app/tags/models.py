from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_company_admin = models.BooleanField(default = False)
    is_customer_admin = models.BooleanField(default = False)
    tags = TaggableManager()

    @property
    def get_user(self):
        return User.objects.get(pk = self.user_id)

    @property
    def user_name(self):
        return User.objects.get(pk = self.user_id).username

@receiver(post_save, sender = User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            profile = instance.profile
        except:
            profile = Profile.objects.create(user = instance)
    instance.profile.save()
