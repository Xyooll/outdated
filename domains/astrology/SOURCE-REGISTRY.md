# Xyool Astrology — Source Registry

Status: **EXPERIMENTAL DOMAIN CANONICAL / SOURCE PROVENANCE AUTHORITY**

Purpose: separate calculation authorities, tradition sources, modern-system sources, user-derived frameworks, and Xyool hypotheses so provenance never masquerades as predictive validation.

Core rule:

> **Source authority answers “what is the rule/data?”; validation answers “does it work for the claimed purpose?”**

---

## 1. Source classes

```text
CALCULATION_PRIMARY
CALCULATION_CROSSCHECK
TIMEZONE_PRIMARY
ASTRONOMICAL_CATALOGUE
LIVING_TRADITION
FOUNDATIONAL_TRADITION_TEXT
SCHOLARLY_SECONDARY
ESTABLISHED_PRACTITIONER_SECONDARY
MODERN_SYSTEM_PRIMARY
USER_DERIVED_FRAMEWORK
XYOOL_HYPOTHESIS
FREE_FORM_SYNTHESIS
```

---

## 2. Calculation anchors

### JPL Horizons

```text
source_id: src.jpl.horizons
class: CALCULATION_PRIMARY
scope: solar-system ephemerides / observer-dependent positions
provider: NASA Jet Propulsion Laboratory Solar System Dynamics
canonical_locator: https://ssd.jpl.nasa.gov/horizons/
```

Use as a high-authority astronomical reference/cross-check for solar-system positions and timing. Record query settings, coordinate center, time scale, and output type.

### Swiss Ephemeris

```text
source_id: src.astro.swisseph
class: CALCULATION_PRIMARY / CALCULATION_CROSSCHECK
scope: astrology-oriented planetary, lunar, fixed-star, time-conversion, and house calculations
provider: Astrodienst / Swiss Ephemeris project
canonical_locator: https://www.astro.com/swisseph/
```

Version-lock the library/data. Record ephemeris mode, flags, time scale, sidereal settings, and house system. Licensing requirements must be respected by any deployed implementation.

### IANA Time Zone Database

```text
source_id: src.iana.tzdb
class: TIMEZONE_PRIMARY
scope: historical civil-time offsets and DST rules
provider: IANA tz database
canonical_locator: https://www.iana.org/time-zones
```

Record tzdb version for reproducibility. Historical pre-1970 data may have locality-specific limitations; preserve uncertainty when records are incomplete.

### SIMBAD / CDS

```text
source_id: src.cds.simbad
class: ASTRONOMICAL_CATALOGUE
scope: identifiers, coordinates, bibliography, measurements for astronomical objects outside the solar system
provider: CDS, Strasbourg
canonical_locator: https://simbad.cds.unistra.fr/
```

SIMBAD itself states that it is a database rather than a catalogue. For reproducible fixed-star work, preserve the underlying cited catalogue/measurement and epoch where material; use VizieR or the original catalogue when a catalogue identity is required.

---

## 3. Maya traditional/living anchors

### Smithsonian — Living Maya Time

```text
source_id: src.smithsonian.living_maya_time
class: LIVING_TRADITION / SCHOLARLY_SECONDARY
scope: Maya calendar system, living calendar-keeper context, Tzolk'in/Chol Q'ij, Haab, Calendar Round, Long Count
provider: Smithsonian National Museum of the American Indian
canonical_locator: https://maya.nmai.si.edu/calendar
```

### Smithsonian Maya Calendar Converter

```text
source_id: src.smithsonian.maya_converter
class: CALCULATION_CROSSCHECK
scope: Gregorian ↔ Maya Long Count / Tzolk'in / Haab conversion
canonical_locator: https://maya.nmai.si.edu/calendar/maya-calendar-converter
```

Use as a reference cross-check rather than silently treating one converter as the definition of every Maya regional practice.

For day meanings, record the named language/community/Day Keeper or document source rather than flattening all Maya traditions into one dictionary.

---

## 4. Dreamspell primary anchor

### Foundation for the Law of Time / Law of Time materials

```text
source_id: src.lawoftime.dreamspell
class: MODERN_SYSTEM_PRIMARY
scope: Dreamspell / 13 Moon / 20 Solar Seals / 13 Galactic Tones / Wavespell concepts
canonical_locator: https://lawoftime.org/
```

