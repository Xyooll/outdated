# Xyool — Decision Architecture

## Final objective

**CAPITAL COMPOUNDING THROUGH OPPORTUNITY ROTATION**

The permanent asset is capital. Companies are temporary capital destinations.

The active architecture has two conceptual stages before Quant expression:

```text
1. QUALITY QUALIFIER
   Is this opportunity good enough to own?

2. TIME TO CATALYST (TTC)
   Of the qualified opportunities, where should capital be now?
```

Full chain:

```text
CAPITAL
  ↓
COMPANY-LEVEL XYOOL
  ↓
OPPORTUNITY STATE ENGINE
  ↓
QUALITY QUALIFIER
  ↓
TIME TO CATALYST
  ↓
OSE ↔ QUANT DECISION INTERFACE
  ↓
EXECUTABLE POSITION / CASH
  ↓
NEW EVIDENCE
  ↓
STATE + TTC UPDATE
  ↓
HARVEST / ROTATE / REALLOCATE
  ↓
CAPITAL
```

A separate Quant Layer runs alongside the fundamental system and enters the executable-allocation path only through tested integration rules:

```text
FUNDAMENTAL SYSTEM                         QUANT SYSTEM

Company-Level Xyool                       Quant Data
        ↓                                      ↓
Opportunity State Engine                  Quant Models
        ↓                                      ↓
Quality Qualifier                         Signal / Risk State
        ↓                                      ↓
Time to Catalyst                          ↓
        └──────── OSE ↔ QUANT INTERFACE ───────┘
                           ↓
                 Executable Allocation
```

---

## 1. Company-Level Xyool — causal analysis

Answers:

> **Why could this company create asymmetric value?**

Core chain:

**NEED → CONTROL → MOMENTUM → FRICTION → PRICE**

It identifies:
- company-specific structural demand;
- demand cascades;
- bottlenecks / tollbooths;
- company capture;
- backlog and new income streams;
- economic trajectory;
- shareholder friction;
- CFIT;
- market recognition.

Output: **company evidence + causal state**.

---

## 2. Opportunity State Engine — dynamic opportunity state

Answers:

> **What state is the opportunity in, which direction is it moving, how strong is the evidence, and how much opportunity remains?**

Core dimensions include:

**POTENTIAL × SECTOR DEMAND × STRUCTURAL CONFIRMATION × CONVERSION CONFIRMATION × RUNWAY LOCK-IN × VELOCITY × IGNITION × RECOGNITION × FRICTION**

OSE also hosts provisional evidence/state overlays such as:
- Forward Evidence State (FES);
- Cascade Score;
- rerating / nonlinear-recognition research states;
- Conversion Debt diagnostics.

FES is especially important to TTC because it records upstream causal-stage information before financial conversion.

Output: **Opportunity State Card + evidence packet**.

See:
- `skills/xyool/opportunity-state-engine.md`
- `skills/xyool/ose-forward-evidence-state.md`
- `skills/xyool/ose-sector-demand.md`
- `skills/xyool/ose-dual-confirmation.md`
- `skills/xyool/conversion-debt.md`

---

## 3. Quality Qualifier — eligibility

Answers:

> **Is this equity/opportunity good enough to compete for capital at all?**

The qualifier uses Company-Level Xyool + OSE evidence to test:
- real demand;
- company capture/control;
- structural confirmation;
- financial conversion;
- runway durability;
- shareholder capture;
- financing / dilution / governance;
- permanent-impairment risk;
- economic asymmetry / valuation;
- evidence quality.

Conceptual output:

```text
FAIL
WATCH
QUALIFIED
HIGH QUALITY
```

A near catalyst does not rescue a failed quality case.

Once multiple names clear the quality threshold, small quality differences should not automatically dominate a large difference in catalyst proximity or return velocity unless they materially change permanent-loss risk.

---

## 4. Time to Catalyst — capital decision

