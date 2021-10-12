from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from api.models.user import YaUser


class YaUserCreationForm(UserCreationForm):

    class Meta:
        model = YaUser
        fields = ('email',)


class YaUserChangeForm(UserChangeForm):

    class Meta:
        model = YaUser
        fields = ('email', 'role',)
