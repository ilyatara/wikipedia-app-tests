## QA.GURU: Дипломный проект (Mobile)

Проект содержит автотесты для мобильного приложения Wikipedia для Android.

### Используемые технологии

<p align="center">
  <code><img width="5%" title="Pycharm" src="images/logos/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logos/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logos/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/logos/requests.png"></code>
  <code><img width="5%" title="Appium" src="images/logos/appium.png"></code>
  <code><img width="5%" title="Selene" src="images/logos/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logos/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logos/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logos/jenkins.png"></code>
  <code><img width="5%" title="BrowserStack" src="images/logos/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logos/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/logos/tg.png"></code>
</p>

Автотесты написаны на Python с использованием Selene и Appium. Тесты запускаются в Jenkins, отчёт о запуске формируется с помощью Allure, уведомление с отчётом приходит в Telegram.

### Тестируемая функциональность

Поиск:

- Поиск статьи по точному заголовку
- Открытие статьи из результатов поиска

Туториал:

- Пропуск туториала
- Проверка содержимого на всех слайдах туториала



## Запуск тестов

Тесты могут запускаться локально (на реальном устройстве и на эмуляторе) и удалённо - в облачной платформе для тестирования <a href="https://browserstack.com">BrowserStack</a>.

Способ запуска определяется переменной окружения context. Допустимые варианты её значений - local_real, local_emulator и bstack. Значение по умолчанию - local_real. В зависимости от значения context для конфигурации проекта (в файле <code>project.py</code>) будет выбран файл <code>.env.{context}</code>. Примеры заполнения конфигурационных файлов находятся в корневой директории проекта с расширением <code>.example</code>.

### Локальный запуск на реальном устройстве

Перед запуском необходимо:
- заполнить файл <code>.env.local_real</code>
- подключить устройство по USB
- запустить Appium Server
- находясь в корневой директории проекта, выполнить в консоли команды:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=local_real pytest .
```

### Локальный запуск на эмуляторе

Перед запуском необходимо:
- заполнить файл <code>.env.local_emulator</code>
- запустить эмулятор через Android Studio AVD
- запустить Appium Server
- выполнить в консоли команды:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=local_emulator pytest .
```

### Удалённый запуск на BrowserStack

Перед запуском необходимо:
- зарегистрироваться на сайте https://browserstack.com/
- на странице https://app-live.browserstack.com/ выбрать девайс и платформу для тестирования

<img src="images/screenshots/bstack_devices.jpg" alt=""/>

- на странице https://app-automate.browserstack.com/dashboard/v2/builds/ скопировать username и access key

<img src="images/screenshots/bstack_credentials.jpg" alt=""/>

- заполнить файл <code>.env.bstack</code>
- выполнить в консоли команды:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=bstack pytest .
```

При необходимости можно заменить .apk-файл в корне проекта на приложение Wikipedia другой версии. Файл из корня проекта будет автоматически загружен на BrowserStack. Если файл с таким именем был загружен ранее, повторно загружаться он не будет.

### Параметры запуска

Параметры запуска, заданные в .env-файлах, можно переопределить с помощью соответствующей переменной окружения, например:

```
context=bstack device='Galaxy S20' platform_version=10.0 pytest .
```

При запуске через Jenkins параметры можно передать на странице "Собрать с параметрами":

<img src="images/screenshots/jenkins_parametrized_build.jpg" alt=""/>



## Отчёт о прохождении тестов

После тестового прогона формируется тестовый Allure-отчёт.

### Локальный запуск

Для просмотра отчёта необходимо выполнить команду

```
allure serve allure-results
```

### Запуск в Jenkins

В разделе "Послесборочные операции" необходимо добавить шаг "Allure Report", указав директорию "allure-results":

<img src="images/screenshots/jenkins_configuration_allure.jpg" alt=""/>

Просмотреть сформированный отчёт, можно нажав на любую из ссылок "Allure Report" на странице сборки:

<img src="images/screenshots/jenkins_allure_report.jpg" alt=""/>

### Логирование низкоуровневых шагов

При выполнении тестов логируются локаторы элементов и действия, которые были над ними произведены:

<img src="images/screenshots/allure_low_level_logging.jpg" alt=""/>

### Аттачменты

После выполнения тестов в разделе "Tear down" прикрепляются скриншот экрана, XML-код и видео, если тест запускался на BrowserStack:

<img src="images/screenshots/allure_attachments.jpg" alt=""/>

Пример видео:

https://github.com/ilyatara/wikipedia-app-tests/assets/135700131/7f349a2b-99d8-41d0-afcb-f3e06525037f



## Получение уведомления в Telegram

### Удалённый запуск через Jenkins

Чтобы после тестового прогона в Telegram пришло уведомление с его результатами, в разделе "Послесборочные операции" после шага "Allure-report" необходимо добавить шаг "Post build task":

<img src="images/screenshots/jenkins_configuration_notifications.jpg" alt=""/>

Скрипт для отправки уведомлений:

```
java "-DconfigFile=notifications/telegram.json" -jar ".notifications/allure-notifications-4.5.0.jar"
```

### Локальный запуск

Для отправки уведомлений в Telegram после локального запуска необходимо выполнить команды:

```
allure generate allure-results -o allure-report
java "-DconfigFile=./notifications/telegram.json" -jar "./notifications/allure-notifications-4.5.0.jar"
```

### Пример отчёта о выполнении тестов

Для получения результатов о тестировании используется телеграм-бот. В отчёте отображаются параметры запуска тестового комплекта, время прохождения тестов, а также ссылка на Allure-отчёт:

<img src="images/screenshots/telegram_notification.jpg" alt=""/>

