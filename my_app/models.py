from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # display the same name that you add in admin on admin's column
    def __str__(self):
        return '{}'.format(self.search)

    # define the column name on admin
    class Meta:
        verbose_name_plural = 'Searches'
