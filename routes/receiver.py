import json
from flask import Blueprint, current_app, Response, request
from pprint import pprint
from time import sleep

receiver_template = Blueprint('receiver_template', __name__, template_folder='templates')


@receiver_template.route('/', methods=['GET', 'PUT'])
def receiver():
    if request.method == 'GET':
        return show()
    elif request.method == 'PUT':
        return update()


def show():
    current_app.logger.info("get receiver ")
    receiverInfo = {
        'on': current_app.rx.on,
        'volume': current_app.rx.volume,
        'input': current_app.rx.input,
        'mute': current_app.rx.mute,
        'inputs': current_app.rx.inputs()
    }

    return Response(response=json.dumps(receiverInfo), mimetype='application/json')


def update():
    current_app.logger.info("update receiver")
    receiverInfo = request.json
    if current_app.rx.on != receiverInfo['on']:
        current_app.rx.on = receiverInfo['on']
    if current_app.rx.on:
        if current_app.rx.volume != receiverInfo['volume']:
            current_app.rx.volume = receiverInfo['volume']
        if current_app.rx.input != receiverInfo['input']:
            current_app.rx.input = receiverInfo['input']
        if current_app.rx.mute != receiverInfo['mute']:
            current_app.rx.mute = receiverInfo['mute']
    return Response(response=json.dumps(receiverInfo), mimetype='application/json')
