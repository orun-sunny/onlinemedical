

from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver








class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    user_gender = models.CharField(max_length=6, default='Male', choices=user_sex)

    user_country = models.CharField(max_length=254)
    join_type = (('DOCTOR', 'Doctor'), ('PATIENT', 'Patient'))
    user_joinas = models.CharField(max_length=7, default='Doctor', choices=join_type)
    user_age = models.IntegerField(default=00)
    user_jobtitle = models.TextField(max_length=254)
    user_img = models.ImageField(upload_to='profile_pics', default='default.jpg')
    user_blogtitle = models.TextField(max_length=254)
    user_blogdes = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} Profile'



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        instance.profile.save()
class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    Artical= models.TextField(default='')
    Artical_img = models.ImageField(upload_to='post_pics', default='default.jpg')
    pub_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
