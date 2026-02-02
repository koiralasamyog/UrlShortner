from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random
import string


def home(request):
    short_url = None

    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)

        if form.is_valid():
            original_website = form.cleaned_data['original_url']

            chars = string.ascii_letters + string.digits
            random_chars = ''.join(random.choice(chars) for _ in range(6))

            while ShortURL.objects.filter(short_url=random_chars).exists():
                random_chars = ''.join(random.choice(chars) for _ in range(6))

            obj = ShortURL.objects.create(
                original_url=original_website,
                short_url=random_chars,
                time_date_created=datetime.now()
            )

            short_url = obj.short_url

    else:
        form = CreateNewShortURL()

    return render(request, 'home.html', {
        'form': form,
        'short_url': short_url
    })

def redirect_url(request, url):
    obj = get_object_or_404(ShortURL, short_url=url)
    return redirect(obj.original_url)
