# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrappers: one sub-package per catalogue category.

Every module is emitted by ``scripts/gen_wrappers.py`` as typed stubs and is then
filled in by hand. ``--init`` never overwrites an existing file; ``--write``
rewrites the generated shape but refuses any module that already holds a written
body, so a hand-filled implementation cannot be lost to a regeneration.
"""
