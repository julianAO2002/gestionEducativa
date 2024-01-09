from django.contrib import admin
from .models import Course, Registration, Attendance, Mark


class CourseAdmin(admin.ModelAdmin):
     list_display = ("name", "teacher", "class_quantity")
     list_filter = ("teacher",)
admin.site.register(Course, CourseAdmin)

class RegistrationAdmin(admin.ModelAdmin):
     list_display = ("course", "student", "enabled", "status")
     list_filter = ("course", "student", "enabled", "status")
admin.site.register(Registration, RegistrationAdmin)

class AttendanceAdmin(admin.ModelAdmin):
     list_display = ("course", "student", "date", "present")
     list_filter = ("course", "student", "date", "present")
admin.site.register(Attendance, AttendanceAdmin)

class MarkAdmin(admin.ModelAdmin):
     list_display = ("course", "student", "mark_1", "mark_2", "mark_3", "average")
     list_filter = ("course",)
admin.site.register(Mark, MarkAdmin)     

