import sys
import types

# Master Fix for pkg_resources missing in Python 3.12 on Vercel
try:
    import pkg_resources
except ImportError:
    # Create a dummy pkg_resources module to satisfy drf_yasg
    pkg_res = types.ModuleType('pkg_resources')
    pkg_res.DistributionNotFound = type('DistributionNotFound', (Exception,), {})
    pkg_res.get_distribution = lambda x: types.SimpleNamespace(version='0.0.0')
    sys.modules['pkg_resources'] = pkg_res

from nxtbn.wsgi import application

# This is the entry point for Vercel
app = application
