from functools import wraps


def smoke_check(func):
    """
    check if response code is successful
    field of response has status 'success'
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        resp = func(*args, **kwargs)
        status = resp.get("response")
        assert status == "success", f'Test failed. ' \
            f'Response status should be "success" but was "{status}"'
    return wrapper
