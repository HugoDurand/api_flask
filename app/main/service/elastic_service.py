from app.main import db, es
from flask import jsonify


def add_to_index(index, model):
    if not es:
        return
    fields = {}
    for field in model.__searchable__:
        fields[field] = getattr(model, field)
    es.index(index=index, id=model.id, body=fields)


def remove_from_index(index, model):
    if not es:
        return
    es.delete(index=index, id=model.id)


def query_index(index, searched_value):
    if not es:
        return [], 0
    search = es.search(
        index=index,
        body={
            "query": {
                "multi_match": {
                    "query": searched_value,
                    "type": "phrase_prefix",
                    "fields": ["title"]
                }
            }
        })
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']


class SearchableMixin(object):
    @classmethod
    def search(cls, searched_value):
        ids, total = query_index(cls.__tablename__, searched_value)
        if total == 0:
            return cls.query.filter_by(id=0), 0

        return cls.query.filter(cls.id.in_(ids)).all()

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)
