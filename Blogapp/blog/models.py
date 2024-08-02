from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False, blank=True) # Null değerini öcelikle True veriyoruz ki önce veri tababnına boş şekilde kaydedilebilsin sonra biz elle kaydettikten sonra Null=False yapıyoruz ki kaydedilmeden geçilmesin.

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs", null=True, blank=True)
    story = CKEditor5Field('Text', config_name='extends')
    published_date= models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, db_index=True, editable=False) # bu SEO açısından iyidir.  id yerine kursun tam adı ile url oluşturur.
    categories =models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(User, null=False, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering =["-published_date"]