import sys
sys.path.append('src')
import rgvflood
from spyce.fabfile import docs
from spyce.spell import kubespray
from invoke import Collection

ns = Collection()
ns.add_collection(rgvflood)
ns.add_collection(docs)
ns.add_collection(kubespray)