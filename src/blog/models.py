from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import redirect

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
)
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField('Post Url',max_length=150, unique=True, blank=True, null=True)
    post_title = models.CharField(max_length=120)
    post_image = models.ImageField(default='blogpost_pics/default_blog_post.jpg', upload_to='blogpost_pics/')
    post_description = models.TextField(max_length=1000)
    publish_status = models.CharField(default='draft',max_length=15, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True) 
    
    class Meta: 
       ordering = ('-updated', ) 

    def __str__(self):
        return self.post_title
    
    def save(self, *args, **kwargs):
        
        # print(dir(self))
        # print(f"--------------------> {self.save}")
        self.slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return redirect('post_detail', slug=self.slug)
    
REACT_CHOICES = (
    ('noreact','No React'),
    ('like', 'Like'),
    ('dislike', 'Dislike'),
)



class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    react = models.CharField('',max_length=10,choices=REACT_CHOICES)

    class META:
        unique_together = ('post', 'user',)

    def __str__(self):
        return self.post.post_title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=100)

    def __str__(self):
        return self.user.username