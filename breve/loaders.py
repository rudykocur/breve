import os


class FileLoader(object):
    __slots__ = []

    # noinspection PyMethodMayBeStatic
    def stat(self, template, root):
        timestamp = int(os.stat(os.path.join(root, template)).st_mtime)
        uid = os.path.join(root, template)
        return uid, timestamp

    # noinspection PyMethodMayBeStatic
    def load(self, uid):
        with open(uid, 'U') as f:
            return f.read()
