from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .forms import UserRegistrationForm, UserProfileForm, LoginForm, EditProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import UserProfile
# Create your views here.
def register(request):

	if request.method == 'POST':
		user_form = UserRegistrationForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			new_user = user_form.save(commit=False)
			new_profile = profile_form.save(commit=False)

			new_user.set_password(user_form.cleaned_data['password1'])
			new_user.save()

			new_profile.user = new_user
			new_profile.save()

			# login

			return HttpResponse("Success refister!")
	else:
		user_form = UserRegistrationForm()
		profile_form = UserProfileForm()


	return render(request, 'accounts/register.html', context={'user_form':user_form, 'profile_form': profile_form})


def login_view(request):
	if request.method == 'POST':
		login_form = LoginForm(data=request.POST)

		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])


			if user is not None:
				if user.is_active:
					login(request, user)

					return HttpResponse("Success login!")

				else:
					return HttpResponse("Account Terminated!")

			else:
				return HttpResponse("User Doesnt exist!")

	else:
		login_form = LoginForm()


	return render(request, 'accounts/login.html', context={'login_form': login_form})


def profile_view(request, username):

	user = get_object_or_404(User, username=username)

	follow = False
	try:
		if request.user.profile.following.get(user=user):
			follow = True
	except Exception as e:
		print(e)
	
	return render(request, 'accounts/profile_page.html', {'user': user, 'follow': follow})



def edit_profile_view(request, username):
	if request.method == 'POST':
		edit_form = EditProfileForm(data=request.POST)
		if edit_form.is_valid():
			cd = edit_form.cleaned_data
			user = request.user
			user.first_name = cd['first_name']
			user.last_name = cd['last_name']
			user.email = cd['email']
			user.username = cd['username']

			user.profile.mob_no = cd['mob_no']
			user.profile.save()

			user.save()

			return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': user.username}))

	else:
		edit_form = EditProfileForm()

	return render(request, 'accounts/edit_profile.html', {'edit_form':edit_form})
	


def follow_view(request, username):
	user_to_follow = get_object_or_404(User, username=username)
	current_user = request.user

	current_user.profile.following.add(user_to_follow.profile)

	current_user.save()

	return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': username}))




def unfollow_view(request, username):
	user_to_unfollow = get_object_or_404(User, username=username)
	current_user = request.user

	try:
		if current_user.profile.following.get(user=user_to_unfollow):
			current_user.profile.following.remove(user_to_unfollow.profile)
			current_user.save()
	except Exception as e:
		print(e)

	return HttpResponseRedirect(reverse_lazy('accounts:profile', kwargs={'username': username}))

