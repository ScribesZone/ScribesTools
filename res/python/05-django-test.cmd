@SET TMPSUFFIX=django-test
mkdir tmp-%TMPSUFFIX%
cd tmp-%TMPSUFFIX%
call workon ScribeEnv
call django-admin --version
call django-admin startproject testsite
cd testsite
python manage.py --version
python manage.py makemigrations
python manage.py migrate
rem unix: add " " around echo
echo from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@nowhere.org', 'admin') | python manage.py shell
python manage.py check
rem unix: remove start and add & at the end
start python manage.py runserver
echo Open a browser at http://localhost:8000/admin/ to test django
echo    login:admin
echo    password:admin
pause
cd ..\..
echo Close the shell windows with the server running
pause
rmdir /s /q tmp-%TMPSUFFIX%
