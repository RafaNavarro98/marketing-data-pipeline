def compute_metrics(df):
    """Calcula métricas de marketing digital."""
    df["CTR"] = df["clicks"] / df["impressions"]
    df["CVR"] = df["conversions"] / df["clicks"]
    df["CPA"] = df["spend"] / df["conversions"]
    df["ROAS"] = (df["conversions"] * 50) / df["spend"]  # valor médio por conversão = 50
    return df
 
