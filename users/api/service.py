from django.contrib.auth.models import User


class UserService(object):
    @classmethod
    def get_user_by_username_or_email(cls, username_or_email):
        key = 'email__iexact' if '@' in username_or_email else 'username__iexact'
        if not User.objects.filter(**{key: username_or_email}).exists():
            return None
        return User.objects.get(**{key: username_or_email})

