from django.contrib import admin

from .models import Profile,Project,Language,Rating,Contact
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Rating)
admin.site.register(Contact)