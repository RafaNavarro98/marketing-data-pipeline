import numpy as np

def detect_anomalies(df, column="CTR", threshold=2):
    """Detecta anomalias usando z-score."""
    mean = df[column].mean()
    std = df[column].std()
    df["anomaly"] = np.abs((df[column] - mean) / std) > threshold
    return df
 
