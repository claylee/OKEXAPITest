import json
from datetime import date
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, o):
        print(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)


class AlchemyEncoder(json.JSONEncoder):
    
    _visited_objs = []
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # don't re-visit self
            if obj in self._visited_objs:
                return None
            self._visited_objs.append(obj)

            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime):
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)