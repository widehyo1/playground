from django.db import models

class Post(models.Model):
    title = models.CharField("post title", max_length=100)
    content = models.TextField("post content")
    thumbnail = models.ImageField("thumbnail image", upload_to="post", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("comment content")

    def __str__(self):
        return f"comment of {self.post.title}: (ID: {self.id})"

    def __repr__(self):
        return f"<Comment ({self.id} of {self.post.id})>"
