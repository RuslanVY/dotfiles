import os
import subprocess
from libqtile import hook

# ─────────────────────────────────────────────
#  Хуки (автозапуск)
# ─────────────────────────────────────────────
@hook.subscribe.startup_once
def autostart():
    """Выполняется один раз при старте Qtile."""
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([script])

