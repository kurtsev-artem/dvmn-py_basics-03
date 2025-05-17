import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

server = smtplib.SMTP_SSL('smtp.yandex.com', 465)

LOGIN = os.getenv('LOGIN')
TOKEN = os.getenv('TOKEN')


server.login(LOGIN, TOKEN)

letter = """From: %sender%
To: %to%
Subject: %subject%
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

url = "https://dvmn.org/profession-ref-program/kurtsev.artem/3zWhU/"
myname = "Artem"
friendname = "Igor"
sender = "marine-iguana@yandex.ru"
reciever  = "marine-iguana@yandex.ru"
subject = "Приглашение!"

letter = letter.replace("%website%",url).replace("%my_name%",myname).replace("%friend_name%",friendname).replace("%sender%",sender).replace("%to%",reciever).replace("%subject%",subject)

letter = letter.encode("UTF-8")

server.sendmail("marine-iguana@yandex.ru", "marine-iguana@yandex.ru", letter)
server.quit()

