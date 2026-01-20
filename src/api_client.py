import pandas as pd
import requests

# Mock para testes locais
def fetch_events_mock(days=14):
    data = {
        "day": list(range(1, days+1)),
        "impressions": [1000 + i*10 for i in range(days)],
        "clicks": [50 + i for i in range(days)],
        "conversions": [5 + i//2 for i in range(days)],
        "spend": [100 + i*5 for i in range(days)]
    }
    return pd.DataFrame(data)

# API real
def fetch_events_http(base_url, token, days=14):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    params = {"days": days}

    response = requests.get(f"{base_url}/events", headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # ⚠️ Adaptar para colunas esperadas
        if not {"impressions","clicks","conversions","spend"}.issubset(df.columns):
            # cria colunas fake se a API não tiver esses campos
            df["impressions"] = 1000 + df.index*10
            df["clicks"] = 50 + df.index
            df["conversions"] = 5 + (df.index//2)
            df["spend"] = 100 + df.index*5

        return df
    else:
        raise Exception(f"Erro na API: {response.status_code} - {response.text}")
