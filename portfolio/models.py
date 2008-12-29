from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(blank=True, null=True)
    pull_quote = models.TextField(blank=True, null=True)
    short_description = models.TextField()
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category')
    skills = models.ManyToManyField('Skill')

    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': str(self.slug), })

class Skill(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.skill_detail', (), {'slug': str(self.slug), })

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.category_detail', (), {'slug': str(self.slug), })

class ProjectFile(models.Model):
    project = models.ForeignKey('Project')
    file = models.FileField(upload_to="project_file/%Y/%m/%d")
    desc = models.TextField()

    def __unicode__(self):
        return self.file.name

    def get_absolute_url(self):
        return self.file.url

class ProjectImage(models.Model):
    project = models.ForeignKey('Project')
    image = models.ImageField(upload_to="project_image/%Y/%m/%d")
    desc = models.TextField()

    def __unicode__(self):
        return self.image.name

    def get_absolute_url(self):
        return self.image.url
