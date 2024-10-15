from django import forms
from .models import MovieReview
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)

    def clean(self):
        cleaned_data = super().clean()
        review_text = cleaned_data.get("review_text")
        rating = cleaned_data.get("rating")

        if rating is not None:
            if rating >= 6:
                cleaned_data['status'] = 'positive'
            else:
                cleaned_data['status'] = 'negative'

        return cleaned_data
