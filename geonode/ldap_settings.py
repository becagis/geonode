from .settings import *
from django_auth_ldap import config as ldap_config
from geonode_ldap.config import GeonodeNestedGroupOfNamesType
import ldap

# enable logging
import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

AUTHENTICATION_BACKENDS += (
    "geonode_ldap.backend.GeonodeLdapBackend",
)
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER )

# django_auth_ldap configuration
AUTH_LDAP_SERVER_URI = os.getenv("LDAP_SERVER_URL")
ldap_bind_dn = os.getenv("LDAP_BIND_DN", default="none")
if (ldap_bind_dn != "none"):
    AUTH_LDAP_BIND_DN = os.getenv("LDAP_BIND_DN")
    AUTH_LDAP_BIND_PASSWORD = os.getenv("LDAP_BIND_PASSWORD")

AUTH_LDAP_USER_SEARCH = ldap_config.LDAPSearch(
    os.getenv("LDAP_USER_SEARCH_DN"),
    ldap.SCOPE_SUBTREE,
    os.getenv("LDAP_USER_SEARCH_FILTERSTR")
)
# should LDAP groups be used to spawn groups in GeoNode?
#AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_GROUP_SEARCH = ldap_config.LDAPSearch(
    os.getenv("LDAP_GROUP_SEARCH_DN"),
    ldap.SCOPE_SUBTREE,
    os.getenv("LDAP_GROUP_SEARCH_FILTERSTR")
)
AUTH_LDAP_GROUP_TYPE = GeonodeNestedGroupOfNamesType()
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": os.getenv("LDAP_USER_FISRTNAME"),
    "last_name": os.getenv("LDAP_USER_LASTNAME"),
    "email": os.getenv("LDAP_USER_EMAIL")
}
#AUTH_LDAP_FIND_GROUP_PERMS = True
# AUTH_LDAP_MIRROR_GROUPS_EXCEPT = [
#     "test_group"
# ]

# these are not needed by django_auth_ldap - we use them to find and match
# GroupProfiles and GroupCategories
GEONODE_LDAP_GROUP_NAME_ATTRIBUTE = os.getenv("LDAP_GROUP_NAME_ATTRIBUTE", default="cn")
GEONODE_LDAP_GROUP_PROFILE_FILTERSTR = os.getenv("GEONODE_LDAP_GROUP_PROFILE_FILTERSTR")
GEONODE_LDAP_GROUP_PROFILE_MEMBER_ATTR = os.getenv("LDAP_GROUP_PROFILE_MEMBER_ATTR")