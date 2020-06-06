from app import app
from flask import make_response, jsonify, request, render_template
from app.AniList import AniList
from app.pair import pair
import os
import re

url = 'http://localhost:5000'

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 404)

@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': 'Conflict'}), 409)

@app.route('/')
@app.route('/index')
def index():
    usersL = []
    for fn in os.listdir('./app/animelists'):
        x = re.search( r'animelist_(.*)\.xml', fn)
        usersL.append(x.group(1))

    return render_template('index.html',title = 'Home Page', bheader = 'User List', baseURL = url, list = usersL)

@app.route('/list/<string:username>', methods=['GET'])
def getList(username):
    db = AniList(username)
    animes = []
    for elem in db.root.findall("./anime"):
        animes.append(elem[1].text)
    return render_template('animelist.html', username = username, baseURL = url, list = animes)


@app.route('/list/<string:username>/<string:series_title>', methods=['GET'])
def getAnime(username, series_title):
    db = AniList(username)
    anime = db.getAnime(series_title)
    paramL = []
    for param in anime:
        tmp = pair(param.tag, param.text)
        tmp.first = tmp.first.replace('_', ' ')
        tmp.first = tmp.first.title()
        paramL.append(tmp)

    return render_template('anime.html', anime_title = anime[1].text, list = paramL)

@app.route('/list/<string:username>/<string:series_title>/<string:param>', methods=['GET'])
def getAniParam(username, series_title, param):
    db = AniList(username)
    prm = db.getAnimeParam(series_title, param)
    return make_response(prm.text,200)

@app.route('/list/<string:username>', methods=['POST'])
def postAnime(username):
    db = AniList(username)
    data = request.form
    db.addAnime(data['series_title'], data['series_type'], data['series_episodes'], data['my_watched_episodes'], data['my_score'], data['my_status'], data['my_times_watched'])
    return make_response('',201)
    

@app.route('/list/<string:username>/<string:series_title>', methods=['PUT'])
def putAniParam(username, series_title):
    db = AniList(username)
    data = request.form
    db.modAnime(series_title, data['parameter_name'], data['new_parameter'])
    return make_response('', 200)

@app.route('/list/<string:username>/<string:series_title>', methods=['DELETE'])
def deleteAnime(username, series_title):
    db = AniList(username)
    db.delAnime(series_title)
    return make_response('', 200)