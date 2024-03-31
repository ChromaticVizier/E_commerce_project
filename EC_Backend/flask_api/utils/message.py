status_msg = {
    200: 'success',
    1000: 'The data is incomplete.',
    1001: 'Username or password is incorrect.',
    1002: 'Username is invalid.',
    1003: 'Password is invalid.',
    1004: 'Password inconsistent.',
    1005: 'Phone number is invalid.',
    1006: 'E-mail is invalid.',
    1007: 'Another error occurred while registering.',
    1008: 'Not logged in',
    1009: 'Token is invalid.',
    1010: '',
    1011: '',
    1012: '',
}


def to_dict_msg(status=200, data=None, msg=None):
    return {
        'status': status,
        'data': data,
        'msg': msg if msg else status_msg.get(status)
    }
