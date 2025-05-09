from django.db import models

class Proctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Building(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    proctor = models.ForeignKey(Proctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    current_occupants = models.IntegerField(default=0)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.building.name} - {self.room_number}"

class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    student_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    year_of_study = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

class MaintenanceTeam(models.Model):
    team_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name

class ProblemReport(models.Model):
    STATUS_CHOICES = [('Open', 'Open'), ('InProgress', 'In Progress'), ('Closed', 'Closed')]

    proctor = models.ForeignKey(Proctor, on_delete=models.SET_NULL, null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    date_reported = models.DateField(auto_now_add=True)
    date_resolved = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    team = models.ForeignKey(MaintenanceTeam, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Issue in {self.building.name}, Room {self.room}"
