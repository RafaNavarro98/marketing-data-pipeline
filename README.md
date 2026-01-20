# 📊 Marketing Data Pipeline

Este projeto implementa uma **pipeline de dados de marketing digital** em Python.  
O objetivo é demonstrar como coletar dados (mock ou API), calcular métricas de performance, detectar anomalias e gerar relatórios em CSV e gráficos.

---

## 🚀 Funcionalidades
- Ingestão de dados via:
  - **Mock** (dados simulados)
  - **API HTTP** (exemplo com JSONPlaceholder ou outra API real)
- Cálculo automático de métricas:
  - CTR (Click-Through Rate)
  - CVR (Conversion Rate)
  - CPA (Cost per Acquisition)
  - ROAS (Return on Ad Spend)
- Detecção de anomalias com z-score
- Exportação para CSV (`data/processed/`)
- Geração de gráficos em PNG (`reports/charts/`)

---

## 📂 Estrutura do projeto
marketing-data-pipeline/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── api_client.py
│   ├── transform.py
│   ├── anomaly.py
│   ├── alerts.py
│   ├── pipeline.py
│   └── config.py
├── data/
│   └── processed/
│       └── metrics_daily.csv
└── reports/
└── charts/
└── metrics.png 
