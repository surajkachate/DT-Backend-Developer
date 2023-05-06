# DT-Backend-Developer
Create API with GET, POST, PUT, DELETE methods in Python-Flask

TASK 1:

DT Backend Developer task 1 based on the below documentation:

Object Data Model of an event	
type: event
uid:18 (user id)
name: Name of the event
tagline: A proper tag-line for the event
schedule: (Date + time) Timestamp
description: String
files[image]: Image file (File upload)
moderator: A user who is going to host
category: Category of the event
sub_category: Sub category
rigor_rank: Integer value
attendees: Array of user Id's who is attending the event


Description of URL

Widget: Event
Request Type: GET
Base URL: /api/v3/app	
API Endpoint: /events?id=:event_id	
Description: Gets an event by its unique id

Widget: Event
Request Type: GET
Base URL: /api/v3/app	
API Endpoint: /events?type=latest&limit=5&page=1	
Payload		
Description: Gets an event by its recency & paginate results by page number and limit of events per page

Widget: Event
Request Type: POST
Base URL: /api/v3/app	
API Endpoint: /events	
Payload: name, files[image], tagline, schedule, description, moderator, category, sub_category, rigor_rank		
Description: Creates an event and returns the Id of the event i.e. created

Widget: Event
Request Type: PUT
Base URL: /api/v3/app	
API Endpoint: /events/:id
Payload: name, files[image], tagline, schedule, description, moderator, category, sub_category, rigor_rank		

Widget: Event
Request Type: DELETE
Base URL: /api/v3/app	
API Endpoint: /events/:id
Description: Deletes an event based on its Unique Id
