from django.db import models
from django.utils.text import slugify
from datetime import date, timedelta


class Profile(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=True, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    field = models.CharField(max_length=100, null=True, blank=True)
    institutions = models.CharField(max_length=100, null=True, blank=True)

    # textaress
    biography = models.TextField(null=True, blank=True)
    early_life_education = models.TextField(null=True, blank=True)
    family_career = models.TextField(null=True, blank=True)
    field_work = models.TextField(null=True, blank=True)
    award_honors = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # images
    picture_1 = models.FileField(upload_to='profile_pictures', default='default-img.jpg')
    picture_2 = models.FileField(upload_to='profile_pictures', null=True, blank=True)
    picture_3 = models.FileField(upload_to='profile_pictures', null=True, blank=True)

    picture_1_text = models.CharField(max_length=255, null=True, blank=True)
    picture_2_text = models.CharField(max_length=255, null=True, blank=True)
    picture_3_text = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-date_created',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Profile, self).save(*args, **kwargs)

    def get_age(self):
        age = (date.today() - self.date_of_birth) // timedelta(days=365.2425)
        return age

    def __str__(self):
        return self.name