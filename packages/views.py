from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PackageForm
from .models import Package


def home(request):
    return render(request, "packages/home.html")


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account was created successfully.")
            return redirect("package_list")
    else:
        form = UserCreationForm()
    return render(request, "packages/signup.html", {"form": form})


@login_required
def package_list(request):
    packages = Package.objects.all().order_by("-id")
    return render(request, "packages/package_list.html", {"packages": packages})


@login_required
def add_package(request):
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Package added successfully.")
            return redirect("package_list")
    else:
        form = PackageForm()
    return render(request, "packages/package_form.html", {"form": form, "page_title": "Add Package"})


@login_required
def edit_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == "POST":
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, "Package updated successfully.")
            return redirect("package_list")
    else:
        form = PackageForm(instance=package)
    return render(request, "packages/package_form.html", {"form": form, "page_title": "Edit Package"})


@login_required
def delete_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == "POST":
        package.delete()
        messages.success(request, "Package deleted successfully.")
        return redirect("package_list")
    return render(request, "packages/package_confirm_delete.html", {"package": package})
