from django.db import models
from django.core.files.base import ContentFile
from django.utils.safestring import mark_safe
from django.core.files.storage import FileSystemStorage, DefaultStorage, Storage, get_storage_class
from django.conf import settings
import os
import sys
import copy
from PIL import Image 
from .function import make_small_image, make_wide_image, make_round_image, make_tall_image, new_name

# class OverwriteStorage(DefaultStorage):

#     def get_available_name(self, name, max_length=None):
#         # If the filename already exists, remove it as if it was a true file system
#         if self.exists(name):
#             self.delete(name)
#         return name
class OverwriteStorage(get_storage_class()):

    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name


# Create your models here.
class Info_Home(models.Model):
    message_home_1 = models.CharField(max_length = 30)
    message_home_2 = models.CharField(max_length = 30)
    desc_home_1 = models.CharField(max_length = 70)
    desc_home_2 = models.CharField(max_length = 70)
    button_home = models.CharField(max_length = 15)
    image_home = models.ImageField(upload_to='pics')
    destinations = [("#top", "Home"),
                ("#blog", "News"),
                ("#featured", "Developer Team"),
                ("#detailednews", "Detailed News"),
                ("#projects", "Soul&Spirit"),
                ("#projects2", "CoronaWars"),
                ("#contact", "Contact")]
    home_destination = models.CharField(max_length=15, 
                                        choices=destinations,
                                        default="top",)

class News(models.Model):
    news_test = 'Mensaje de prueba'
    news_date = models.IntegerField(help_text= "Write as 'ddmmyyyy= Day/Month/Year', example 10052019=10/05/2019")
    news_auto_date = models.DateField(auto_now_add=True)
    news_headline = models.CharField(max_length = 70)
    news_body = models.TextField(default="Replace this text for one that has at least 250 characters.",
                                help_text = "Minimum of 250 characters and a maximum of 500 characters.")
    news_image = models.ImageField(upload_to='pics', storage=OverwriteStorage())
    news_body_big = models.TextField()
    news_title_big = models.CharField(max_length = 30)
    news_subtitle_big = models.CharField(max_length = 70)
    news_image_big = models.ImageField(upload_to='pics', storage=OverwriteStorage())
    news_image_big.verbose_name = "Wide_News_Image"

    def save(self, *args, **kwargs):
        if new_name(self.news_image, '_small')!=None: self.news_image = make_small_image(self.news_image, '_small')
        if new_name(self.news_image_big, '_wide')!=None: self.news_image_big = make_wide_image(self.news_image_big, '_wide')
        super().save(*args, **kwargs)

    def news_example(self):
        return mark_safe('<img src="%s" />' % '/media/pics/news.jpg')

    def big_news_example(self):
        return mark_safe('<img src="%s" />' % '/media/pics/news2.jpg')
    

class Developer_Team_Information(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length = 30)
    subtitle = models.CharField(max_length = 70)
    body = models.TextField()

