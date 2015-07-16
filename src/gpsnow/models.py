# encoding=utf-8

from django.db import models

class Transponder(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "発信機"

    name = models.CharField("名前", max_length=20, unique=True)
    description = models.CharField("説明", max_length=100, blank=True)
    marker = models.ImageField("マーカー", upload_to="uploads/markers", blank=True)
    marker_disabled = models.ImageField("マーカー (無効時)", upload_to="uploads/markers", blank=True)

    def __str__(self):
        return "[{0}] {1}".format(self.name, self.description)


class Waypoint(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "位置情報"

    transponder = models.ForeignKey(Transponder)
    created = models.DateTimeField("時刻")
    latitude = models.DecimalField("緯度", max_digits=10, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField("軽度", max_digits=10, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return "[{0}] @{1} {2} {3}".format(self.transponder.name, self.created, self.latitude, self.longitude)


    @property
    def latitude_10(self):
        latitude = float(self.latitude)
        d = int(latitude / 100)
        m = latitude % 100
        return d + m / 60.0


    @property
    def longitude_10(self):
        longitude = float(self.longitude)
        d = int(longitude / 100)
        m = longitude % 100
        return d + m / 60.0
