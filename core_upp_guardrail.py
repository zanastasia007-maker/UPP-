# /sims/core_upp_guardrail.py
def require_pause(decision_context: str, stakes: str = "high"):
    if "launch" in decision_context or "deploy" in decision_context:
        raise UPPPauseError(
            f"[TRIGGER] High-stakes action: {decision_context}\n"
            f"[PAUSE] Human review required before [RESUME]\n"
            f"[LOG] 2025-11-15 16:05 CST | @anastasiaz007 principle enforced"
        )
