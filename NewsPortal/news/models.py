from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRait = self.post_set.aggregate(postRating=Sum('rating'))
        pRait = 0
        pRait += postRait.get('postRating')

        commentRait = self.authorUser.comment_set.aggregate(commentRaiting=Sum('rating'))
        cRait = 0
        cRait += commentRait.get('commentRaiting')

        self.ratingAuthor = pRait*3 + cRait
        self.save()

    def __str__(self):
        return str(self.authorUser)
        # return str(self.ratingAuthor)

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, 'Новост'),
        (ARTICLE, "Статья")
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    # postCategory = models.ManyToManyField(Category, through="PostCategory")
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123]+'...'


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['dateCreation']

# class PostCategory(models.Model):
#     postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
#     categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.categoryThrough)




class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation=models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return str(self.commentPost)