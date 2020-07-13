from django.db import models

safety_level = (
    ('SAFE', 'Safe'),
    ('EUCLID', 'Euclid'),
    ('KETER', 'Keter'),
)

class Monster(models.Model):
    monster_name = models.CharField(max_length=50)
    behaviour_type = models.CharField(choices=safety_level, max_length=6)
    image = models.ImageField(upload_to ='', default='/default0.png')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.monster_name

class Location(models.Model):
    name = models.CharField(max_length=50)
    monsters = models.ManyToManyField(Monster)

    def __str__(self):
        return self.name