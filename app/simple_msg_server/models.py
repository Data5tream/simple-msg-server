from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class MsgForm(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=512)
    fields = models.JSONField()
    endpoint = models.UUIDField(auto_created=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class MsgEntry(models.Model):
    form = models.ForeignKey('MsgForm', on_delete=models.CASCADE, related_name='entries')
    content = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    read_by = models.ForeignKey('User', blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.id} - Answer to {self.form.name} ({self.form_id}) - {self.created}'