Answers:

> **Among qualified opportunities, which one deserves capital now?**

TTC is the capital-allocation, ranking, harvest, and rotation layer. There is no separate allocation controller.

TTC integrates:
- event probability;
- event materiality;
- causal distance-to-economic-conversion;
- FES / evidence quality;
- expected conversion window;
- signal age / window position / decay;
- remaining gates;
- funding state;
- procurement / conversion friction;
- recognition gap;
- return velocity;
- remaining opportunity;
- downside and shareholder capture;
- liquidity / transaction friction.

TTC distinguishes:
- **new capital**, which competes aggressively for the best qualified opportunity;
- **earned capital**, which requires a materially higher removal hurdle.

TTC owns desired economic actions:

```text
WATCH
INITIATE
INCREASE
HOLD
REDUCE
HARVEST
ROTATE
CASH
```

See:
- `skills/xyool/time-to-catalyst.md`
- `skills/xyool/ttc-evidence-tested-rules.md`

---

## 5. FES and causal clocks inside TTC

FES is not a separate allocation layer.

```text
FES
= what event is forming and how far it has progressed

PROCUREMENT / R&D / INDUSTRY-SPECIFIC CLOCK
= what conversion window is normal from this stage

TTC
= whether the timing-adjusted qualified opportunity deserves capital now
```

Relevant causal clocks can include:
- procurement / government funding;
- R&D conversion;
- semiconductor qualification / design-win conversion;
- data-center permitting / construction / energization;
- biotech / medtech regulatory and launch sequences;
- industrial award / installation / utilization;
- mining/materials offtake / financing / construction / production.

Reusable Asset Monetization (RAM) may support current economics while a catalyst develops, but does not replace catalyst evidence.

---

## 6. Independent Quant Layer — risk / sizing / execution modifier

Answers:

> **How should TTC's already-decided desired economic exposure be expressed under measured market risk?**

Quant cannot create conviction, invent a broken thesis, or increase exposure above TTC desired exposure.

Frozen production stack conceptually remains:

```text
TTC desired vector
  ↓
market-data readiness
  ↓
daily EWMA97
  ↓
R12M correlation → P01-P common downward-only portfolio scaling
  ↓
SPLIT-C5 / BLEND50 concentration logic
  ↓
R12M final risk safety
  ↓
TTC name ceilings + long-only + no leverage + residual cash
```

The 12% constant remains a **one-sided maximum forecast-volatility budget**, not a realized-volatility target.

Legacy internal code/API field names may remain temporarily for backward compatibility, but they do not define the conceptual architecture. New documentation and new interfaces should use TTC terminology.

See:
- `skills/xyool/quant-architecture.md`
- `skills/xyool/quant-layer.md`
- `skills/xyool/quant-production-defaults.md`

---

## 7. OSE ↔ Quant Decision Interface — authority / execution

The tested authority rule remains unchanged in substance:
- first independent high-quality OSE deterioration checkpoint: Quant may challenge/veto/delay/scale;
- second independent high-quality deterioration checkpoint before recovery: Quant may scale by at most one step or delay at most one monthly checkpoint, but cannot completely veto the economic action;
- F5 capital-survival/governance/shareholder-capture failure overrides Quant;
- Quant cannot invent a fundamental thesis break when SC/CC remain strong.

TTC supplies the desired economic action/magnitude to the interface.

See:
- `skills/xyool/ose-quant-interface.md`

---

## State ownership

```text
COMPANY XYOOL
    owns company-specific causal business state
          ↓
OPPORTUNITY STATE ENGINE
    owns dynamic opportunity/evidence state
          ↓
QUALITY QUALIFIER
    owns eligibility
          ↓
TIME TO CATALYST
    owns ranking, desired capital action, harvest and rotation
          ↓
OSE ↔ QUANT INTERFACE
    owns authority resolution / executable expression

INDEPENDENT QUANT LAYER
    owns empirical market/risk signals and measured model utility
```

