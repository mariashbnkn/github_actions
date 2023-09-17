from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Length


class ListZodiacForm(FlaskForm):
    name = StringField(
        "Name:",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    date = DateField(
        'Date',
        validators=[DataRequired()]
    )
