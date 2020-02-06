from django.db import models

# Create your models here.
class Teachers(models.Model):
    teacher_name = models.CharField(verbose_name='教师姓名', max_length=50)
    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'
#
    def __str__(self):
        return self.teacher_name
class Course(models.Model):
    course_name = models.CharField(verbose_name='课程名称', max_length=50)
    LEVEL = (('一阶', 1), ('二阶', 2), ('三阶', 3), ('四阶', 4), ('五阶', 5), ('六阶', 6))
    course_level = models.CharField(choices=LEVEL, verbose_name='阶段', max_length=50)
    TIME = (('周五 18:00-20:00', '周五 18:00-20:00'), ('周六 13:00-14:30', '周六 13:00-14:30'),
            ('周六 18:30-20:00', '周六 18:30-20:00'), ('周日 13:00-14:30', '周日 13:00-14:30'),
            ('周日 15:15-16:45', '周日 15:15-16:45'), ('周日 18:00-19:30', '周日 18:00-19:30'))
    course_class = models.CharField(choices=TIME, verbose_name='上课时间', max_length=50)
    course_counts = models.IntegerField(verbose_name='总课时')
    course_date = models.DateField(verbose_name="开课时间")
    who_teach = models.ForeignKey(Teachers, verbose_name='教师', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

    def __str__(self):
        return self.course_name+self.course_level+self.course_class
# class Grade(models.Model):
#     grade_course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE, blank=True, null=True)
#     grade_name = models.CharField(verbose_name="阶段", max_length=50)
#     #date_grade = models.DateTimeField(verbose_name='开课时间')
#     grade_count = models.IntegerField(verbose_name='总课时')
#     class Meta:
#         verbose_name = '阶段信息'
#         verbose_name_plural = '阶段信息'
#
#     def __str__(self):
#         return self.grade_name
#
# class Class(models.Model):
#     #class_course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE, blank=True, null=True)
#     class_grade = models.ForeignKey(Grade, verbose_name='课程阶段', on_delete=models.CASCADE, blank=True, null=True)
#     class_name =  models.CharField(verbose_name="班级", max_length=50)
#     teach_class = models.ForeignKey('Teachers', verbose_name='教师', on_delete=models.CASCADE, blank=True, null=True)
#     class Meta:
#         verbose_name = '班级信息'
#         verbose_name_plural = '班级信息'
#
#     def __str__(self):
#         return self.class_name
class Students(models.Model):
    SEX = (('male', '男'), ('female', '女'),)
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄')
    tel = models.IntegerField(verbose_name='联系电话')
    remarks = models.TextField(verbose_name='备注', blank=True)
    course_choice = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    def __str__(self):
        return self.name


