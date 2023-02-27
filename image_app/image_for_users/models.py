from django.contrib.auth.models import User
from django.db import models

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Images(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images")
    image_base = ImageSpecField(source="image",
                                processors=[ResizeToFill(height=200, width=200)],
                                format='JPEG',
                                options={'quality': 60})
    image_premium = ImageSpecField(source="image",
                                   processors=[ResizeToFill(height=400, width=400)],
                                   format='JPEG',
                                   options={'quality': 60})

    def __str__(self):
        return f"{self.title} - {self.image} "


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Memberships(models.Model):
    MEMBERSHIPS_TYPES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    )
    plan_types = models.CharField(choices=MEMBERSHIPS_TYPES, max_length=10, default='Basic')

    def __str__(self):
        return f"{self.plan_types}"


class Subscription(models.Model):
    author = models.ForeignKey(Author, related_name='subscriptions', on_delete=models.PROTECT, null=False)
    images = models.ForeignKey(Images, related_name='subscriptions', on_delete=models.PROTECT)
    subscription = models.ForeignKey(Memberships, related_name='subscriptions', on_delete=models.PROTECT, null=False,
                                     default="basic")

    def __str__(self):
        return f"{self.author} {self.subscription}"