Store under `DREAMSPELL.ARGUELLES`, never as evidence of historical/living Maya calendrical meaning.

---

## 5. Western and traditional astrology sources

Do not create one universal source list that pretends modern Western, Hellenistic, medieval, Renaissance, and contemporary traditions are the same.

Each imported rule should name:

```text
author / source tradition
work / edition / translation
rule location if practical
modern commentary source if used
whether Xyool is using the source directly or through a secondary synthesis
```

A modern web interpretation does not become “traditional” because it describes an old technique.

---


## 5A. Western story-grammar v1 source anchors

These sources support the first bounded Western Tropical Xyool story grammar. They establish provenance for conventions/rules, not predictive efficacy.

### Astrodienst — Whole Sign Houses

~~~text
source_id: src.astro.whole_sign_houses
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Overview house systems / Whole Sign Houses
provider: Astrodienst
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/faq/fq_fh_owhouse_e.htm
scope: whole-sign house calculation convention
limitations: convention/source authority only; does not validate predictive efficacy
~~~

### Astrodienst — Houses

~~~text
source_id: src.astro.houses
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: House
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/astrowiki/en/House
scope: broad house/life-area significations
limitations: broad modern synthesis; not a single ancient/traditional rulebook
~~~

### Astrodienst — Planets

~~~text
source_id: src.astro.planets
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Planet
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/astrowiki/en/Planet
scope: broad planetary functions/significations
limitations: broad modern synthesis; not predictive validation
~~~

### Astrodienst — Aspects

~~~text
source_id: src.astro.aspects
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Aspect / Brief Introduction to Aspects
provider: Astrodienst
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/astrowiki/en/Aspect
scope: major aspect geometry; applying/separating distinction; broad harmonious/challenging classification
limitations: orb practice varies by technique/tradition
~~~

### Astrodienst — Transits

~~~text
source_id: src.astro.transits
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Transit
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/astrowiki/en/Transit
scope: transit definition, exact-contact activation convention, small-orb starting guidance, slow-vs-fast transit distinction
limitations: interpretive convention; claimed effects remain validation required
~~~

### Astrodienst — Classical sign rulers

~~~text
source_id: src.astro.classical_rulers
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Ruler / Classical ruler
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-24
canonical_locator: https://www.astro.com/astrowiki/en/Ruler
scope: traditional seven-planet sign rulerships used by the profection component
limitations: modern and traditional rulership systems differ; this v1 explicitly uses classical rulers for profections
~~~

### The Astrology Podcast — Annual Profections

~~~text
source_id: src.tap.profections153
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V1
title: Annual Profections: An Ancient Time-Lord Technique
author_or_provider: Chris Brennan / The Astrology Podcast
retrieved_at: 2026-09-24
canonical_locator: https://theastrologypodcast.com/transcripts/ep-153-annual-profections-an-ancient-time-lord-technique/
scope: one-sign-per-year annual profection cycle, lord-of-year selection, transit-priority rules for the activated lord/sign
limitations: modern practitioner reconstruction/use of an ancient technique; efficacy remains validation required
~~~


## 5B. Full-chart / asteroid source anchors

These sources support the bounded full-chart aggregation added in Western Story v2. Asteroid use is treated as a lower-authority modern layer and is not allowed to create unlimited post-hoc matches.

### Astrodienst — Houses / House Rulers / House Axes

~~~text
source_id: src.astro.house_rulers
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V2
title: House Ruler / House Axis
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-25
scope: sign-on-house rulership links, dispositor links, opposite-house axis themes
limitations: interpretive convention; schools differ
~~~

### Astrodienst — Asteroids overview

~~~text
source_id: src.astro.asteroids_overview
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V2
title: Asteroid / Planetoid
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/astrowiki/en/Planetoid
scope: modern Western use of asteroids; first four major asteroids; limits/debate around asteroid interpretation
limitations: asteroid interpretation is comparatively recent, heterogeneous, and vulnerable to overfitting when large numbers of objects are admitted
~~~

### Astrodienst — Asteroid chart factors

