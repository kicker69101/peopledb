from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Address(models.Model):
    Person = models.ForeignKey('Person')
    Street = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Zip = models.CharField(max_length=20)
    State = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)

    def __unicode__(self):
        return "(%s) %s" % (self.Person.name, self.Street)


class LikesDislike(models.Model):
    Person = models.ManyToManyField('Person')
    LIKE = 'like'
    DISLIKE = 'dislike'
    DIRECTIONS = (
        (LIKE, 'like'),
        (DISLIKE, 'dislike'),
    )
    direction = models.CharField(max_length=20, choices=DIRECTIONS)
    subject = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s (%s)" % (self.subject, self.direction)


class PersonNotes(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    Person = models.ForeignKey('Person')
    note = models.TextField()

    def __unicode__(self):
        return "%s (%s)" % (self.Person.name, self.timestamp)


class RelationType(models.Model):
    name = models.CharField(max_length=255)
    to_name = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Relationship(models.Model):
    to_person = models.ForeignKey('Person')
    from_person = models.ForeignKey('Person')
    RelationType = models.ForeignKey('RelationType')

    def __unicode__(self):
        return "%s -> %s (%s)" % (self.to_person.name, self.from_person.name, RelationType.name)
