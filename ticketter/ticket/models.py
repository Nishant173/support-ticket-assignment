from django.db import models


DEPARTMENT_CHOICES = (
    ('DevOpsSupport', 'DevOpsSupport'),
    ('SomeSupport', 'SomeSupport'),
    ('SomeOtherSupport', 'SomeOtherSupport'),
)

CATEGORY_CHOICES = (
    ('Kubernetes deployments', 'Kubernetes deployments'),
    ('New CI/CD pipeline setup', 'New CI/CD pipeline setup'),
    ('Update CI/CD pipeline configuration', 'Update CI/CD pipeline configuration'),
    ('DevSecOps pipeline setup', 'DevSecOps pipeline setup'),
    ('CI/CD pipeline failure', 'CI/CD pipeline failure'),
    ('Docker and containers', 'Docker and containers'),
)

PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)


class Ticket(models.Model):
    department = models.CharField(verbose_name='Department name',
                                  choices=DEPARTMENT_CHOICES,
                                  default='DevOpsSupport',
                                  max_length=50)
    category = models.CharField(verbose_name='Category',
                                choices=CATEGORY_CHOICES,
                                default='Kubernetes deployments',
                                max_length=50)
    project_url = models.URLField(verbose_name='Project URL')
    subject = models.CharField(verbose_name='Subject', max_length=50)
    description = models.TextField(verbose_name='Description', max_length=250)
    username = models.CharField(verbose_name='Username', max_length=30)
    priority = models.CharField(verbose_name='Priority level',
                                choices=PRIORITY_CHOICES,
                                default='Low',
                                max_length=20)

    def __str__(self):
        return f"Username: {self.username} Subject: {self.subject}"