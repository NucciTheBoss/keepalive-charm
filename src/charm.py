#!/usr/bin/env python3
# Copyright 2022 Canonical

"""Charm the service."""

import logging

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class KeepaliveCharm(CharmBase):

    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.config_changed, self._on_config_changed)
        self.framework.observe(self.on.start, self._on_start)
        self._stored.set_default(things=[])

    def _on_start(self, _):
        self.unit.status = ActiveStatus()

    def _on_config_changed(self, _):
        pass


if __name__ == "__main__":
    main(KeepaliveCharm)