~~~text
source_id: src.astro.asteroid_chart_factors
class: CALCULATION_CROSSCHECK / ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V2
title: Astrodienst with asteroids / extra chart factors
provider: Astrodienst
retrieved_at: 2026-09-25
scope: commonly surfaced additional objects including Ceres, Pallas, Juno, Vesta, Chiron, Pholus, Nessus, and Eros
limitations: availability in chart software does not itself establish interpretive validity
~~~

### Astrodienst — Ceres / Pallas / Juno / Vesta / Chiron / Eros

~~~text
source_id: src.astro.asteroid_meanings_core
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.WT.XYOOL_STORY_V2
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-25
scope:
  Ceres: nurturing, sustenance, care, letting-go themes
  Pallas: strategy, creative intelligence, pattern/craft themes
  Juno: commitment, relationship ideals, partnership-contract themes
  Vesta: focus, dedication, service, concentrated commitment themes
  Chiron: modern centaur/healing-wound symbolism
  Eros: erotic attraction, passion, desire, creative/relational intensity
limitations: modern interpretive layer; meanings are not treated as empirically validated
~~~


## 5C. Star Astrology / degree-field source anchors

These sources support the astronomical coordinate layer for the user-derived Star Astrology framework. They do not establish intrinsic degree symbolism or predictive efficacy.

### Astrodienst — Fixed Star List

~~~text
source_id: src.astro.fixed_star_list
class: CALCULATION_CROSSCHECK / ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
title: Astrodienst Fixed Stars list
provider: Astrodienst / Swiss Ephemeris
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/swisseph/fstarlist.htm
scope: fixed-star identities available to Swiss Ephemeris/Astrodienst
limitations: list availability does not establish astrological meaning
~~~

### Astrodienst — Fixed Star overview

~~~text
source_id: src.astro.fixed_star_overview
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
title: Fixed Star
provider: Astrodienst Astrowiki
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/astrowiki/en/Fixed_Star
scope: fixed-star astronomy overview, precession relative to tropical zodiac, ecliptic longitude/latitude, magnitude, small-orb practitioner convention
limitations: interpretive content is practitioner tradition; efficacy remains validation required
~~~

### Astrodienst — Precession / tropical coordinate clarification

~~~text
source_id: src.astro.precession
class: CALCULATION / COORDINATE REFERENCE
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
title: Precession
provider: Astrodienst
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/faq/fq_ua_precession_e.htm
scope: tropical zodiac degrees as ecliptic-longitude sectors measured from the equinox; fixed-star background shifts relative to tropical longitude through precession
limitations: coordinate reference only; no degree symbolism implied
~~~

### Astrodienst — Fixed Stars chart style

~~~text
source_id: src.astro.fixed_star_chart_style
class: CALCULATION_CROSSCHECK / METHOD REFERENCE
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
title: Astrodienst Fixed Stars chart style
provider: Astrodienst
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/cgi/h.cgi?f=gch&h=gchafz&lang=e
scope: example of preserving star longitude/latitude, true angles, axes, parans, and nearby-star reporting
limitations: software display convention; not an efficacy claim
~~~

## 6. Jyotish sources

Jyotish rules should preserve lineage/text/method identity where material.

For each rule record, as relevant:

```text
text / author / school
translation / edition
ayanamsha assumption
house/bhava convention
nakshatra scheme
dasha system
Panchang convention
modern practitioner synthesis if used
```

Do not cite “Vedic astrology” as though it were one rulebook.

---

## 7. Fixed-star sources

Separate:

```text
ASTRONOMICAL STAR DATA
coordinates / proper motion / epoch / identifiers
```

from:

```text
ASTROLOGICAL STAR MEANINGS
traditional or modern interpretive source
```

A precise star position does not validate an astrological star interpretation.

---

## 8. Source record requirements

Every material source should have:

```yaml
source_id:
source_class:
system_id:
title:
author_or_provider:
version_or_edition:
published_at:
retrieved_at:
locator:
content_hash_if_local:
scope:
limitations:
```

---

## 9. Source conflict

When two calculation sources disagree materially:

```text
DO NOT AVERAGE
→ identify settings/time scale/reference frame/version differences
→ reproduce each result
→ resolve if possible
→ otherwise mark CALCULATION CONFLICT / BLOCKED
```

When two interpretive traditions disagree:

