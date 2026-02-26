"""
Technique: Signal Monitoring Checks (Production Guardrails)
Use When:
- Once a signal is live, you monitor stability: missing rates, drift, extremes
- Cheap checks catch upstream data breaks before trading losses
"""

import pandas as pd


def signal_checks(df: pd.DataFrame, col: str = "signal") -> pd.DataFrame:
    s = df[col]
    return pd.DataFrame(
        {
            "n": [int(s.size)],
            "null_rate": [float(s.isna().mean())],
            "min": [float(s.min())],
            "p01": [float(s.quantile(0.01))],
            "p50": [float(s.quantile(0.50))],
            "p99": [float(s.quantile(0.99))],
            "max": [float(s.max())],
        }
    )


if __name__ == "__main__":
    df = pd.DataFrame({"signal": [0.1, 0.2, None, -0.3, 10.0, -10.0]})
    print(signal_checks(df))
