from django.contrib import admin


# Register your models here.
from App.models import Grade, Student, Blog


class StudentInfo(admin.TabularInline):
    model = Student
    extra = 3


class StudentAdmin(admin.ModelAdmin):
    list_filter = ['s_name','s_grade']


class GradeAdmin(admin.ModelAdmin):

    def get_type(self):
        if self.g_type == 1:
            return 'python'
        elif self.g_type == 2:
            return 'html+'
        else:
            return 'other'
    get_type.short_description = '学科'
    # list_display = ['g_name','g_type','g_student_count']
    list_display = ['g_name',get_type,'g_student_count']
    list_per_page = 3
    list_filter = ['g_name','g_position']
    search_fields = ['g_name', 'g_position']
    ordering = ['g_student_count']
    fieldsets = (
        ("基本信息",{'fields':('g_name', 'g_position')}),
        ("其他信息", {"fields": ('g_student_count', 'g_type')})
    )
    inlines = [StudentInfo]


# admin.site.register(Grade, GradeAdmin)
# admin.site.register(Student, StudentAdmin)

class MyAdminSite(admin.AdminSite):
    site_header = "头"
    site_title = "标题"
    site_url = '/index/'


site = MyAdminSite()
site.register(Grade)
site.register(Student)
site.register(Blog)
