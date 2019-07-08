from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()

# A beat is a meeting in a series of meetings
class Beat(models.Model):
    beat_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    meeting_on = models.DateField(auto_now_add=True,null=True, blank=True)
    meeting_start_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    meeting_end_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    meeting_type  = models.CharField(max_length=100)
    meetupURL = models.URLField(max_length=200,null=True, blank=True)
                                       
    class Meta:
    ordering = ['-meeting_on',]

    def get_absolute_url(self):
    return reverse('beat_detail', args=[str(self.pk)])
       
    def __str__(self):
        return self.name


# A matron is a member of a group
class Matron(models.Model):
    userid = models.OneToOneField(User, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    socialin = models.URLField(max_length=200,null=True, blank=True)
    last_rating = models.DecimalField(max_digits=6, decimal_places=4,null=True, blank=True)
    last_rating_on = models.DateField(auto_now_add=True,null=True, blank=True)
    is_crone = models.BooleanField(default=False)
    
    class Meta:
    ordering = ['name',]

    def get_absolute_url(self):
        return reverse('matron_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view
    
    def __str__(self):
        return self.name


# a dress is a question on the survey
class Dress(models.Model):
    dress_name = models.CharField(max_length=100)
    question = models.TextField(max_length=1000,null=True, blank=True)
    order_by_help = models.PositiveSmallIntegerField(null=True, blank=True)
                                        
    class Meta:
        ordering = ['name',]

    class Meta:
    ordering = ['order_by_help',]
    
    def get_absolute_url(self):
        return reverse('dress_detail', args=[str(self.pk)])
    
    def __str__(self):
        return self.name



# a shoe an answer to a survey question
class Shoe(models.Model):
    shoe_keyword = models.CharField(max_length=100)
    shoe_boolean = models.BooleanField
    shoe_more = models.TextField(max_length=1000,null=True, blank=True)
    shoe_URL = models.URLField(max_length=200,null=True, blank=True)
    shoe_matron = models.ForeignKey(Matron,on_delete=models.PROTECT, null=True, blank=True)
                                      
    class Meta:
        ordering = ['keyword',]

    def get_absolute_url(self):
    return reverse('skin_detail', args=[str(self.pk)])
    
    def __str__(self):
        return self.name


class Dressing(models.Model):
    beat_id = models.ForeignKey('Beat', on_delete=models.PROTECT, null=True, blank=True)
    matron_id = models.ForeignKey('Matron', on_delete=models.PROTECT, null=True, blank=True)
    shoe_id = models.ForeignKey('Shoe', on_delete=models.PROTECT, null=True, blank=True)
    dressing_id = models.ForeignKey('Dressing', on_delete=models.PROTECT, null=True, blank=True)


