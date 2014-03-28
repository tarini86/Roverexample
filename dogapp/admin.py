from django.contrib import admin
from dogapp.models import Person, Dog

class DogAdmin(admin.ModelAdmin):
	list_display = ('dogName', 'age', 'breed')
	search_fields = ('dogName', 'breed')

class PersonAdmin(admin.ModelAdmin):
	list_display = ('personName_text','personAge')
	search_fields = ('personName_text','personAge')
	
# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Dog, DogAdmin)
