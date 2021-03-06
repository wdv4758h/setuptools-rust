from __future__ import print_function, absolute_import
import sys
import subprocess
from distutils.errors import DistutilsPlatformError

import semantic_version


def cpython_feature():
    version = sys.version_info
    if (2, 7) < version < (2, 8):
        return ("cpython/python27-sys", "cpython/extension-module-2-7")
    elif (3, 3) < version:
        return ("cpython/python3-sys", "cpython/extension-module")
    else:
        raise DistutilsPlatformError(
            "Unsupported python version: %s" % sys.version)


def get_rust_version():
    try:
        output = subprocess.check_output(["rustc", "-V"])
        if isinstance(output, bytes):
            output = output.decode('latin-1')
        return semantic_version.Version(output.split(' ')[1], partial=True)
    except (subprocess.CalledProcessError, OSError):
        raise DistutilsPlatformError('Can not find Rust compiler')
    except Exception as exc:
        raise DistutilsPlatformError(
            'Can not get rustc version: %s' % str(exc))
