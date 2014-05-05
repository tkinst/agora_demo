from flask import Flask, request, flash, render_template, abort, redirect, url_for, jsonify
import re
import sys
import json

app = Flask(__name__)

PLAYERS_DATA = {}
ID_INC = 1

@app.route('/')
def index():
	# basic home screen, maybe documentation
	pass

@app.route('/players/new')
def player_new():
	# new player
	pass

@app.route('/players/<int:id>/edit')
def player_edit(id):
	# dialouge to edit player
	pass

##### CRUD OPERATIONS BELOW #####

@app.route('/players',  methods=['GET'])
def player_index():
	# show list of players
	return jsonify({'players':PLAYERS_DATA}) # i love jsonify

@app.route('/players/<int:id>', methods=['GET'])
def player_show(id):
	# show single player
	# !!!
	if id in PLAYERS_DATA:
		return jsonify({'player':PLAYERS_DATA[id]}) # return the data at that id
	else:
		abort(404) # not found in database

@app.route('/players/<int:id>', methods=['PUT'])
def player_update(id):
	# update player
	# !!!

	if not request.json: 
		#if there's no data to update, the request was bad
		abort(400)

	if id in PLAYERS_DATA:
		this_id = PLAYERS_DATA[id]
		data = request.json
		# loop through the data and update the dictionary.
		# this may be unnecessary since I updated this to no longer use those evil MultiDicts
		for key in data:
			temp_dict = {key:data[key]}
			this_id.update(temp_dict)
		PLAYERS_DATA[id] = this_id
		return jsonify( { 'player': PLAYERS_DATA[id]})
	else:
		abort(404) #id doesn't exist!



@app.route('/players/<int:id>', methods=['DELETE'])
def player_destroy(id):
	# destroy player
	# !!!
	if id in PLAYERS_DATA:
		PLAYERS_DATA.pop(id)
		return jsonify( { 'completed':True })
	else:
		abort(404)


@app.route('/players', methods=['POST'])
def player_create():
	# create player
	# !!!
	global ID_INC

	if not request.json: #no data means bad request
		abort(400)

	newdata = request.json
	id = ID_INC
	newdata.update({"id":id})
	PLAYERS_DATA[id] = newdata

	ID_INC += 1 #increment the autocounter

	return jsonify( { 'player': PLAYERS_DATA[id]}), 201




if __name__ == "__main__":
	app.run(debug=True)

