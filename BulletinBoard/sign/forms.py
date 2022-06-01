import redis
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import EmailField, CharField, Form, PasswordInput


class BaseRegisterForm(Form):
    error_messages = {
        "password_mismatch": "The two password fields didn’t match.",
    }

    username = CharField(label="username", max_length=150)
    email = EmailField(label="Email")

    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        fields = ("username",
                  "email",
                  "password1",
                  "password2",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as error:
                self.add_error("password2", error)


class BaseVerificationForm(UserCreationForm):
    data_from_redis = None

    error_messages = {
        "one-time-code_mismatch": "The one-time code field didn’t match.",
    }

    one_time_code = CharField(label="One-time code", max_length=6)

    class Meta:
        model = User
        fields = ("one_time_code",)

    def clean_one_time_code(self):
        red = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
        user_code = self.cleaned_data.get("one_time_code")
        self.data_from_redis = red.get(user_code)
        if not self.data_from_redis:
            raise ValidationError(
                self.error_messages["one-time-code_mismatch"],
                code="one-time-code_mismatch",
            )
        return user_code

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['username'] = 'bobby'
        return cleaned_data

    def clean_username(self):
        return 'bobby'

    def _post_clean(self):
        super()._post_clean()

        print('apsod')
        values = self.data_from_redis.split('\t')
        self.cleaned_data.setdefault('username', '')
        self.cleaned_data["username"] = values[0]
        self.cleaned_data.setdefault('email', '')
        self.cleaned_data["email"] = values[1]
        self.cleaned_data.setdefault('password1', '')
        self.cleaned_data["password1"] = values[2]
        self.cleaned_data.setdefault('password2', '')
        self.cleaned_data["password2"] = values[2]
        print('bab')

        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)
        print('fuckasd')

    def save(self, commit=True):
        print('before_save')
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
