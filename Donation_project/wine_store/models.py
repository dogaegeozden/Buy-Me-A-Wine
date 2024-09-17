# LIBRARIES
from django.db import models
from django.utils import timezone



# DATA CLASSES

##############################

# HOME PAGE

##############################

class HomePageMetaDescription(models.Model):
    
    text = models.TextField(max_length=500, null=False, blank=False, default="Send me a token of your love and gratitude with wine and a personalized message!")
    
    class Meta:
        verbose_name_plural = "Home Page Meta Descriptions"

class HomePageHookLine(models.Model):
    
    text = models.TextField(max_length=500, null=False, blank=False, default="Hey, would you like to buy me a wine?", help_text="Hook line should be an interesting paragraph, fact, or a question to cath audience's attention.")

    class Meta:
        verbose_name_plural = "Home Page Hook Lines"

class Message(models.Model):
    
    full_name = models.CharField(max_length=70, verbose_name="Full Name")
    email = models.CharField(max_length=120, verbose_name="E-mail")
    message = models.TextField(max_length=10000, verbose_name="Message")
    sending_time = models.DateTimeField(blank=True, null=True, verbose_name="Send Time", default=timezone.now)

    class Meta:
        verbose_name_plural = "Messages"


