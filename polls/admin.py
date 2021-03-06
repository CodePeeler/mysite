from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [ 
	    ('Questions...', {'fields': ['question']}), 
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), 
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

#admin.site.register(Choice)
admin.site.register(Poll, PollAdmin)