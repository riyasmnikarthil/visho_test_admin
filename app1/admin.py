from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import Category, Report, Item

def make_published(modeladmin, request, queryset):
    	rows_updated = queryset.update(is_active='0')
	if rows_updated == 1:
	    message_bit = "1 story was"
	else:
	    message_bit = "%s stories were" % rows_updated
	modeladmin.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = "Mark selected stories as published"

def make_published1(modeladmin, request, queryset):
    queryset.update(is_active='1')
make_published1.short_description = "Mark selected stories as published1"


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id','name','is_active','commission_rate']
	actions = [make_published,make_published1]
	ordering = ['name']
	actions_on_top = False
	actions_on_bottom = True
	actions_selection_counter = True
	#exclude = ('id',) # remove edit option
	readonly_fields = ('id',)
	list_display_links = ('name',)
	list_filter = ('name',)
	list_per_page = 5
	search_fields = ('name','is_active')

class ReportAdmin(admin.ModelAdmin):
	list_display=['id', 'item','object_link']
	exclude = ['is_deleted']
	list_select_related = True
	def object_link(self, obj):
		ct = obj.item
		url = reverse('admin:%s_%s_change' % ('app1', 'item'), args=(ct.id,)) 
		return '<a href="%s">%s</a>' % (url, ct.title)
	object_link.allow_tags = True

admin.site.register(Category, AuthorAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Item)
