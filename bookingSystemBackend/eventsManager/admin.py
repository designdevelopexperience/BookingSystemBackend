from django.contrib import admin

from .models import Owner, Event, Client, Enrollment


class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 1


class EnrollmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event owner',               {'fields': ['owner']}),
        ('Event name',               {'fields': ['event_name']}),
        ('Event date',               {'fields': ['date']}),
        ('Capacity', {'fields': ['capacity']}),
    ]
    inlines = [EnrollmentInline]


admin.site.register(Owner)
admin.site.register(Event, EnrollmentAdmin)
admin.site.register(Client)
admin.site.register(Enrollment)