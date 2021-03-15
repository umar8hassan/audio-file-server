from app import app
import constants

logger = app.logger


def validate_file_type(audio_file_type):
    if audio_file_type not in constants.SUPPORTED_AUDIO_TYPES:
        return False, 'Invalid audio file type provided! It must be one of ' \
                      f'these: {", ".join(constants.SUPPORTED_AUDIO_TYPES)}'
    return True, ''


def validate_request(audio_file_type, metadata):
    try:
        assert audio_file_type in constants.SUPPORTED_AUDIO_TYPES, \
            'Invalid audio file type provided! It must be one of ' \
            f'these: {", ".join(constants.SUPPORTED_AUDIO_TYPES)}'
        assert metadata, 'Metadata cannot be empty!'
        assert metadata.get('name') if audio_file_type != 'audiobook' \
            else metadata.get('title'), \
            'Name of audio file cannot be empty!'
        assert (int(metadata.get('duration')) or 0) > 0, \
            'Duration of file cannot be 0 or negative!'
        if audio_file_type == 'podcast':
            assert metadata.get('host'), 'Host for a podcast cannot be empty!'
            assert isinstance(metadata.get('participants'), list), \
                'Participant data provided in invalid format!'
            assert len(metadata.get('participants')) <= 10, \
                'Limit reached for participants!'
        if audio_file_type == 'audiobook':
            assert metadata.get('author'), 'Author of audiobook cannot be empty!'
            assert metadata.get('narrator'), 'Narrator of an audiobook cannot be empty!'

        return True, ''

    except Exception as error:
        logger.error('An error while validating request!')
        return False, str(error)
