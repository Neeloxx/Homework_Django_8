from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.FloatField(default=0.0)

    def update_rating(self):
        author_articles_rating = self.post_set.all().aggregate(post_rating=Sum("post_rating"))['post_rating']
        author_comments_rating = self.user.comment_set.all().aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
        all_author_rating = Comment.objects.filter(post__author=self.id).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
        self.user_rating = author_articles_rating * 3 + author_comments_rating + all_author_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'



class Post(models.Model):
    news = "NEWS"
    article = "ARTI"

    TYPE = [
        (news, 'Новости'),
        (article, 'Статья')
    ]

    post_time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.FloatField(default=0.0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=TYPE, default=news)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.post_text[0:124]}...'

    def __str__(self):
        return f'Post: {self.title}, Text: {self.post_text[:20]}...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




class Comment(models.Model):
    comment_text = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()


