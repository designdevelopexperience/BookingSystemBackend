from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    capacity = models.IntegerField()

    def __str__(self):
        return self.event_name


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Enrollment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_name + " " + self.client.first_name + " - " + self.client.last_name



