import argparse
from src.pipeline import run_pipeline

def parse_args():
    p = argparse.ArgumentParser(description='Pipeline de integração API (mock/real) + alertas')
    p.add_argument('--dias', type=int, default=14, help='Quantidade de dias a processar')
    p.add_argument('--source', type=str, default='mock', choices=['mock', 'http'], help='Fonte de dados')
    p.add_argument('--base_url', type=str, default=None, help='Base URL para API real')
    p.add_argument('--token', type=str, default=None, help='Token Bearer para API real')
    return p.parse_args()

if __name__ == '__main__':
    args = parse_args()
    run_pipeline(days=args.dias, source=args.source, base_url=args.base_url, token=args.token)
 
