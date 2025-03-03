from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name_plural = 'Tags'

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name_plural = 'Authors'

class Posts(models.Model):
    title = models.CharField(max_length=30)
    excerpt = models.CharField(max_length=200)
    img_name = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Post Details'

class comments(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=250)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.user_name
    class Meta:
        verbose_name_plural = 'Comments'