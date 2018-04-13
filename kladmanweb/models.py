# -*- coding: utf-8 -*-
from django.db import models


class KladMan(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256, blank=True, null=True, default=None)

    def __str__(self):
        return ('' if self.username is None else self.username) + ' id: ' + str(self.id)

    def return_username(self):
        return self.username

    return_username.short_description = 'Юзернейм'

    def return_id(self):
        return str(self.id)

    return_id.short_description = 'id'


class GeoTag(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, blank=True, null=True, default=None)
    KladMan = models.ForeignKey(KladMan, blank=True, null=True, default=None)
    longitude = models.FloatField(blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)
    height = models.FloatField(blank=True, null=True, default=None)
    hash = models.CharField(max_length=256)

    def __str__(self):
        return ('' if self.title is None else self.title) + ' id: ' + str(self.id)

    def return_hash(self):
        return '<a href="https://asergey.me/kladman/data/?hash={0}">{0}</a>'.format(self.hash)

    return_hash.short_description = 'Hash'
    return_hash.allow_tags = True

    def return_longitude(self):
        return str(self.longitude)

    return_longitude.short_description = 'Долгота'

    def return_latitude(self):
        return str(self.latitude)

    return_latitude.short_description = 'Широта'

    def return_height(self):
        return '-' if self.height is None else str(self.height)

    return_height.short_description = 'Высота'

    def return_title(self):
        return '-' if self.title is None else self.title

    return_title.short_description = 'Название'

    def return_id(self):
        return str(self.id)

    return_id.short_description = 'id'
