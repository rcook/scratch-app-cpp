# -----------------------------------------------------------------------------
#
# Copyright (C) 2017, Richard Cook. All rights reserved.
#
# -----------------------------------------------------------------------------

import os

from ptool.git_util import git_execute_attribute, git_symlink
from ptool.template_util import template_tokens

class SimpleCommandInfo(object):
    def __init__(self, command_template):
        self._command_template = command_template
        self._keys = None

    @property
    def keys(self):
        if self._keys is None:
            self._keys = template_tokens(self._command_template)
        return self._keys

    def run(self, ctx, values):
        command = ctx.render_from_template_string(self._command_template, values)
        if os.system(command) != 0:
            raise RuntimeError("Command \"{}\" failed".format(command))

class GitExecuteAttributeCommandInfo(object):
    def __init__(self, path_template):
        self._path_template = path_template
        self._keys = None

    @property
    def keys(self):
        if self._keys is None:
            self._keys = template_tokens(self._path_template)
        return self._keys

    def run(self, ctx, values):
        path = ctx.render_from_template_string(self._path_template, values)
        git_execute_attribute(os.getcwd(), path)

class GitSymlinkCommandInfo(object):
    def __init__(self, source_path_template, target_path_template):
        self._source_path_template = source_path_template
        self._target_path_template = target_path_template
        self._keys = None

    @property
    def keys(self):
        if self._keys is None:
            self._keys = template_tokens(self._source_path_template, self._target_path_template)
        return self._keys

    def run(self, ctx, values):
        source_path = ctx.render_from_template_string(self._source_path_template, values)
        target_path = ctx.render_from_template_string(self._target_path_template, values)
        git_symlink(os.getcwd(), source_path, target_path)

