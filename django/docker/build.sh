if %mode == 'development'
then
    bash migration.sh
end

if $mode == 'development'
then
    python manage.py runserver 0.0.0.0:8000
end