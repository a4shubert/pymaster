"""
Technique: Feature Flags + Percentage Rollout

Why this is enterprise:
- Gradual rollout reduces risk.
- Enables fast rollback without redeploy.
- Supports A/B tests and staged deployments.

Pattern:
1) Represent flags in config.
2) Decide per user/request deterministically.
3) Keep flag checks near the boundary.
"""

import hashlib
from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureFlag:
    name: str
    enabled: bool
    rollout_percent: int = 100


def is_enabled(flag: FeatureFlag, subject_id: str) -> bool:
    if not flag.enabled:
        return False
    if flag.rollout_percent >= 100:
        return True
    if flag.rollout_percent <= 0:
        return False

    # Stable hash -> 0..99
    digest = hashlib.sha256(f"{flag.name}:{subject_id}".encode("utf-8")).digest()
    bucket = digest[0] % 100
    return bucket < flag.rollout_percent


if __name__ == "__main__":
    flag = FeatureFlag(name="new_checkout", enabled=True, rollout_percent=30)
    for user in ["u1", "u2", "u3", "u4", "u5"]:
        print(user, is_enabled(flag, user))
