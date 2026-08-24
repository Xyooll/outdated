# RSS Intelligence Layer

RSS is the low-cost radar. It detects new information; deeper research verifies and enriches it.

## Pipeline

feed -> ingest -> normalize -> deduplicate -> classify -> score -> enrich -> store -> alert

## Initial source classes

- SEC / EDGAR
- DoD
- SAM.gov
- Federal Reserve
- DARPA
- CFTC
- NASA
- FDA
- DOE / EIA / FERC
- USGS
- Federal Register

## Item scoring

Priority should combine impact, novelty, relevance, time sensitivity and source confidence. Never treat an RSS headline as verified fact without evidence from the underlying source.

## Feed record

Each feed should use `schemas/source.yaml`. Each normalized item should reference its source and create an event when it represents a material change.
