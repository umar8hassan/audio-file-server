from flask import request

from db import db
from app import app
import constants
import configs
from utils import validate_request, validate_file_type
from models import Audiobook, Podcast, Song


logger = app.logger
models = {'song': Song, 'podcast': Podcast, 'audiobook': Audiobook}


@app.errorhandler(Exception)
def handle_exception(error):
    logger.error('%s', str(error))

    return 'internal-server-error', 500


@app.errorhandler(404)
def page_not_found(error):

    return 'URL not found!', 404


@app.route('/create/', methods=['POST'])
def create():
    data = request.json
    audio_file_type = data.get('audioFileType', '')
    metadata = data.get('audioFileMetadata', {})

    status, error = validate_request(audio_file_type, metadata)
    if not status:
        return error, 400

    audio_file = models[audio_file_type](**metadata)
    db.session.add(audio_file)
    db.session.commit()

    return f'{audio_file_type.title()} has been uploaded!'


@app.route('/<audio_file_type>/<audio_file_id>/', methods=['GET'])
def get(audio_file_type, audio_file_id):
    if audio_file_type not in constants.SUPPORTED_AUDIO_TYPES:
        return 'Invalid audio file type provided! It must be one of these: ' \
               f'{", ".join(constants.SUPPORTED_AUDIO_TYPES)}'

    audio_file = db.session.query(models[audio_file_type]
                                  ).filter_by(id=audio_file_id).first()

    if not audio_file:
        return f'Audio file not found for ID: {audio_file_id}', 400

    return audio_file.to_json()


@app.route('/<audio_file_type>/', methods=['GET'])
def get_all(audio_file_type):
    status, error = validate_file_type(audio_file_type)
    if not status:
        return error, 400

    audio_files = db.session.query(models[audio_file_type]).all()

    if not audio_files:
        return f'No {audio_file_type.title()}(s) found!'

    return {'data': [audio_file.to_json() for audio_file in audio_files]}


@app.route('/<audio_file_type>/<audio_file_id>/', methods=['PUT'])
def update(audio_file_type, audio_file_id):
    data = request.json
    metadata = data.get('audioFileMetadata', {})

    status, error = validate_request(audio_file_type, metadata)
    if not status:
        return error, 400

    if not db.session.query(models[audio_file_type]).filter_by(id=audio_file_id).first():
        return f'Audio file not found for ID {audio_file_id}!', 400

    db.session.query(models[audio_file_type]).filter_by(id=audio_file_id) \
                                             .update(metadata)
    db.session.commit()

    return f'{audio_file_type.title()} with id {audio_file_id} has been updated!'


@app.route('/<audio_file_type>/<audio_file_id>/', methods=['DELETE'])
def delete(audio_file_type, audio_file_id):
    status, error = validate_file_type(audio_file_type)
    if not status:
        return error, 400

    file = db.session.query(models[audio_file_type]).filter_by(id=audio_file_id) \
                                                    .first()
    if not file:
        return f'Audio file not found for ID {audio_file_id}!', 400

    db.session.delete(file)
    db.session.commit()

    return f'{audio_file_type.title()} with id {audio_file_id} has been deleted!'


if __name__ == '__main__':
    app.run(debug=configs.DEBUG, host=configs.APP_HOST, port=configs.APP_PORT)
