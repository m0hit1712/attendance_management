from django.db import models

# Create your models here.
class SubjectModel(models.Model):
        name = models.CharField(max_length=50)

class ClassModel(models.Model):
        class_name = models.CharField(max_length=100)
        subject_model = models.ManyToManyField(SubjectModel)

class StudentInformationModel(models.Model):
        full_name = models.CharField(max_length=200)
        contact_no = models.CharField(max_length=20)

class StudentModel(models.Model):
        student_info = models.OneToOneField(StudentInformationModel, on_delete=models.CASCADE)
        class_model = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
        username = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        email =  models.CharField(max_length=200)

class TeacherInfomationModel(models.Model):
        full_name = models.CharField(max_length=200)
        contact_no = models.CharField(max_length=20)

class TeacherModel(models.Model):
        teacher_info = models.OneToOneField(TeacherInfomationModel, on_delete=models.CASCADE)
        subject_id_array = models.CharField(max_length=100)
        class_model = models.ManyToManyField(ClassModel)

class AttendanceModel(models.Model):
        student_id = models.IntegerField(null=False)
        status = models.BooleanField(default=False)
        date = models.DateTimeField()
        class_id = models.IntegerField(null=False)
        subject_id = models.IntegerField(null=False)

class AdminModel(models.Model):
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        email = models.CharField(max_length=200)

class TeacherDocumentModel(models.Model):
        document_name = models.CharField(max_length=50)
        document_url = models.CharField(max_length=2000)
        teacher_model = models.ForeignKey(TeacherInfomationModel, on_delete=models.CASCADE)

class StudentDocumentModel(models.Model):
        document_name = models.CharField(max_length=50)
        document_url = models.CharField(max_length=2000)
        student_models = models.ForeignKey(StudentInformationModel, on_delete=models.CASCADE)

