from django.db import models


class Review(models.Model):
    movie_title = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.rating}/10"


class MovieReview(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    STATUS_CHOICES = [
        ('positive', 'Положительный'),
        ('negative', 'Отрицательный'),
    ]

    movie_title = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.movie_title} - {self.rating} ({self.status})"

