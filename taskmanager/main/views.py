import os.path
import joblib
from django.contrib.sessions.backends import file
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm

model_path = os.path.join(os.path.dirname(file), 'model.pkl')

model = joblib.load(model_path)

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.rating = 5
            review.is_positive = True
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def classify_review(text):


    prediction = model.predict([text])[0]
    sentiment = 'positive' if prediction == 1 else 'negative'
    return sentiment


def review_view(request, sentiment=None):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['review_text']  
            rating = 5 if sentiment == 'positive' else 1
            Review.objects.create(movie_title=form.cleaned_data['movie_title'], review_text=text, rating=rating, 
                                   status=sentiment)
            return render(request, 'reviews/result.html', {'sentiment': sentiment})
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})