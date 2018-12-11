from reconfigure.nodes import *
from reconfigure.parsers.nginx import NginxParser


class BIND9Parser (NginxParser):
    """
    A parser for named.conf
    """

    tokens = [
        (r"(masters)\s+?([^\s{}]*)\s+?(port|dscp)\s+?([^\s{}]*\s*)\s*(port|dscp)\s*?([^\s{}]*\s*)\s*{", lambda s, t: ('section_start', t)),
        (r"(listen-on-v6|listen-on|masters)\s+?(port|dscp)\s+?([^\s{}]*\s*)\s*{", lambda s, t: ('section_start', t)),
        (r"(view|zone)\s+?([^\s{}]*)?\s+?([^\s{}]*)\s*{", lambda s, t: ('section_start', t)),
        (r"(acl|key|masters|server)\s+?([^\s{}]*\s*)\s*{", lambda s, t: ('section_start', t)),
        (r"(controls|logging|options)\s+?([^\s{}]*\s*)*{", lambda s, t: ('section_start', t)),
        (r"(allow-notify|allow-query-on|allow-query|allow-recursion-on|allow-recursion|allow-transfer|allow-update-forwarding|allow|also-notify|alt-transfer-source-v6|alt-transfer-source|disable-algorithms|dual-stack-servers|forwarders|managed-keys|match-clients|match-destinations|rrset-order|sortlist|update-policy)\s+?([^\s{}]*\s*)*{", lambda s, t: ('section_start', t)),
        (r"(channel)\s+?([^\s{}]*\s*)\s*{", lambda s, t: ('section_start', t)),
        (r"\#.*?\n", lambda s, t: ('comment', t)),
        (r"//.*?\n", lambda s, t: ('comment', t)),
        (r"/\*.*?\*/", lambda s, t: ('comment', t)),
        (r"((([^\s{};#]+)|({\s*([^\s{};#]+;\s*)*}))\s*?)+;", lambda s, t: ('option', t)),
        (r"\s", lambda s, t: 'whitespace'),
        (r"$^", lambda s, t: 'newline'),
        (r"\};", lambda s, t: 'section_end'),
    ]
    token_section_end = '};'
