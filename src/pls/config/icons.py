"""
Do not import variables from this module, always import the module directly and use its
variables with a dot ``.`` notation.
"""

from __future__ import annotations

from pathlib import Path

from pls.data.utils import load_yml_file
from pls.exceptions import ConfigException


def get_icons(conf_paths: list[Path]) -> tuple[dict[str, str], dict[str, str]]:
    """
    Icons are technically just string-string maps. Nerd Font icons map icon
    names to Unicode code-points containing character glyphs and emoji icons
    map icon names to emoji characters.

    :param conf_paths: the list of config files from which to import icons
    :return: the mapping of icon name to icon glyph
    """

    nerd: dict[str, str] = {}
    emoji: dict[str, str] = {}

    for conf_path in reversed(conf_paths):
        conf = load_yml_file(conf_path)

        if not isinstance((nerd_val := conf.get("nerd_icons", {})), dict):
            raise ConfigException("[italic]`nerd_icons`[/] must be a dictionary.")
        nerd.update(nerd_val)

        if not isinstance((emoji_val := conf.get("emoji_icons", {})), dict):
            raise ConfigException("[italic]`emoji_icons`[/] must be a dictionary.")
        emoji.update(emoji_val)

    return nerd, emoji


nerd_icons: dict
"""the mapping of icon names to Unicode code-points"""

emoji_icons: dict
"""the mapping of icon names to emoji characters"""
