from django.contrib import admin
from .models import Category,video,watch_historys
# Register your models here.

class Categoryadmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)  

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'user', 'category', 'uploaded_at')  
    search_fields = ('video_name', 'user__username', 'category__name')  
    list_filter = ('category', 'user')  
    date_hierarchy = 'uploaded_at'  
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_name', 'History')  
    search_fields = ('user__username', 'video_name__video_name') 
    list_filter = ('History',) 
admin.site.register(Category, Categoryadmin)
admin.site.register(video, VideoAdmin)
admin.site.register(watch_historys, WatchHistoryAdmin)