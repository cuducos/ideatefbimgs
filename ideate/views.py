# coding: utf-8
import base64
import cairosvg
from flask import render_template, request, Response
from ideate import app
from unipath import Path


@app.route('/')
def index():
    f = app.config['FIELDS']
    fields = zip(f, map(lambda x: x.title(), f), ['' for i in range(len(f))])
    return render_template(
        'base.html',
        fields=fields,
        ph=app.config['PLACEHOLDERS'])


@app.route('/download', methods=['GET'])
def download():

    # get values
    sent = map(lambda x: request.args[x], app.config['FIELDS'])
    values = dict(zip(app.config['FIELDS'], sent))
    try:
        volume = values['volume']
        season = values['season']
        year = values['year']
        color = values['color']
    except:
        return 'Error'

    # path to embed
    twitter_file = Path('ideate', 'static', 'imgs', 'Twitter.png')
    f = open(twitter_file)
    twitter = base64.b64encode(f.read())
    f.close()

    # return image
    svg = render_template(
        'Cover.svg',
        volume=values['volume'],
        season=values['season'],
        year=values['year'],
        color=values['color'],
        twitter=twitter)
    png = cairosvg.svg2png(bytestring=svg)
    return Response(png, mimetype='image/png')
