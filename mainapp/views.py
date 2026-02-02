# mainapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from .forms import CreateNewShortURL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.utils import timezone
from .utils import encode_base62
from .utils import generate_qr_code

@login_required
def home(request):
    short_url = None
    qr_code = None  # new

    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            custom_url = form.cleaned_data.get('custom_short_url')
            expiration = form.cleaned_data.get('expiration_date')

            if custom_url:
                if ShortURL.objects.filter(short_url=custom_url).exists():
                    form.add_error('custom_short_url', 'This short URL is already taken.')
                    return render(request, 'home.html', {'form': form, 'short_url': None})
                short_code = custom_url
                obj = ShortURL.objects.create(
                    original_url=original_website,
                    short_url=short_code,
                    creator=request.user,
                    time_date_created=timezone.now(),
                    expiration_date=expiration
                )
            else:
                temp_obj = ShortURL.objects.create(
                    original_url=original_website,
                    creator=request.user,
                    time_date_created=timezone.now(),
                    expiration_date=expiration
                )
                short_code = encode_base62(temp_obj.id)
                temp_obj.short_url = short_code
                temp_obj.save()
                obj = temp_obj

            short_url = obj.short_url
            qr_code = generate_qr_code(f"{request.scheme}://{request.get_host()}/s/{short_url}")

    else:
        form = CreateNewShortURL()

    return render(request, 'home.html', {'form': form, 'short_url': short_url, 'qr_code': qr_code})

def redirect_url(request, url):
    obj = get_object_or_404(ShortURL, short_url=url)

    now = timezone.now()
    if obj.expiration_date and now > obj.expiration_date:
        messages.error(request, "This short URL has expired.")
        return redirect('home')

    obj.click_count += 1
    obj.save()
    return redirect(obj.original_url)


@login_required
def all_urls(request):
    urls = ShortURL.objects.filter(creator=request.user).order_by('-time_date_created')
    return render(request, 'all_urls.html', {'urls': urls})

@login_required
def edit_url(request, url_id):
    url_obj = get_object_or_404(ShortURL, id=url_id, creator=request.user)

    if request.method == 'POST':
        form = CreateNewShortURL(request.POST, instance=url_obj)
        if form.is_valid():
            custom_url = form.cleaned_data.get('custom_short_url')
            
            # Check uniqueness if custom URL is changed
            if custom_url and ShortURL.objects.filter(short_url=custom_url).exclude(id=url_obj.id).exists():
                form.add_error('custom_short_url', 'This short URL is already taken.')
                return render(request, 'edit_url.html', {'form': form})

            obj = form.save(commit=False)

            # If no custom URL, regenerate Base62 from ID
            if not custom_url:
                obj.short_url = encode_base62(obj.id)

            obj.save()
            messages.success(request, "URL updated successfully!")
            return redirect('all_urls')
    else:
        form = CreateNewShortURL(instance=url_obj)

    return render(request, 'edit_url.html', {'form': form})


@login_required
def delete_url(request, url_id):
    url_obj = get_object_or_404(ShortURL, id=url_id, creator=request.user)
    if request.method == 'POST':
        url_obj.delete()
        messages.success(request, "URL deleted successfully!")
        return redirect('all_urls')
    return render(request, 'delete_url.html', {'url': url_obj})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
