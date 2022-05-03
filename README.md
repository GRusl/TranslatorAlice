# [Yandex Lyceum] Translator Alice

_Alice's skill for translating words_

You can deploy this app yourself to Heroku to play with

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Preparation

### Registering alice's skill

1. Register in Yandex or log in if you are already registered
2. Follow the link https://dialogs.yandex.ru/developer/
3. Click **создать диалог**
4. Select an option **Навык в Алисе**
5. Fill in **"активационное имя"** 
_(By this phrase, Alice will call your skill)_
6. Fill in the fields by specifying the link in the field **"Webhook URL"**
_(We will get it a little later)_

### Getting a token for the translator api

1. Log in or register on the service https://rapidapi.com
2. Subscribe to https://rapidapi.com/translated/api/mymemory-translation-memory/
3. Copy the received token

## Launch

### Local

Download the code
```
https://github.com/GRusl/TranslatorAlice
```

Installing dependencies
```
pip install -r requirements.txt
```

Creating a virtual environment
```
echo > .env 'TOKEN="your-token"' 
```

Starting the server
```
python app.py 
```

Great, everything works. But I think it's not hard to guess that 
we won't be able to specify a local address in the **"Webhook URL"** field.

Let's fix it!


### ngrok

Fortunately, there are services that organize a virtual tunnel from the 
Internet to your local computer. One of them is **ngrok**

Its important feature: ngrok has a free plan, but even this limited version is enough 
for our purposes. First you need to register and log in on the service's 
[website](https://ngrok.com)

1. You need to download the executable file of the application 
for the desired operating system from the [download page](https://ngrok.com/download)
2. Unpack the archive and in the terminal window go to the folder 
with the unpacked utility
3. Copy the command from the Setup & Installation page to configure ngrok 
to work with your account and run it in the terminal
<br>It looks like this: `ngrok authtoken 25srTxReQIIwsPMX67ZiY1E5TMH_7KbpfVGLcg9rRDd2hwfk9`
4. Now let's launch our application and execute it in the terminal: `ngrok http 5000`

Everything works! We will get our address from the console and order 
it in the appropriate skill field

### Heroku

A more advanced method that (when using paid plans) is suitable for "combat" 
deployment of an application on the Internet (deployment) is renting containers 
for applications on one of the many services that provide such services.

1. Register on Heroku. Then create a new application at https://dashboard.heroku.com/apps
2. Come up with a name for the application and choose a location
3. We will connect GitHub to Heroku and select the necessary repository, 
and then the branch from which we will take the code for placement. 
This can be done automatically or manually
4. If automatic code placement is not enabled, click on the **Deploy branch** button
5. We got our address app_name.herokuapp.com!

| :exclamation:  Don't forget to specify the environment variables |
|------------------------------------------------------------------|

## Testing

Now that we have specified the address in the **"Webhook URL"** field, 
we can proceed to testing

Go to the **Тестирование** tab and check how the skill works
