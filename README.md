agora_demo
==========

Demo app for Agora Games

This app uses the Flask framework in Python to create a simple RESTful API for interacting with a player database.

I did not use any database for this app, but it could easily be adapted to work with MongoDB or most other NoSQL databases.

Supported methods include:

/players GET
Retrieves the data for all current player entries.



/players/<<int:id>>
Retrieves the data for the specified id. Returns a 404 if the id is not found.



/players POST
Creates a new player. The id is automagically generated. There are no restrictions on what fields can be put into the "players" model, but the POST data must be in JSON.



/players/<<int:id>> PUT
Updates the player at the specified id. Data must be in JSON.



/players/<<int:id>> DELETE
Deletes the player at the specified id. Returns a {'completed':True} if it ran successfully.
