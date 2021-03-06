# -----------------------------------------------------------------------------
#
# Copyright (C) 2017, Richard Cook. All rights reserved.
#
# -----------------------------------------------------------------------------

def _safe_token(s):
    h, t = s[0], s[1:]
    h = h if h.isalpha() else "_"
    t = "".join(map(lambda c: c if c.isalnum() else "_", t))
    return h + t

class TokenList(object):
    def __init__(self, s):
        self._fragments = s.replace("-", "_").split("_")
        self._safe_tokens = map(_safe_token, filter(lambda x: len(x) > 0, self._fragments))

    @property
    def fragments(self): return self._fragments

    @property
    def safe_tokens(self): return self._safe_tokens