No layer should silently absorb the responsibilities of another layer.

---

## Event processing

Every new fundamental/company/sector event follows:

```text
NEW EVENT
   ↓
WHAT CHANGED?
   ↓
COMPANY STATE UPDATE
   ↓
OSE UPDATE
   ↓
QUALITY STILL PASSES?
   ↓
CATALYST STAGE / PROBABILITY / MATERIALITY?
EXPECTED CONVERSION WINDOW?
WINDOW POSITION / DECAY?
RECOGNITION / FRICTION / SHAREHOLDER CAPTURE?
   ↓
TTC RETURN-VELOCITY UPDATE
   ↓
CURRENT vs CANDIDATES vs CASH
   ↓
TTC DESIRED ACTION
   ↓
OSE ↔ QUANT AUTHORITY RULE
   ↓
EXECUTABLE ACTION
```

Every new Quant update follows:

```text
OLD QUANT STATE
   ↓
NEW MARKET DATA
   ↓
VOL / CORRELATION / TREND UPDATE
   ↓
PORTFOLIO RISK + CONCENTRATION STATE
   ↓
OSE ↔ QUANT INTERFACE
   ↓
DOWNWARD-ONLY EXPRESSION WITHIN TTC AUTHORITY
```

---

## Replacement rule

A current holding is not replaced because another qualified candidate has a slightly higher quality rank.

A candidate must clear a replacement hurdle after considering:
- opportunity differential;
- catalyst stage and probability;
- catalyst materiality;
- evidence quality / freshness;
- conversion-window position;
- remaining gates;
- recognition gap;
- return velocity;
- shareholder capture;
- liquidity / transaction costs / taxes where relevant;
- concentration;
- uncertainty;
- permanent-impairment risk.

Fresh, material, late-stage unresolved current-holding catalysts raise the removal hurdle.

When the comparison is close, prefer hold + new capital or partial rotation rather than full replacement.

---

## Anti-chasing rule

Price acceleration is evidence about recognition, not proof of improving economic opportunity.

Before increasing an already-rising position ask:

> **Did the underlying economic opportunity improve faster than the market price?**

Quant momentum/trend may corroborate recognition or ignition, but cannot by itself prove the catalyst improved.

---

## Research-to-capital loop

```text
DISCOVER
  ↓
QUALITY QUALIFY
  ↓
STATE / VALIDATE
  ↓
TIME TO CATALYST
  ↓
ALLOCATE
  ↓
QUANT-ADJUST EXPRESSION
  ↓
UPDATE / IGNITE / CONVERT
  ↓
HARVEST
  ↓
COMPARE
  ↓
ROTATE
  ↓
REALLOCATE
  ↓
COMPOUND
```

---

## Release state

The execution-facing allocator remains **BLOCKED / FAIL CLOSED** because a genuine real-data no-trade replay PASS on the frozen approved cohort is absent under the current external runner/payload constraints.

The terminology change does not weaken any Quant parameter, readiness contract, authority rule, or release gate.

---

## Primary system test

The system is successful only if it improves **compounded capital growth**, not merely stock-ranking accuracy.

Required conceptual benchmark ladder:

1. buy/hold
2. Quant only
3. Quality Qualifier only
4. Quality Qualifier + generic timing
5. Quality Qualifier + full TTC causal clocks
6. TTC + Quant expression
7. full dynamic system through the OSE ↔ Quant interface

Backtests must be point-in-time and prevent look-ahead and survivorship bias.

Final objective:

> **MAXIMIZE COMPOUNDED CAPITAL BY FIRST QUALIFYING WHAT IS WORTH OWNING, THEN DIRECTING CAPITAL TOWARD THE QUALIFIED OPPORTUNITY WITH THE STRONGEST TIME-ADJUSTED, PROBABILITY-ADJUSTED REMAINING PAYOFF.**