# Paper Execution V1

Paper execution is now a distinct runtime boundary between AI decisions and the Alpaca paper account.

## Gate order

1. Kill switch
2. Persistent runtime pause
3. Controller execution flag
4. Explicit `XYOOL_PAPER_EXECUTE=YES` opt-in
5. Stock-symbol / quantity / side / reference-price validation
6. Estimated notional limit
7. Live paper-account eligibility check
8. Resource budget consumption
9. Audit authorization event
10. Alpaca paper order submission
11. Audit success or failure event

The controller uses `AlpacaPaperAdapter`, which hard-rejects the live Alpaca endpoint. This milestone does not add live trading capability.

## Readiness check

```powershell
python operation-dna/live_paper_execution.py
```

## Paper order

The two independent execution switches are intentional:

```powershell
$env:XYOOL_PAPER_EXECUTE="YES"
python operation-dna/live_paper_execution.py --execute --symbol AAPL --qty 1 --side buy --reference-price 25
```

The default notional ceiling is `$100`. Override only when intentionally testing a different paper-risk boundary:

```powershell
python operation-dna/live_paper_execution.py --execute --symbol AAPL --qty 2 --side buy --reference-price 25 --max-notional 100
```

Never commit Alpaca credentials. They remain environment variables only.

## Audit

Successful and failed paper execution attempts are appended to:

`data/logs/paper_execution.jsonl`

## Tests

```powershell
python run_tests.py --fail-fast
```
