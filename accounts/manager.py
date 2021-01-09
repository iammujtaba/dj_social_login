from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AccountsManager(BaseUserManager):

    def create_user(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValidationError(_('Email id is required for registration'))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,first_name,password,**other_fields):
        if not email:
            raise ValidationError(_("Email id is required for registration as a staff."))

        other_fields.setdefaults('is_staff',True)
        other_fields.setdefaults('is_superuser',True)
        other_fields.setdefaults('is_active',True)
        if not other_fields.get('is_staff'):
            raise ValidationError(_('Please mark this user as a staff.'))
        if not other_fields.get('is_superuser'):
            raise ValidationError(_('User need to be have superuser permissions'))
        
        return self.create_user(email,username,first_name,password,**other_fields)
