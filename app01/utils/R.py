def result(code, msg, data):
    res = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return res


def error(code, msg):
    res = {
        "code": code,
        "msg": msg
    }
    return res
