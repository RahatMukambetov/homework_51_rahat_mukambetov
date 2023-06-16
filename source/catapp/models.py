from django.db import models
import random


class Cat(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=1)
    hunger_level = models.IntegerField(default=40)
    happiness_level = models.IntegerField(default=40)
    is_sleeping = models.BooleanField(default=False)

    ANGRY = 'cat/angry.jpg'
    NORMAL = 'cat/normal.jpg'
    HAPPY = 'cat/happy.jpg'

    def __str__(self):
        return self.name

    def feed(self):
        if not self.is_sleeping and self.hunger_level < 100:
            self.hunger_level += 15
            self.happiness_level += 5
            if self.hunger_level > 100:
                self.happiness_level -= 30
                self.hunger_level = 100

    def play(self):
        if not self.is_sleeping and self.hunger_level < 100:
            self.hunger_level -= 10
            self.happiness_level += 15
            if self.hunger_level < 0:
                self.hunger_level = 0
            if random.randint(1, 3) == 1:
                self.happiness_level = 0

    def sleep(self):
        self.hunger_level -= 5
        self.happiness_level += 5
        self.is_sleeping = True
        if self.hunger_level < 0:
            self.hunger_level = 0

    def wake_up(self):
        self.is_sleeping = False

    def get_avatar_path(self):
        if self.happiness_level <= 30:
            return self.ANGRY
        elif self.happiness_level <= 70:
            return self.NORMAL
        else:
            return self.HAPPY
