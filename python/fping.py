import subprocess
import tempfile
from datetime import datetime

def fping(ips=None, count_pkgs=None, size_pkg=None, intertime=None):
    if not ips or not count_pkgs or not size_pkg or not intertime:
        return None, None

    
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as f:
        f.write("\n".join(ips))
        f.flush()

        args = [
            "/sbin/fping",
            "-f", f.name,
            "-i", str(intertime),
            "-c", str(count_pkgs),
            "-b", str(size_pkg),
            "-r", "0",""
            "-t", "200"
        ]

        subp = subprocess.run(
            args,
            capture_output=True,
            text=True,
        )

    timestamp = datetime.now().isoformat(sep="T", timespec="seconds")

    # trate stdout como saída principal
    out = subp.stdout.strip()
    err = subp.stderr.strip()

    res = f"{timestamp}\n{out}" if out else f"{timestamp}\n"
    return res, err
