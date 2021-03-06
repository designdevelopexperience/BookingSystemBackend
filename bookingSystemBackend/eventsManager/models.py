from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, related_name='events', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    capacity = models.IntegerField()

    def __str__(self):
        return self.event_name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, related_name="enrollments", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name="clients", on_delete=models.CASCADE)

    def __str__(self):
        return self.client.first_name + " " + self.client.last_name



