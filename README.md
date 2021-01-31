# AntiVinchick

Ну эээ... 
# Настройка токенов:
```
AntiVinchick/settings.py 

VK_BOT_TOKEN = 'dbec106482ef194b8231145c3d3b522437289b6bc4a92b30f7e750e74149c1477df806f191fb8c563d52c'
VK_GROUP_ID = '201924301'
NEED_TO_ACCESS = 5
```

# Что бы запустить сие чудо:

Накатываем миграции
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
