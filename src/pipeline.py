from src.api_client import fetch_events_mock, fetch_events_http

from src.transform import compute_metrics
from src.anomaly import detect_anomalies
from src.alerts import save_alerts
from src import config
import matplotlib.pyplot as plt

def plot_metrics(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["day"], df["CTR"], marker="o", label="CTR")
    plt.plot(df["day"], df["CPA"], marker="x", label="CPA")
    plt.plot(df["day"], df["ROAS"], marker="s", label="ROAS")
    plt.legend()
    plt.title("Métricas da campanha")
    plt.xlabel("Dia")
    plt.ylabel("Valor")
    plt.savefig("reports/charts/metrics.png")
    plt.close()


from src.api_client import fetch_events_mock, fetch_events_http

def run_pipeline(days=14, source="mock", base_url=None, token=None):
    print(f"Rodando pipeline com {days} dias, fonte={source}")

    # 1. Ingestão
    if source == "mock":
        df = fetch_events_mock(days)
    elif source == "http":
        df = fetch_events_http(base_url, token, days)
    else:
        raise ValueError("Fonte inválida. Use 'mock' ou 'http'.")

    # resto da pipeline...




    # 2. Transformação
    df = compute_metrics(df)

    # 3. Detecção de anomalias
    df = detect_anomalies(df, column="CTR", threshold=config.ANOMALY_THRESHOLD)

    # 👉 Teste: imprimir primeiras linhas com métricas
    print("\nPrévia das métricas calculadas:")
    print(df[["day", "CTR", "CVR", "CPA", "ROAS"]].head())

    # 4. Salvar métricas
    df.to_csv(config.DATA_PROCESSED, index=False)

    # 5. Gerar alertas
    save_alerts(df, path=config.ALERTS_FILE)

    # 6. Gráfico
    plot_metrics(df)

    print("✅ Pipeline concluída")

# ...

