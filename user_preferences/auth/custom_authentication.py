from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from user_preferences.models import User, Teacher, Student, Parents

class CustomAuthentication(ModelBackend):
    def authenticate(selt, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            
            if user.check_password(password):
                CustomAuthentication.if_first_time_set_up()

                user.groups.clear()
                if Teacher.objects.filter(abstract_user=user).exists():
                    if not user.groups.filter(name="Teacher").exists():
                        user.groups.add(Group.objects.get(name="Teacher"))
                if Parents.objects.filter(abstract_user=user).exists():
                    if not user.groups.filter(name="Parents").exists():
                        user.groups.add(Group.objects.get(name="Parents"))
                return user
            return None
        except User.DoesNotExist:
            return None



    @staticmethod
    def if_first_time_set_up():
        if not Group.objects.filter(name="Teacher").exists():
            Group.objects.create(name="Teacher")
        if not Group.objects.filter(name="Parents").exists():
            Group.objects.create(name="Parents")

        if not Permission.objects.filter(codename="is_teacher").exists():
            Permission.objects.create(
                codename="is_teacher",
                name="User is Teacher",
                content_type=ContentType.objects.get_for_model(User),
            )
        if not Permission.objects.filter(codename="is_parents").exists():
            Permission.objects.create(
                codename="is_parents",
                name="User is Parents",
                content_type=ContentType.objects.get_for_model(User),
            )

        if not Group.objects.get(name="Teacher").permissions.filter(codename="is_teacher").exists():
            Group.objects.get(name="Teacher").permissions.add(Permission.objects.get(codename="is_teacher"))
        if not Group.objects.get(name="Parents").permissions.filter(codename="is_parents").exists():
            Group.objects.get(name="Parents").permissions.add(Permission.objects.get(codename="is_parents"))