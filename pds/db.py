import glob
import pickle


class Pds_db:
    def __init__(self):
        self.db = {}
        for file in glob.glob("dump.pkl"):
            with open(file, 'rb') as f:
                self.db = pickle.load(f)

    def set(self, key, value):
        try:
            self.db[key] = value
        except KeyError:
            return 'Key Error'
        with open('dump.pkl', 'wb') as f:
            pickle.dump(self.db, f)

    def get(self, key):
        try:
            result = self.db[key]
        except KeyError:
            return 'Key Error'
        return result

    def clear(self):
        self.db.clear()

    def rm(self, key):
        del self.db[key]
        with open('dump.pkl', 'wb') as f:
            pickle.dump(self.db, f)

    def plus(self, key, value_plus):
        try:
            value = self.db[key]
            result = value + value_plus
            self.db[key] = result
        except KeyError:
            return 'Key Error'
        with open('dump.pkl', 'wb') as f:
            pickle.dump(self.db, f)

    def rename(self, key, keynew):
        value = self.db.pop(key)
        self.db[keynew] = value
        with open('dump.pkl', 'wb') as f:
            pickle.dump(self.db, f)

    def find_key(self, key):
        keys = self.db.keys()
        for db_key in keys:
            if db_key == key:
                return 'Found'
        return 'Not_found'

    def find_value(self, value):
        values = self.db.values()
        for db_value in values:
            if db_value == value:
                return 'Found'
        return 'Not_found'

    def list(self):
        return self.db
