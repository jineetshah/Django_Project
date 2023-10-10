# Welcome to Temperature Alert Using uAgents library from fetch.ai

We are using this project to showcase how much we have learned about fetch.ai and how to use its functionlities.

# Working

you can start by first installing the dependencies by running the command
```
pip install -r requirements.txt
```

Then you must add the `.env`, you can refer to the `.env.template` for furthur details.

Then you can run the Django project by running:

```
python3 manage.py runserver 0.0.0.0:3000
```

Finally by going to this page
```
/playground/main/
```

you should be able to see the form where you will add your email and min-max temperature range.
select a city from the dropdown and boom its done.

click on submit and take a cup of coffee.

an agent will be deployed which will update you every hour if there is a temperature bounds violation.
