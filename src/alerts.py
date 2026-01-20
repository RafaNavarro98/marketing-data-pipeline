def save_alerts(df, path="data/processed/alerts.csv"):
    """Salva alertas em CSV e imprime no console."""
    alerts = df[df["anomaly"]]
    if not alerts.empty:
        alerts.to_csv(path, index=False)
        print("⚠️ Alertas detectados:")
        print(alerts)
    else:
        print("✅ Nenhuma anomalia encontrada.")
 