```text
preserve both under separate rule IDs
```

Do not force a consensus merely to simplify synthesis.

---

## 10. Version pinning

For reproducibility pin, where applicable:

```text
tzdb version
ephemeris/library version
JPL ephemeris family / query settings
star catalogue / epoch
Maya converter/correlation identity
Dreamspell implementation version
translation/edition of interpretive text
```

---

## 11. Provenance confidence versus efficacy confidence

Maintain two separate questions:

```text
PROVENANCE CONFIDENCE
How confident are we that this rule/data accurately represents the named source/system?

EFFICACY CONFIDENCE
How much controlled evidence supports using the rule for this descriptive/predictive purpose?
```

A source can be perfectly authentic and empirically unvalidated.

Final rule:

> **Never let “ancient,” “traditional,” “official,” or “precisely calculated” silently answer the separate question of predictive validity.**

---

## 12. Deep Research source expansion — Star Astrology / full-chart v2

These records were added from the 2026-09-25 Deep Research pass. They support provenance, calculation, and validation design; they do not by themselves establish astrological efficacy.

### Ptolemy — Tetrabiblos I.9 fixed stars

~~~text
source_id: src.ptolemy.tetrabiblos.i9
class: FOUNDATIONAL_TRADITION_TEXT
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
author: Claudius Ptolemy
work: Tetrabiblos
book_chapter: I.9
translation: F. E. Robbins (Loeb, 1940) as surfaced by University of Chicago LacusCurtius
retrieved_at: 2026-09-25
canonical_locator: https://penelope.uchicago.edu/thayer/e/roman/texts/ptolemy/tetrabiblos/1b%2A.html
scope: historical fixed-star planetary analogies and tropical-zodiac context
limitations: historical source authority only; no empirical validation; later traditions may differ
~~~

### Sabian Symbols lineage

~~~text
source_id: src.astro.sabian_symbols
class: ESTABLISHED_PRACTITIONER_SECONDARY
system_id: ASTRO.STAR.DEGREE.XYOOL_V1
retrieved_at: 2026-09-25
canonical_locator: https://www.astro.com/astrowiki/en/Sabian_Symbols
scope: modern 360-degree symbolic lineage originating with Marc Edmund Jones / Elsie Wheeler
limitations: source-lineage reference; corpus variants must be versioned separately; efficacy unvalidated
~~~

### IAU SOFA

~~~text
source_id: src.iau.sofa
class: CALCULATION_PRIMARY
scope: reference astronomical transformations including precession/nutation
provider: International Astronomical Union SOFA service
retrieved_at: 2026-09-25
canonical_locator: https://www.iausofa.org/current-software
limitations: calculation authority only; no astrological meaning
~~~

### Gaia DR3

~~~text
source_id: src.gaia.dr3
class: ASTRONOMICAL_CATALOGUE
scope: stellar astrometry / proper motion / reference epoch J2016.0
provider: ESA Gaia
retrieved_at: 2026-09-25
canonical_locator: https://www.cosmos.esa.int/web/gaia/dr3
limitations: stellar-state authority only; later Gaia releases require explicit catalog migration
~~~

### ESA Gaia release schedule

~~~text
source_id: src.esa.gaia_release_schedule
class: ASTRONOMICAL_CATALOGUE / RELEASE-SCHEDULE
scope: future Gaia data-release timing
provider: European Space Agency
retrieved_at: 2026-09-25
canonical_locator: https://www.esa.int/About_Us/Corporate_news/ESA_s_highlights_for_2026
limitations: time-sensitive planning source; refresh before migration work
~~~

### JPL Small-Body Database / orbit service

~~~text
source_id: src.jpl.sbdb
class: CALCULATION_PRIMARY
scope: current small-body orbital solutions / uncertainty context
provider: NASA JPL Solar System Dynamics
retrieved_at: 2026-09-25
canonical_locator: https://ssd.jpl.nasa.gov/sb/orbits.html
limitations: solutions update as new astrometry arrives; retrieval timestamp and solution identity are material
~~~

### Minor Planet Center Orbits API

