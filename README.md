# ticket_manager_flask_api
ticket manager built using flask api




# CURL requests if preffered to interact with endpoints

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
curl --location --request GET 'http://127.0.0.1:5000/app/v1/events/check_event/2'

```

Add tickets to an exisitng event;


```
curl --location --request POST 'http://127.0.0.1:5000/app/v1/events/add_tickets/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "event": "event_5",
    "number_of_tickets": 50
}'
```

Check ticket status;


```
curl --location --request GET 'http://127.0.0.1:5000/app/v1/tickets/check_ticket/133299'
```