class SoulAndSpirit(models.Model):
    plantillas = [("A", "Model A"),
                ("B", "Model B"),
                ("C", "Model C")]
    select_plantilla = models.CharField(max_length=2, 
                                        choices=plantillas,
                                        default="B",)
    image_1 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)                                   
    image_2 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)                                   
    image_3 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)     
    image_3.help_text = "Only necessary for models A y B"                              
    image_4 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_4.help_text = "Only necessary for model B"                                  
    image_5 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_5.help_text = "Only necessary for models B y C"                               
    image_6 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)   
    image_6.help_text = "Only necessary for model C"
    image_1_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_2_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_3_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_4_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_5_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_6_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)   

    # def duplicate(self):
    #     picture_copy = ContentFile(self.image_1.read())
    #     new_picture_name = self.image_1.name.split("/")[-1]
    #     print(new_picture_name)
    #     self.image_1_big.save(new_picture_name, picture_copy)
    #     #super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Image 1
        if new_name(self.image_1, '_1croc')!=None: self.image_1 = make_round_image(self.image_1, '_1croc')
        if new_name(self.image_1_big, '_1big')!=None: self.image_1_big.name = new_name(self.image_1_big, '_1big')
        # Image 2
        if new_name(self.image_2, '_2croc')!=None: self.image_2 = make_round_image(self.image_2, '_2croc')
        if new_name(self.image_2_big, '_2big')!=None: self.image_2_big.name = new_name(self.image_2_big, '_2big')
        # Image 3
        try:
            if new_name(self.image_3, '_3croc')!=None: self.image_3 = make_round_image(self.image_3, '_3croc')
            if new_name(self.image_3_big, '_3big')!=None: self.image_3_big.name = new_name(self.image_3_big, '_3big')
        except:
            print("No image found 3")
        # Image 4
        try:         
            if new_name(self.image_4, '_4croc')!=None: self.image_4 = make_round_image(self.image_4, '_4croc')
            if new_name(self.image_4_big, '_4big')!=None: self.image_4_big.name = new_name(self.image_4_big, '_4big')
        except:
            print("No image found 4")
        # Image 5
        try:           
            if new_name(self.image_5, '_5croc')!=None: self.image_5 = make_tall_image(self.image_5, '_5croc')
            if new_name(self.image_5_big, '_5big')!=None: self.image_5_big.name = new_name(self.image_5_big, '_5big')
        except:
            print("No image found 5")
        # Image 6
        try:    
            if new_name(self.image_6, '_6croc')!=None: self.image_6 = make_tall_image(self.image_6, '_6croc')
            if new_name(self.image_6_big, '_6big')!=None: self.image_6_big.name = new_name(self.image_6_big, '_6big')
        except:
            print("No image found 6")
            
        super().save(*args, **kwargs)
    image_1.verbose_name = "Small Image 1"
    image_2.verbose_name = "Small Image 2"
    image_3.verbose_name = "Small Image 3"
    image_4.verbose_name = "Small Image 4"
    image_5.verbose_name = "Big Image 5"
    image_6.verbose_name = "Big Image 6"
    image_1_big.verbose_name = "Small Image 1 Complete"
    image_2_big.verbose_name = "Small Image 2 Complete"
    image_3_big.verbose_name = "Small Image 3 Complete"
    image_4_big.verbose_name = "Small Image 4 Complete"
    image_5_big.verbose_name = "Big Image 5 Complete"
    image_6_big.verbose_name = "Big Image 6 Complete"

    def image_tag(self):
        #NO ESTA MOSTRANDO CUANDO AUN NO SE GUARDA EL OBJETO
        return mark_safe('<img src="%s" />' % '/static/img/plantillas_pagina_web.jpg')
    image_tag.short_description = 'Image Tag'
    image_tag.allow_tags = True

    def image_tag_1(self):
        return mark_safe('<img src="%s" />' % self.image_1.url)
    def image_tag_2(self):
        return mark_safe('<img src="%s" />' % self.image_2.url)
    try:
        def image_tag_3(self):
            return mark_safe('<img src="%s" />' % self.image_3.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_4(self):
            return mark_safe('<img src="%s" />' % self.image_4.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_5(self):
            return mark_safe('<img src="%s" />' % self.image_5.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_6(self):
            return mark_safe('<img src="%s" />' % self.image_6.url)
    except:
        print("Doesn't exist")

class CoronaWars(models.Model):
    plantillas = [("A", "Model A"),
                ("B", "Model B"),
                ("C", "Model C")]
    select_plantilla = models.CharField(max_length=2, 
                                        choices=plantillas,
                                        default="B",)
    image_1 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)                                   
    image_2 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)                                   
    image_3 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)     
    image_3.help_text = "Only necessary for models A y B"                              
    image_4 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_4.help_text = "Only necessary for model B"                                  
    image_5 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_5.help_text = "Only necessary for models B y C"                               
    image_6 = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)   
    image_6.help_text = "Only necessary for model C"
    image_1_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)
    image_2_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_3_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_4_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_5_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  
    image_6_big = models.ImageField(upload_to='pics', storage=OverwriteStorage(), null=True, blank=True)  

    def save(self, *args, **kwargs):
        # Image 1
        if new_name(self.image_1, '_1croc')!=None: self.image_1 = make_round_image(self.image_1, '_1croc')
        if new_name(self.image_1_big, '_1big')!=None: self.image_1_big.name = new_name(self.image_1_big, '_1big')
        # Image 2
        if new_name(self.image_2, '_2croc')!=None: self.image_2 = make_round_image(self.image_2, '_2croc')
        if new_name(self.image_2_big, '_2big')!=None: self.image_2_big.name = new_name(self.image_2_big, '_2big')
        # Image 3
        try:
            if new_name(self.image_3, '_3croc')!=None: self.image_3 = make_round_image(self.image_3, '_3croc')
            if new_name(self.image_3_big, '_3big')!=None: self.image_3_big.name = new_name(self.image_3_big, '_3big')
        except:
            print("No image found 3")
        # Image 4
        try:         
            if new_name(self.image_4, '_4croc')!=None: self.image_4 = make_round_image(self.image_4, '_4croc')
            if new_name(self.image_4_big, '_4big')!=None: self.image_4_big.name = new_name(self.image_4_big, '_4big')
        except:
            print("No image found 4")
        # Image 5
        try:           
            if new_name(self.image_5, '_5croc')!=None: self.image_5 = make_tall_image(self.image_5, '_5croc')
            if new_name(self.image_5_big, '_5big')!=None: self.image_5_big.name = new_name(self.image_5_big, '_5big')
        except:
            print("No image found 5")
        # Image 6
        try:    
            if new_name(self.image_6, '_6croc')!=None: self.image_6 = make_tall_image(self.image_6, '_6croc')
            if new_name(self.image_6_big, '_6big')!=None: self.image_6_big.name = new_name(self.image_6_big, '_6big')
        except:
            print("No image found 6")
        super().save(*args, **kwargs)
    image_1.verbose_name = "Small Image 1"
    image_2.verbose_name = "Small Image 2"
    image_3.verbose_name = "Small Image 3"
    image_4.verbose_name = "Small Image 4"
    image_5.verbose_name = "Big Image 5"
    image_6.verbose_name = "Big Image 6"
    image_1_big.verbose_name = "Small Image 1 Complete"
    image_2_big.verbose_name = "Small Image 2 Complete"
    image_3_big.verbose_name = "Small Image 3 Complete"
    image_4_big.verbose_name = "Small Image 4 Complete"
    image_5_big.verbose_name = "Big Image 5 Complete"
    image_6_big.verbose_name = "Big Image 6 Complete"

    def image_tag(self):
        #NO ESTA MOSTRANDO CUANDO AUN NO SE GUARDA EL OBJETO
        return mark_safe('<img src="%s" />' % '/static/img/plantillas_pagina_web.jpg')
    image_tag.short_description = 'Image Tag'
    image_tag.allow_tags = True

    def image_tag_1(self):
        return mark_safe('<img src="%s" />' % self.image_1.url)
    def image_tag_2(self):
        return mark_safe('<img src="%s" />' % self.image_2.url)
    try:
        def image_tag_3(self):
            return mark_safe('<img src="%s" />' % self.image_3.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_4(self):
            return mark_safe('<img src="%s" />' % self.image_4.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_5(self):
            return mark_safe('<img src="%s" />' % self.image_5.url)
    except:
        print("Doesn't exist")
    try:
        def image_tag_6(self):
            return mark_safe('<img src="%s" />' % self.image_6.url)
    except:
        print("Doesn't exist")
        