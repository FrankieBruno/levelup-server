from django.db import models


class Event(models.Model):
    description = models.CharField(max_length=55)
    date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        "Gamer", related_name="gamer_events_attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
