#!/usr/bin/env python3
import subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent.parent
subprocess.run([sys.executable,str(root/'scripts/validate_project.py'),str(root)],check=True)
subprocess.run([sys.executable,str(root/'scripts/export-book.py'),'--format', 'all'],check=True)
