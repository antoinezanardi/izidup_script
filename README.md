# izidup

## What is it ?

**Izidup_script** is a minimal python script built to warn you if a domain is not up anymore or send unexpected HTTP status code.
By executing the script, all domains, API routes and any web adresses you provided to it will be tested.
If something is wrong with one of those (Can't connect to it or HTTP status code different to 200), the script can warn you with two differents ways: By **mail** or by a **Slack** app.

## Usage

After cloning the project, open **izidup.py**. In the first lines of the script, you will find some informations to provide such as the domains you want to test, your slack webhook URL, and more depending of what you want to do.

When it's all set, execute it manually or by a cronjobs and **you're ready to go**.
