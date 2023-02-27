from datetime import datetime
from urllib.parse import urljoin

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin('http://localhost/', self.short)
        )

    def from_dict(self, data):
        for field in ['url', 'custom_id']:
            if field in data:
                setattr(self, field, data[field])
