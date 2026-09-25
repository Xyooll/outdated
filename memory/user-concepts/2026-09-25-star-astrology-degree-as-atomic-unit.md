# Star Astrology — Degree as the Atomic Astrological Unit

DATE: 2026-09-25
STATUS: **ACTIVE / USER-DERIVED ASTROLOGY FRAMEWORK**

## USER-STATED

> "My thought is that astrology should be done at the degree level. Instead of just being seen as a degree in a specific house, zodiac or decan, the degree its self is just as informative. I call it star astrology as the degrees line up with the stars"

## CONCEPT

Treat the exact astrological degree as a first-class information object rather than merely a coordinate nested inside sign, house, decan, or another larger partition.

Working correspondence:

~~~text
EXACT DEGREE
= atomic sky address

SIGN / HOUSE / DECAN
= contextual wrappers around that address

STARS
= stellar field / neighborhood associated with the address under a declared coordinate frame and epoch

PLANETS / ANGLES / ASTEROIDS
= occupants or moving activators of degree addresses
~~~

## ASTRONOMICAL CLARIFICATION

This framework must distinguish:
- an intrinsic/symbolic meaning assigned to a degree by the user/Xyool framework;
- the actual fixed-star neighborhood around that longitude.

In a tropical zodiac, degrees are measured from the equinox and fixed-star longitudes shift relative to tropical degrees mainly through precession. A degree therefore does not permanently correspond one-to-one with one fixed star.

The model should preserve coordinate frame, epoch/date, stellar latitude, and star identity rather than flattening "degree = star."

## SYSTEM CONSEQUENCE

Develop a bounded Star Astrology layer in which:
- exact ecliptic longitude is first-class;
- degree-level information is preserved before sign/house/decan compression;
- fixed-star neighborhood is calculated explicitly;
- larger zodiacal structures remain contextual wrappers;
- asteroids and other points can participate through the same degree-address representation;
- degree meaning and star meaning remain separable for validation;
- predictive tests can ask whether degree/star information adds signal beyond sign/house/aspect baselines.

## OPEN QUESTION

Does the degree itself contain reusable predictive/descriptive information after controlling for:
- sign;
- house;
- decan;
- planetary identity;
- aspect structure;
- nearby fixed stars?

This should be tested rather than assumed.

## RELATED

- `../../domains/astrology/SYSTEM-REGISTRY.md`
- `../../domains/astrology/DEPENDENCY-GRAPH.md`
- `../../domains/astrology/library/open-questions/full-chart-aggregation-v2.md`
