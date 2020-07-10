from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer

# @receiver(post_save, sender=User)


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )

        print('PROFILE WAS CREATED FOR')

post_save.connect(customer_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print('Profile updated.')
