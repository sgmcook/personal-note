# PersonalNote REST API Application -Michael-cook

## Questions you might have before reviewing:
+ Why so many commits on main?
    + Apologies, I would have PR'd into main from my other branches but didn't know what policies are set up, and just worked from main instead. In a normal dev team I would only have merged work that was approved, and with a squash commit.
+ Why did this take you two weeks to write?
	+ Had to learn about REST APIs from scratch which has taken some time -- going from learning the philosophy of REST, the finding an appropriate framework that I could get up to speed with reasonably quickly. Finally, this has been completed in time after work, so I've only been able to dedicate some time each night. 
+ Is there a Postman file for us to import for easy testing?
	+ There is, please find it in the root folder of this project :)
+ What did your learning journey look like for this project?
	+ I've used a number of branches throughout this project which you can use to track what I was learning to use at each point (plus tutorials at the bottom of this doc)
+ Where is the testing?
	+ I did have some initial tests when using the initial Django framework (not the rest one) but they became redundant once I switched to Django rest-framework.
	+ You can still see some of the initial tests in branch method_2_generic_response_objects
	+ I would be happy to discuss some testing that I would add during interview. Some basic examples, I would have tested the 7 behaviours using Django’s default test toolkit (I.e. can the test save a new note, return only archived notes, etc. etc.)


## Steps to run and get set up:
NOTE: This application runs on docker so the person testing it doesn't need to install everything. Please make sure you have it installed, then run the following commands:

+ Download the this repo into a folder of your choice using <code>git clone https://github.com/tf-interviews/-Michael-cook.git</code>, and navigate into it. 

+ From within the root folder of this project run the following:
	<code>docker-compose up -d</code>
It will download the container images for you

+ **Troubleshooting** If your personalnote container is reporting errors of not knowing which port to run on, close the container down <code>docker-compose down</code> and the bring it up again.

+ Navigate into the container with <code>docker exec -it <container_name> /bin/bash</code>

+ Run the following commands: 
	+ <code>python manage.py makemigrations</code>
	+ <code>python manage.py migrate</code>
	+ <code>python manage.py createsuperuser</code>

+ The server should be up and running and you can jump into accessing the API below :)

+ You can also go to the admin site to see a list of users and notes with the superuser you've just made: http://localhost:8000/admin


## Accessing the API 
I'm working with the assumption that the user in question has some knowledge about how APIs work; postman is recommended given its ease-of-use. You will need to sign up as a user to make and alter notes. Every action in this system requires you to provide a JWT, which is useable for 1 hour after provision

**NOTE: I've made all postman requests available as an import file called "personalnote.postman_collection.json" in the root directory.**

1.	Signing up your user
	+ To register a user, call the API with the following:
	+ METHOD: POST
	+ URL: http://127.0.0.1:8000/auth/register/
	+ Notes: Django checks the inbound password and won't allow those that are too simple (though you can force this by using the django superuser command on the console if you're running the server) - so make sure it's sufficiently complex.
	+ JSON Example:
		```json
		{
			"username":"JoeBloggs",
			"password":"compl3xP4ssword123",
			"password2":"compl3xP4ssword123",
			"email":"test2@email.com",
			"first_name":"Joe",
			"last_name":"Bloggs"
		}
		```


2.	Getting your access token (Open for 1 hour)
	+ Once you have your user, you will need to request an access token 
	+ METHOD: POST
	+ URL: http://127.0.0.1:8000/auth/login/
	+ Notes: Post a request including your username and password as key:value parameters. This will return your keys. For the sake of time, only the "access" key is relevant for this exercise.
	+ JSON Example: 
		```json
		{
			"username":"admin",
			"password":"admin123"
		}
		```

## Creating, Modifying, and Deleting your notes
Before you begin this, make sure you've followed the steps in the section "Accessing the API section" above. 

**When you make a request using postman, include your access token under "Authorisation" >> Type = Bearer Token >> Add in your token into the "Token" field**

1.	Save a new note
	+ METHOD: POST
    + URL: http://localhost:8000/notes/
	+ Notes: You don't need to specify a user. The token you've obtained will make sure your new note is associated with the user who requested it. Only the title & body are required. By default notes are given datetimes of now, your ID, and archived as false. 
	+ JSON Example:
		```json
		{
			"title": "Hello I'm an example!",
			"body": "Hello from the example body!"
		}
		```

2.	Update a previously saved note
	+ METHOD: PATCH
    + URL: http://localhost:8000/notes/<note_id>
	+ Notes: You only need to include the field that you want to update
	+ JSON Example:
		```json
		{
			"title":"I'm a new title"
		}
		```

		OR

		```json
		{
			"body":"I'm a new body"
		}
		```

