# ticket_manager_flask_api
ticket manager built using flask api

# SETUP
1. Checkout the main branch in your ide
2. create a .env - you can copy .envexample and fill with your secret key and postgres db details
3. in your terminal `run make install` -- ensure your are in your venv :)
4. then run `make migration setup` - this will setup your db for migrations and establish the connection is live
5. then run `make migration` - this will setup your tables based on the models
6. Finally, run `make apply migration` - this will apply the migration to your database

Next you can use the curl requests below to interact with the API (I was going to setup swagger to make it easier, but the yaml files are tedious with flask and somewhat time consuming)


# CURL requests if preffered to interact with endpoints -- replace <something here>

Add an event;
  
```
  curl --location --request POST 'http://127.0.0.1:5000/app/v1/events/add_event' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "event_5",
    "date": "21/01/2022",
    "number_of_tickets": 100
}'
  ```

Check an event status;


```
curl --location --request GET 'http://127.0.0.1:5000/app/v1/events/check_event/<event_id>'
```
  
Add tickets to exisitng event;

```
  curl --location --request GET 'http://127.0.0.1:5000/app/v1/events/check_event/2'
  ```

Redeem a ticket;
```
curl --location --request GET 'http://127.0.0.1:5000/app/v1/tickets/redeem/<ticket_number>'
```

Check ticket status;


```
curl --location --request GET 'http://127.0.0.1:5000/app/v1/tickets/check_ticket/<ticket_number>'
```
