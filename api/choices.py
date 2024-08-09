from django.db.models import TextChoices


class EmployeeStatuses(TextChoices):
    XODIM = 'XODIM'
    TALABA = 'TALABA'
    PROFESSOR = 'PROFESSOR'


class MessageStatuses(TextChoices):
    YANGI = 'YANGI'
    ESKI = 'ESKI'

