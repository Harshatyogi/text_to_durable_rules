def generate_durable_rule(rule_json: dict) -> str:
    conditions = rule_json["conditions"]
    action = rule_json["action"]

    cond_expr = []
    for c in conditions:
        cond_expr.append(f"(m.{c['field']} {c['operator']} {c['value']})")

    condition_line = " & ".join(cond_expr)

    rule_code = f"""
from durable.lang import *

with ruleset('{rule_json["ruleset"]}'):

    @when_all({condition_line})
    def rule(c):
        c.assert_fact({action})
"""

    return rule_code
