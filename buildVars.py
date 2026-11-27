from site_scons.site_tools.NVDATool.typings import (
    AddonInfo,
    BrailleTables,
    SymbolDictionaries,
)
from site_scons.site_tools.NVDATool.utils import _

addon_info = AddonInfo(
    addon_name="dengjen_neural_voices",
    addon_summary=_("Dengjen Neural Voices"),
    addon_description=_(
        """Adds fast, local neural text-to-speech voices to NVDA. Provides a synthesizer driver for Piper voice models via the dengjen engine, together with a voice manager for downloading and installing voices."""
    ),
    addon_version="4.2.2",
    addon_changelog=_(
        "This unofficial version adds Japanese support and vowel clustering support from Piper 1.5+ voices. "
        "It also fixes a long-standing inference bug that affected some voices, notably Spanish ones. "
        "You must install the required Japanese dictionary from the Kokoro tab in the voice manager. "
        "The voice catalog was pinned to a more recent commit."
    ),
    addon_author="Musharraf Omer (original) <ibnomer2011@hotmail.com>, Ali Ustek (maintainer) <13117393+austek@users.noreply.github.com>",
    addon_url="https://github.com/zirekhq/dengjen-nvda",
    addon_sourceURL="https://github.com/zirekhq/dengjen-nvda",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2026.1",
    addon_lastTestedNVDAVersion="2026.3",
    addon_updateChannel=None,
    addon_license="GPL 2",
    addon_licenseURL="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html",
)

pythonSources: list[str] = [
    "addon/globalPlugins/*/*.py",
    "addon/synthDrivers/*/*.*",
    "addon/synthDrivers/*/domain/*.py",
    "addon/synthDrivers/*/ports/*.py",
    "addon/synthDrivers/*/adapters/*.py",
    "addon/synthDrivers/*/adapters/*/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py", "addon/installTasks.py"]

excludedFiles: list[str] = [
    "_cygrpc/private_key_signing/*.cc",
    "_cygrpc/private_key_signing/*.h",
    "protobuf/internal/_parameterized.py",
    "protobuf/internal/testing_refleaks.py",
]

baseLanguage: str = "en"

markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
