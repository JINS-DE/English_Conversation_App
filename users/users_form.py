from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Users

class UserCreateForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2', 'level','profile_img')  # 필요한 필드 추가

class UserModifyForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'level', 'profile_img')
