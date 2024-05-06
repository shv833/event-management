# event-management

## Requirements for prod mode
- Docker
- Make

## Requirements for dev mode
- Docker
- Make
- Python
- Node.js

## Getting started with Windows 10/11

```
winget install ezwinports.make
```

```
git clone https://github.com/shv833/event-management.git
```

```
cd .\event-management
```

## Configure .env.dev or .env.prod for email notification
- Configure your email smtp
- Update env files with next info
```
EMAIL_USER=<your_email@gmail.com>
EMAIL_PASS=<your api token for email>
EMAIL_SENDER=<your_email@gmail.com>
```

## Running tests
```
docker exec -it event-management-back-1 /bin/sh -c "cd /usr/src/backend/ && python manage.py test"
```

## Running in prod mode
```
make prod
```
or for clean run(rebuild images and reinstall packages)
```
make cprod
```

## Running in dev mode
```
make dev
```
or for clean run(rebuild images and reinstall packages)
```
make cdev
```

## How to test app manually

1. Once an app has started, it created 5 test simple users, 10 test events and one superuser
2. Credentials for superuser are next ```'admin@example.com', 'admin'```(also you can check/change it in ```.\backend\entrypoint.sh```)
3. Credentials for simple users are generated in next way ```
email=f'user{i + 1}@example.com',
password='password',
``` where `i` starts from `0`(also you can check/change it in ```.\backend\backend\management\commands\create_data.py```)
4. Visit swagger for checking available endpoints [`http://localhost:8000/swagger`](http://localhost:8000/swagger)
5. Some endpoints need authorization so please retrieve access token first here [`http://localhost:8000/api/v1/users/token/`](http://localhost:8000/api/v1/users/token/) or in swagger and then pass it to swagger `Authorize` button
6. If you want to test endpoints not in swagger, but just using browser - firstly install extension `Modheader` for browser and add `Authorization` header with next value `Bearer <access_token>`
7. Feel free to test it:)

## Short description of workflow
- Users can be signed up with endpoint `/api/v1/users/register/`
- All users(authorized and non-authorized) can access next endpoints

|endpoint|description|
|--------|-----------|
|`/api/v1/events/`|list of all events(you can also test here search and filtering events)|
|`/api/v1/events/{id}/`|event's detail|
|`/api/v1/users/register/`|sign up|
|`/api/v1/users/token/`|retrieve access and refresh jwt tokens|
|`/api/v1/users/token/refresh/`|refresh access token|

- Next endpoints are only for authorized users

|endpoint|description|
|--------|-----------|
|`/api/v1/users/events/`|list signed in user's events where he/she is an attendee|
|`/api/v1/events/create/`|create event|
|`/api/v1/events/{id}/delete/`|delete event(if you are admin or event owner)|
|`/api/v1/events/{id}/update/`|put/patch event(if you are admin or event owner)|
|`/api/v1/events/{id}/attend/`|register for an event(once user did it, he/she receives an email notification about it)|
|`/api/v1/events/{id}/unattend/`|unregister from an event(once user did it, he/she receives an email notification about it )|

## Terraform `healthcheck`

```json
"healthCheck": {
    "command": [
        "CMD-SHELL",
        "curl --fail http://localhost:8000/api/v1/events/ || exit 1",
        "curl --fail http://localhost:3000/ || exit 1"
    ],
    "interval": 30,
    "retries": 3,
    "timeout": 5
}
```

## Environment variables
| Environment variables                  | Default Value                                 | Description                                                            |
|----------------------------------------|-----------------------------------------------|------------------------------------------------------------------------|