3.	Delete a saved note
	+ METHOD: DELETE
    + URL: http://localhost:8000/notes/<note_id>
	+ Notes: Deletes a note 
	+ Example: http://localhost:8000/notes/1

4.	Archive a note
	+ METHOD: PATCH
    + URL: http://localhost:8000/notes/<note_id>
	+ Notes: Archived notes are not moved to a new database. It is only a boolean flag on the note, so a patch is sufficient.
	+ JSON Example:
		```json
		{
			"archived":"true"
		}
		```

5.	Unarchive a previously archived note
	+ METHOD: PATCH
    + URL: http://localhost:8000/notes/<note_id>
	+ Notes: Archived notes are not moved to a new database. It is only a boolean flag on the note, so a patch is sufficient.
	+ Example: http://localhost:8000/notes/1
		+ Sample body:
		```json
		{
			"archived":"false"
		}
		```

6.	List saved notes that aren't archived
	+ METHOD: GET
    + URL: http://localhost:8000/notes/
	+ Notes: At the end of your URI, attach the query param ?archived=false. This will return you a list of unarchived notes associated with your user/access token
	+ Example: http://localhost:8000/notes/?archived=false

7.	List notes that are archived
	+ METHOD: GET
    + URL: http://localhost:8000/notes/
	+ Notes: At the end of your URI, attach the query param ?archived=true. This will return you a list of unarchived notes associated with your user/access token
	+ Example: http://localhost:8000/notes/?archived=true

8.  See all users notes
	+ METHOD: GET
	+ URL: http://localhost:8000/users/
	+ Notes: lists the IDs of the notes in the "notes" field. 
	+ Example: http://localhost:8000/users/


## API Verion 1.0.0 Object fields:
Users (using Django's auth user_):
+ id
+ password
+ last_login
+ is_superuser
+ username
+ first_name
+ last_name
+ email
+ is_staff
+ is_active
+ date_joined

Notes:
+ pub_date (auto fills when note is created)
+ last_updated_date (auto fills when note is created - doesn't update yet though)
+ title
+ body
+ archived
+ owner_id


## Tech stack choices and reasoning
### Python
+ Chosen for familiarity with the language. Given I was learning REST from scratch, it didn't make sense to me to also try to familiarise myself with another language at the same time. 
+ Extensive options for libraries 
+ A lot of other developers are familiar with it so ease of understanding between devs

### **Learned from scratch:** [Django REST framework](https://www.django-rest-framework.org/tutorial/1-serialization/)
+ Easy to use testing methods inbuilt in the framework
+ Excellent tutorials & community support for devs new to REST
+ Premade support for returned HTTP responses with more explicit detail in the function call for devs to read
+ Request & Response objects mean you don't have to manually specificy the request/return type

### **Learned from scratch:** JWTs
+ So that the user only has to provide a username/password once at the beginning of the interactions

### **Learned from scratch:** Docker 
+ For easy transfer of work (without having to set up a DB)
+ Easier to download and run a container than it is to ask reviewers to install individual components

### **Have used SQL DBs before, but not postgres specificaally:** PostgreSQL database
+ Familiarity with SQL DBs over noSQL DBs (I have used Dynamo DB before, but it's been a while)
+ In the long run I would have wanted to implement cluster indexing

### JSON responses
+ Easy to read as responses, easy to collate information for posts and updates


## Long term plans for application
+ Add a password reset function for users - At the moment, forgetting your password requires the admin of the application to manually do it, and god-forbid if they forget their password too.
+ Only allow users to get and edit their own notes (this was how it worked when only username and password were in use, but changing to JWTs has modified this somehow; would need to look into it)
+ Add a relationship so you can see the note title when looking at a list of user's notes
+ Add proper user deletion functionality 
+ Start adding unit & intergration tests
+ Leverage the JWT token refresh function properly - as it stands I've just extended the basic auth to an hour instead of properly using the refresh which lasts longer. 
+ Implement the regex that doesn't force users to have to close all their URLs with forward slashes 


## Tutorials and guides used: 
+ [Django Getting Started tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
+ [Rest Getting Started tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)
+ [Yunus Cevik's JWT Authentication guide](https://medium.com/django-rest/django-rest-framework-jwt-authentication-94bee36f2af8)
+ [Yunus Cevil's Register Users guide](https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5)
+ [Cameron Mckenzie's Docker by Example](https://www.youtube.com/watch?v=JmyAMcKUNYA&list=LL&index=57)
+ [Amigoscode Getting started with Postgres](https://www.youtube.com/watch?v=BLH3s5eTL4Y&list=LL&index=97)
+ [Help with Coding interviews (humerous, not serious)](https://www.youtube.com/watch?v=kVgy1GSDHG8&list=LL&index=68)
+ [Docker & Django](https://docs.docker.com/samples/django/)
+ Many other members of Stack overflow <3