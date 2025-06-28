from django.db import models

class StaffBase(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    diagnostic_reference = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def get_role(self):
        return "Manager"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end = models.DateField()

    def get_role(self):
        return "Intern"

