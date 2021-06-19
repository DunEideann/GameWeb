from django.contrib import admin
from django.utils.html import format_html
from .models import Info_Home
from .models import News
from .models import Developer_Team_Information


from .models import SoulAndSpirit
class SoulAndSpiritAdmin(admin.ModelAdmin):

    readonly_fields = ('image_tag', 'image_tag_1', 'image_tag_2', 'image_tag_3', 'image_tag_4', 'image_tag_5', 'image_tag_6')
    fields = ( 'image_tag', 'select_plantilla',
            'image_1', 'image_1_big', 'image_tag_1',
            'image_2', 'image_2_big', 'image_tag_2',
            'image_3', 'image_3_big', 'image_tag_3',
            'image_4', 'image_4_big', 'image_tag_4',
            'image_5', 'image_5_big', 'image_tag_5',
            "image_6", 'image_6_big', 'image_tag_6')
    
from .models import CoronaWars
class CoronaWarsAdmin(admin.ModelAdmin):

    readonly_fields = ('image_tag', 'image_tag_1', 'image_tag_2', 'image_tag_3', 'image_tag_4', 'image_tag_5', 'image_tag_6')
    fields = ( 'image_tag', 'select_plantilla',
            'image_1', 'image_1_big', 'image_tag_1',
            'image_2', 'image_2_big', 'image_tag_2',
            'image_3', 'image_3_big', 'image_tag_3',
            'image_4', 'image_4_big', 'image_tag_4',
            'image_5', 'image_5_big', 'image_tag_5',
            "image_6", 'image_6_big', 'image_tag_6')
    


class NewsAdmin(admin.ModelAdmin):

    list_display = ('news_headline', 'news_date', 'news_auto_date')
    readonly_fields = ('news_example', 'big_news_example')
    fields = ('news_example', 'news_date',
            'news_headline', 'news_body', 'news_image',
            'big_news_example', 'news_title_big', 'news_subtitle_big',
            'news_body_big', 'news_image_big')

admin.site.register(CoronaWars, CoronaWarsAdmin)
admin.site.register(SoulAndSpirit, SoulAndSpiritAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Info_Home)
admin.site.register(Developer_Team_Information)