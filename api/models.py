from django.db import models


class Admin(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    recent_login_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "admin"
