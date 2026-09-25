# ASTRO-LIB-ASTRONOMICAL-FOUNDATION

TYPE: DOMAIN FACT / CALCULATION METHOD
STATUS: **SOURCE-GROUNDED / DOMAIN-ESTABLISHED FOR CALCULATION POLICY**
SCOPE: all Astrology systems using astronomical positions
LAST REVIEWED: 2026-09-25

## Core separation

Keep three layers distinct:
- astronomical state: what object was where, at what epoch/frame, under which ephemeris/catalog;
- astrological semantics: what a declared system/source says that state means;
- empirical status: whether that rule survived controlled/prospective testing.

Astronomical precision does not validate astrological interpretation.

## Canonical calculation policy

For solar-system objects:
- deterministic local runtime candidate: Swiss Ephemeris;
- independent high-authority cross-check: JPL Horizons / SBDB;
- preserve time scale, observer center, coordinate frame, flags, and ephemeris version.

For stellar objects:
- operational star data may use Swiss Ephemeris / Astrodienst;
- independent stellar audit should use a named astrometric catalog such as Gaia DR3;
- preserve catalogue release, identity, reference epoch, proper motion where material;
- use IAU-compatible precession/nutation transformations.

## Degree-field rule

DEGREE ADDRESS + EPOCH / DATE + COORDINATE FRAME -> STELLAR NEIGHBORHOOD.

Never store a permanent identity such as '29° Leo = Regulus forever' without epoch-aware calculation.

## Required state

object_id; timestamp/JD; time_scale; observer_center; longitude; latitude if applicable; RA/Dec when used; coordinate_frame; epoch; ephemeris/catalog version; flags; uncertainty when material.

## Failure boundaries

Return BLOCKED / CALCULATION_CONFLICT when timezone/time precision, frame, ephemeris/catalog identity, or authoritative calculation agreement is materially unresolved.

## Freshness

- historical astrology text: stable / edition-sensitive;
- Swiss/JPL engine/data: release-sensitive;
- small-body orbit solutions: dynamic;
- stellar catalogue: data-release sensitive.

Calculation policy may be established while astrological efficacy remains unvalidated.