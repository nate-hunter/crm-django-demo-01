# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     first_name = models.CharField(max_length=200, blank=True, null=True)
#     last_name = models.CharField(max_length=200, blank=True, null=True)
#     phone = models.CharField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.first_name


# def create_profile(sender, insance, created, **kwargs):
#     if created:
#             Profile.objects.create(user=instance)
#             print('Profile created')


# def update_profile(sender, insance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print('Profile updated.')
