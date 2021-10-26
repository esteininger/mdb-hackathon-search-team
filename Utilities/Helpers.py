# -*- coding: utf-8 -*-
import re
import unidecode
from config import secret_key
import base64


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)
