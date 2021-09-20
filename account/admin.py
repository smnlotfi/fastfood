from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import MyUser
# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ['mobile','name','adress']
    search_fields = ['mobile']
    readonly_fields = ['created_at','last_login']
    filter_horizontal = ()
    list_filter = ['last_login']
    fieldsets = ()
    ordering =['mobile']
    add_fieldsets = (
        (None,{
            'classes':'wide',
            'fields':('mobile','name','adress')
        }),
    )
admin.site.register(MyUser,MyUserAdmin)
