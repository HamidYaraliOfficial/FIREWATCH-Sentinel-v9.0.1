from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlannedChecks:
    rule_engine: bool = True
    browser_discovery: bool = False
    zap: bool = False


class PlannerProtocol:
    def plan(self, *, enable_browser: bool, enable_zap: bool, passive_only: bool) -> PlannedChecks:
        """Replaceable deterministic planner boundary.

        A future LLM planner can implement this same contract and still be
        constrained by the ScopePolicy and rule registry.
        """
        return PlannedChecks(
            rule_engine=True,
            browser_discovery=bool(enable_browser and not passive_only),
            zap=bool(enable_zap and not passive_only),
        )