~~~text
source_id: src.mpc.orbits_api
class: CALCULATION_CROSSCHECK
scope: minor-body designation, orbit elements, uncertainty/covariance metadata
provider: Minor Planet Center
retrieved_at: 2026-09-25
canonical_locator: https://docs.minorplanetcenter.net/tutorials/notebooks/mpc_tutorial_api_orbits/
limitations: identity/orbit authority; not interpretive authority
~~~

### Carlson double-blind astrology test

~~~text
source_id: src.empirical.carlson1985
class: SCHOLARLY_SECONDARY
scope: controlled test of natal-chart/personality interpretation
title: A double-blind test of astrology
publication: Nature 318, 419–425 (1985)
canonical_locator: https://www.nature.com/articles/318419a0
limitations: tests a particular form of natal astrology, not Xyool Star Astrology directly
~~~

### Fourie et al. complete-chart study

~~~text
source_id: src.empirical.fourie1980
class: SCHOLARLY_SECONDARY
scope: complete-chart/personality evaluation and inter-astrologer agreement
canonical_locator: https://journals.sagepub.com/doi/10.1177/008124638001000308
limitations: historical controlled study; does not directly test Xyool systems
~~~

### Wyman / Vyse double-blind experiment

~~~text
source_id: src.empirical.wyman_vyse2008
class: SCHOLARLY_SECONDARY
scope: double-blind astrological/personality matching and Barnum-effect considerations
canonical_locator: https://pubmed.ncbi.nlm.nih.gov/18649494/
limitations: does not directly test Xyool Star Astrology
~~~

### Proper scoring rules

~~~text
source_id: src.stats.gneiting_raftery2007
class: SCHOLARLY_SECONDARY
scope: proper scoring rules for probabilistic forecasts, including Brier/log-score framework
canonical_locator: https://doi.org/10.1198/016214506000001437
limitations: statistical methodology source, not astrology evidence
~~~

### OSF preregistration guidance

~~~text
source_id: src.osf.preregistration
class: SCHOLARLY_SECONDARY / METHOD REFERENCE
scope: timestamped preregistration / immutable research-plan concepts
canonical_locator: https://help.osf.io/article/330-welcome-to-registrations
limitations: method reference; Xyool may implement equivalent internal freezing without using OSF
~~~

## 13. Orthogonal authority dimensions

For Star Astrology v2, retain separate fields where practical:

~~~text
ASTRONOMICAL AUTHORITY
HISTORICAL / TRADITION SOURCE AUTHORITY
MODERN PRACTITIONER SOURCE AUTHORITY
USER-DERIVED / XYOOL HYPOTHESIS
EMPIRICAL SUPPORT FOR SCOPE
~~~

Do not flatten these into one rank.

A Ptolemaic rule can be high-confidence historical provenance and zero-confidence predictive efficacy at the same time.


---

## 14. Intrinsic-degree research sources — local 30 + absolute 360

### Greenbaum & Jones — P.Berl. 9825 / monomoiriai

~~~text
source_id: src.scholar.greenbaum_jones2017_monomoiria
class: SCHOLARLY_SECONDARY
title: P.Berl. 9825: An elaborate horoscope for 319 CE and its significance for Greek astronomical and astrological practice
authors: Dorian Greenbaum / Alexander Jones
published_at: 2017
retrieved_at: 2026-09-25
canonical_locator: https://archive.nyu.edu/bitstream/2451/49543/4/Greenbaum%20and%20Jones%202017%20PBerl%209825%20ISAW%20Papers.pdf
scope: historical evidence for monomoiriai / single-degree rulers and Paulus sign-based method
limitations: historical-practice evidence; does not validate efficacy
~~~

### Ema Kurent — monomoiria practitioner synthesis

~~~text
source_id: src.secondary.kurent_monomoiria
class: ESTABLISHED_PRACTITIONER_SECONDARY
title: Monomoiria: Essential Dignity by Degree
author: Ema Kurent
published_at: 2017
retrieved_at: 2026-09-25
canonical_locator: https://www.emakurent.com/en/2017/02/09/monomoiria-essential-dignity-by-degree/
scope: modern synthesis of Paulus / Valens degree-ruler methods; sign-based and trigonal variants
limitations: secondary interpretation of ancient material; efficacy unvalidated
~~~

### Ptolemy — Tetrabiblos I.22 witness to degree rulership

