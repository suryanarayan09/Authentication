from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib import admin

User = get_user_model()

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm


# Register your models here.


class UserAdmin(BaseUserAdmin):
    # the forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # the fields to be used in displaying the user model.
    # these override the definition on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'phone', 'admin',)
    list_filter = ('staff', 'active', 'admin',)
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permission', {'fields': ('admin', 'staff', 'active',)}),

    )

    # add_fieldsets is not a standard NodeAdmin attribute, UserAdmin
    # overrides ger_fieldsets to use these attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')
        }),
    )

    search_fields = ('phone', 'name')
    ordering = ('phone', 'name')
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
