from django.db import models
# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length = 250)
    Surname = models.CharField(max_length = 250)
    Address = models.CharField(max_length = 250)
    Email = models.EmailField()

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.Email

from django.dispatch import receiver
from .signals import new_emp_create
from django.conf import settings
from django.core.mail import send_mail

@receiver(new_emp_create,sender = Employee)
def create_employee(**kwargs):
    Name = kwargs['Name']
    Surname = kwargs['Surname']
    Address = kwargs['Address']
    Email = kwargs['Email']
        
    a = f"Employee name is {Name} {Surname} address {Address} mail id {Email} added in our employee list."

    subject = 'New Employee Joined'
    message = f'''Dear Sir/Man,
                        Kindly note new Employee created and added in our Company Employee list.
                        
                    Please fnd the below details of Employee
                    Name = {Name} 
                    Surname = {Surname} 
                    Address = {Address} 
                    Email = {Email} 

                '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["vrbhandari1995@gmail.com"]      # vrbhandari1995@gmail.com

    send_mail( subject, message, email_from, recipient_list )
    print("To", recipient_list, "From", email_from, a)
    # print(a)










    