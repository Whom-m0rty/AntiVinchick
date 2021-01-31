# AntiVinchick

Ну эээ... 
Что бы запустить сие чудо:

```
python manage.py migrate
```

Что бы создать админа:

```
python manage.py createsuperuser
```

Что бы запустить сервер:
```
sudo cp admin.service /etc/system/systemd
sudo cp bot.service /etc/system/systemd

systecmtl start admin.service
systecmtl start bot.service
systecmtl enable admin.service
systecmtl enable bot.service
```

Что бы проверить статус бота:
```
systecmtl status bot.service
```

Что бы проверить статус админки:
```
systecmtl status admin.service
```

Что бы зайти на админку:
```
Переходите на url
http://<IP вашего сервера>:8000/admin
```
