Кому интересно запустить БД в контейнере. В репозитории находится 2 файла:
- `docker-compose.yaml` - содержит описание сервиса, берет переменные из `.env` автоматически. Запускается командой `docker compose up -d`, при условии, что у вас установлен docker. После успешного запуска БД будет доступна через `localhost:5432/test`
- `.env` - содержит значения переменных окружения для контейнера. Редактировать нужно его.

Для установки `docker` на windows - [windows-install](https://docs.docker.com/desktop/install/windows-install/)

Может понадобиться настройка [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) - [Документация](https://docs.docker.com/desktop/wsl/)