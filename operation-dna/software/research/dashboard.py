"""Dependency-free HTML opportunity dashboard."""
from html import escape
from pathlib import Path
from .storage import ResearchStore


def render(db_path: str = "data/operation_dna.db", output: str = "data/opportunities.html") -> str:
    store = ResearchStore(db_path)
    try:
        rows = store.top_opportunities(100)
    finally:
        store.close()
    body = []
    for i, row in enumerate(rows, 1):
        body.append(
            f"<tr><td>{i}</td><td>{escape(str(row.get('name','')))}</td>"
            f"<td>{escape(str(row.get('domain','')))}</td>"
            f"<td>{float(row.get('score', 0)):.4f}</td>"
            f"<td>{float(row.get('evidence_score', 0)):.2f}</td>"
            f"<td>{escape(str(row.get('thesis','')))}</td></tr>"
        )
    html = """<!doctype html><meta charset='utf-8'><title>Operation DNA Opportunities</title>
<style>body{font-family:system-ui;margin:2rem}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:.5rem;text-align:left}th{background:#eee}</style>
<h1>Opportunity Queue</h1><table><thead><tr><th>#</th><th>Opportunity</th><th>Domain</th><th>Score</th><th>Evidence</th><th>Thesis</th></tr></thead><tbody>""" + "".join(body) + "</tbody></table>"
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return str(path)


if __name__ == "__main__":
    print(render())
