import  xadmin
from .models import *
from xadmin.views.website import LoginView
from xadmin.views import CommAdminView
# # Register your models here.
class LoginViewAdmin(LoginView):
    title = '学生信息管理系统'
class GlobalSetting(CommAdminView):
    site_title = '学生信息管理系统'
    site_footer = 'sight-code'
    menu_style = 'accordion'
class CourseAdmin(object):
     list_display = ('course_name', 'course_level', 'course_class', 'course_counts', 'course_date')
#
# # class GradeAdmin(object):
# #     list_display = ('grade_course', 'grade_name', 'grade_count',)
# #
# # class ClassAdmin(object):
# #     list_display = ('class_grade', 'class_name',)
# #
class StudentsAdmin(object):
     list_display = ('name', 'sex', 'age', 'course_choice',)
# #
class TeachersAdmin(object):
     list_display = ('teacher_name',)
#    style_fields = {'teach_class':'checkbox-inline'}
# #
xadmin.site.register(Course, CourseAdmin)
# # xadmin.site.register(Grade, GradeAdmin)
# # xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(Students, StudentsAdmin)
xadmin.site.register(Teachers, TeachersAdmin)
xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(CommAdminView, GlobalSetting)