~~~text
source_id: src.ptolemy.tetrabiblos.i22_degree_rulership_witness
class: FOUNDATIONAL_TRADITION_TEXT
author: Claudius Ptolemy
work: Tetrabiblos
book_chapter: I.22
translation: F. E. Robbins
retrieved_at: 2026-09-25
canonical_locator: https://penelope.uchicago.edu/thayer/e/roman/texts/ptolemy/tetrabiblos/1b%2A.html
scope: historical witness that some astrologers assigned individual degrees to planets in Chaldean order
limitations: Ptolemy explicitly criticizes/omits the method; use as historical witness, not endorsement
~~~

### Modern Degree Theory — Astrology.com secondary reconstruction

~~~text
source_id: src.modern.degree_theory.astrology_com
class: ESTABLISHED_PRACTITIONER_SECONDARY
named_lineage: Nikola Stojanovic Degree Theory
retrieved_at: 2026-09-25
canonical_locator: https://www.astrology.com/article/degree-theory-astrology/
scope: modern 0–29 local-degree symbolism and critical-degree discussion
limitations: secondary source; primary Stojanovic text not yet recovered by Xyool
~~~

### Modern Degree Theory — Augurine secondary reconstruction

~~~text
source_id: src.modern.degree_theory.augurine
class: ESTABLISHED_PRACTITIONER_SECONDARY
named_lineage: Nikola Stojanovic Degree Theory
retrieved_at: 2026-09-25
canonical_locator: https://www.augurine.com/degree-theory
scope: 0–29 local-degree mapping; 0° treated as host-sign amplifier; 1°→Aries sequence
limitations: secondary source; indexing conflicts exist across modern summaries
~~~

### Charubel / Sepharial — Degrees of the Zodiac Symbolized

~~~text
source_id: src.degree.charubel_sepharial
class: MODERN_SYSTEM_PRIMARY / HISTORICAL_DEGREE_CORPUS
authors: Charubel (John Thomas) / Sepharial (Walter Gorn Old)
work: The Degrees of the Zodiac Symbolized
first_publication_period: 1890s
retrieved_at: 2026-09-25
canonical_locator: https://books.google.com/books/about/Degrees_of_the_Zodiac_Symbolized.html?id=qth56M-rQUMC
scope: two 360-degree symbolic corpora including Charubel and La Volasfera/Sepharial material
limitations: corpus authorship/provenance differs by section; efficacy unvalidated
~~~

### Kozminsky — Zodiacal Symbology

~~~text
source_id: src.degree.kozminsky1917
class: MODERN_SYSTEM_PRIMARY / HISTORICAL_DEGREE_CORPUS
author: Isidore Kozminsky
work: Zodiacal Symbology and Its Planetary Power
published_at: 1917
retrieved_at: 2026-09-25
canonical_locator: https://books.google.com/books/about/Zodiacal_Symbology_and_Its_Planetary_Pow.html?id=JtwuDwAAQBAJ
scope: 360 degree symbols plus planetary attributions
limitations: author's empirical claims are not treated as validated evidence
~~~

### Janduz — 360 symbolic degrees secondary record

~~~text
source_id: src.degree.janduz_secondary
class: SCHOLARLY_SECONDARY / PRACTITIONER_SECONDARY
author: Jeanne Duzéa (Janduz)
work: Les 360 degrés du Zodiaque
published_at: early 1930s / later editions
retrieved_at: 2026-09-25
canonical_locator: https://www.astrotheme.com/the_360_symbolic_degrees.php
scope: Janduz 360-degree lineage; later synthesis influenced by La Volasfera, fixed stars and Kabbalistic material
limitations: current locator is a modern rewritten secondary presentation; dependency on earlier corpora must be preserved
~~~

## 15. Degree-corpus source dependency

Do not treat all degree corpora as independent evidence.

Known/claimed dependencies include:
- Sabian Symbols are a separate 1925 Jones/Wheeler lineage, later reworked by Rudhyar;
- Janduz materially reworked La Volasfera and therefore is not independent of it;
- modern Degree Theory is a separate 0–29 local-degree lineage and must not be conflated with 360 symbol corpora;
- monomoiria is an ancient planetary degree-rulership method, not a symbolic-image corpus.

Intrinsic-meaning synthesis must preserve these lineages.
