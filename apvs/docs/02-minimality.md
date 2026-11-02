---
layout: default
title: "Chapter 2: Minimality"
nav_order: 3
---

# Chapter 2. Minimality

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance and verification text (shaded and in italics below) are in beta. Requirement type is waiting for community comments, and the chapter and section introductions are in beta as well. Wording will keep moving as feedback arrives.
</div>

Defines how little personal data an application needs to collect, derive and keep in order to fulfill each documented purpose, and how to verify that it holds no more than that. It exists because data that is never collected cannot leak, be misused or be demanded later.

## About this chapter

Minimality is the state a system is in when, for every feature, the personal data present in collection, processing and storage matches what the documented purpose requires, and nothing beyond it. It is the state an assessor can observe in a running application, and it results from the minimization work a team does during design reviews and cleanups. This chapter is written around that state. Its requirements describe what a verifier should be able to find, and they treat the data and the way it is used as a pair, since the same field can be necessary for one feature and surplus for another.

The reasoning is practical. Every additional attribute, every extra digit of precision and every month of retained history widens the set of things that can be breached, subpoenaed, repurposed or combined with other data to identify someone. Data that was never collected cannot be leaked, and a coarser value is usually enough to make a feature work. The chapter also reflects an uncomfortable habit of software projects, which is that data gathered because it might be handy tends to stay around long after anyone remembers why.

Three principles run through the requirements. The first is necessity, so an element belongs in the system only when removing it would stop the purpose from being fulfilled. The second is sufficiency of form, which asks that each necessary element be held at the lowest precision, narrowest scope and smallest volume that still serves the purpose, and that this form degrade further as the data ages. The third is consistency, so that inferred and derived data face the same limits as data collected directly, and optional data is genuinely optional in the backend as well as on the screen.

For developers and architects, the working method is to start from the documented purpose, choose the least detailed level that keeps the feature functional, write down why a lower level would not do, and then check the code, schemas, logs, caches and exports against that decision. The chapter gives ordered scales for common data classes to make this concrete. Because minimality constrains every moment in the data lifecycle, from collection through deletion, this chapter applies to all phases, and Chapter 3 then applies it to each phase in turn.

## Sections at a glance

| Section | Title | Requirements | <span style="color:#1a7f37">L1</span> | <span style="color:#9a6700">L2</span> | <span style="color:#8250df">L3</span> |
|---|---|---:|---:|---:|---:|
| [2.1](#section-2-1) | Minimization by Necessity | 7 | 2 | 3 | 2 |
| [2.2](#section-2-2) | Data Class Granularity | 7 | 0 | 7 | 0 |

---

<a id="section-2-1"></a>
## 2.1 Minimization by Necessity

This section establishes the general tests for minimality. It asks whether each data element is necessary, whether it is held in its least detailed form, and whether that judgment is revisited when a purpose changes, ends, or produces derived and aggregated data.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [2.1.1](#req-2-1-1) | Necessity of each data element | 🟢 L1 | `APP` |
| [2.1.2](#req-2-1-2) | Minimum sufficient data | 🟢 L1 | `APP` |
| [2.1.3](#req-2-1-3) | Necessity reassessment on change or retirement | 🟡 L2 | `APP` |
| [2.1.4](#req-2-1-4) | Derived data precision | 🟣 L3 | `APP` |
| [2.1.5](#req-2-1-5) | Optional data not functionally mandatory | 🟡 L2 | `APP` |
| [2.1.6](#req-2-1-6) | Abstract and aggregate | 🟡 L2 | `APP` |
| [2.1.7](#req-2-1-7) | Granularity degradation over time | 🟣 L3 | `APP` |

<a id="req-2-1-1"></a>
### 2.1.1 Necessity of each data element

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Limit the personal data elements collected, processed, or stored to those necessary for their documented purpose. Exclude elements that merely enhance or enrich the processing.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"Useful but not necessary" is the key distinction. If removing the element would prevent the purpose from being fulfilled, it is necessary. If it merely enhances or enriches the processing, it is not.

Define purposes first, then define minimal data requirements to fulfill that purpose. Refer to "Purpose specificity" in Chapter 1.

Info: This requirement covers "do we need this (blob of) data". 2.1.2 looks at the data items in the blob

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each data element, confirm it is required for — not merely useful to — the documented purpose. Elements that are useful but not required are findings.

</div>

<a id="req-2-1-2"></a>
### 2.1.2 Minimum sufficient data

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

For each necessary personal data element, use the minimum sufficient form: the least data, coarsest granularity, and narrowest volume, frequency, and population that still fulfil the purpose, including no personal data at all where the feature can be redesigned to avoid it.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Info: Minimal refers to limited both in data types, granularity, encoding (including embedded metadata), volume, frequency, and data subjects.  
(this is a refinement of 2.1.1 by looking specifically at each data item/attribute for the 'data (type/element)' deemed necessary in 2.1.1

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each data element, reviewer assesses whether a reduced dataset or lower precision would still fulfil the purpose. If yes and no justification is recorded, that is a finding.

</div>

<a id="req-2-1-3"></a>
### 2.1.3 Necessity reassessment on change or retirement

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

When a processing activity changes or is retired, the necessity of each associated personal data element must be reassessed. Elements no longer necessary for the updated activity, or for any remaining active purpose, must be removed from collection, processing, and storage, and existing values deleted within a defined and enforced period.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This is when the overall process changes, the underlying purpose changes, ... beyond regularly data lifecycle  evolution

Retiring a purpose (feature sunset, project closure, contract end) is the limiting case of change. Data that also serves another active purpose stays, but is then bound to that purpose only. Deletion uses the Chapter 3 mechanisms (3.3.2 residual window, 3.5 deletion); the period must be defined and enforced, not open-ended.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review system change records or release history against the purpose register. Any change with no corresponding necessity reassessment, or elements retained after a change makes them unnecessary, are findings.  
Inspect: sample retired features or purposes from the change history. Confirm the collection field or endpoint was removed and stored values were deleted, or re-bound to a remaining active purpose. Continued collection after retirement is a finding.

</div>

<a id="req-2-1-4"></a>
### 2.1.4 Derived data precision

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Hold inferred and derived personal data to the same necessity, precision, and granularity limits as directly collected data.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

If collecting precise coordinates is not permitted, inferring them from coarser data is equally not permitted.  
E.g. inferring health status from purchases.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each inferred element, assess whether direct collection of an equivalent element would satisfy the necessity test. If not, the inference is a finding.

</div>

<a id="req-2-1-5"></a>
### 2.1.5 Optional data not functionally mandatory

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Ensure all core functionality works when optional personal data elements are not provided.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Common implementation gap: fields marked optional in the UI but required by backend logic.

e.g. downloading an app where during use of core functionality, suddenly the 'optional' location data or access to camera is still required

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: attempt core functionality with all optional fields left empty. Any degradation or blocking of core functionality is a finding.  
Test: API calls with the optional fields omitted or null must also succeed.

</div>

<a id="req-2-1-6"></a>
### 2.1.6 Abstract and aggregate

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where aggregated or de-identified output satisfies the processing purpose, generate it at the minimum sufficient granularity and discard the raw personal data from which it was derived.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Note that aggregated is not the same as anonymous. Small cell sizes and differencing attacks can still re-identify people.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review the pipelines for aggregation steps, confirm raw inputs are purged afterwards, and check the output against a minimum cell size.

</div>

<a id="req-2-1-7"></a>
### 2.1.7 Granularity degradation over time

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Reduce the granularity of retained longitudinal personal data on a defined schedule as it ages, to the minimum resolution sufficient for the purpose at each age.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Longitudinal personal data — data where the combination or sequence of data points reveals information that individual points would not — carries qualitatively different privacy risk from individual data points. A single location coordinate is low-sensitivity; weeks of location data reveals home address, workplace, and behavioural patterns. The necessity test must therefore be applied to the accumulated history as a whole, not only to individual data points in isolation. Progressive granularity reduction is the expected implementation: precise coordinates may be necessary today, city-level sufficient after a week, country-level after a month.

The system must progressively reduce the granularity of personal data retained across multiple points in time as that data ages. The resolution at which historical data is retained must decrease to the minimum sufficient for the processing purpose over time.  
The system must not retain historical data points at full resolution even if recent data requires higher resolution.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Verify by: identify datasets where personal data is retained across multiple points in time. For each, confirm a defined point exists at which raw data is reduced — through aggregation, de-identification, or deletion. Any longitudinal dataset retained indefinitely in raw form where a coarser representation would suffice is a finding.

</div>

---

<a id="section-2-2"></a>
## 2.2 Data Class Granularity

This section provides ordered scales of granularity for data classes that commonly carry more detail than a feature needs, such as location, age, identity, media and file metadata, communication history and live streams. Teams select the least precise level at which each feature still works and record why a lower one would not suffice. The scales are examples and defaults, so apply them to your own context and customize them where it makes sense. Consider outliers that would disclose a specific identity, such as the elevation of a space station as a location value, or the velocity and direction of change in a series of coordinates.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [2.2.1](#req-2-2-1) | Location data granularity | 🟡 L2 | `APP` |
| [2.2.2](#req-2-2-2) | Age / date of birth granularity | 🟡 L2 | `APP` |
| [2.2.3](#req-2-2-3) | Identity granularity | 🟡 L2 | `APP` |
| [2.2.4](#req-2-2-4) | Photo metadata | 🟡 L2 | `APP` |
| [2.2.5](#req-2-2-5) | File metadata | 🟡 L2 | `APP` |
| [2.2.6](#req-2-2-6) | Communication, call and message history | 🟡 L2 | `APP` |
| [2.2.7](#req-2-2-7) | Live streaming data | 🟡 L2 | `APP` |

<a id="req-2-2-1"></a>
### 2.2.1 Location data granularity

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The granularity level of location data collected or processed per feature must be the least precise level at which the feature remains functional, selected from the following ordered scale (least to most precise):  
Continent → Country → Region/State → City → Neighbourhood → Street → Full Building Address → Precise GPS coordinates.  
Alternative esoteric levels of granularity may be used according to the same restriction of least specific possible.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The scale is normative: teams must document which level they use and why a less precise level would not suffice. Precise coordinates must not be the default.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each feature processing location data, confirm the granularity level is documented and justified. Test: confirm the system does not collect a more precise level than documented. Any feature using precise coordinates where city-level would suffice is a finding.

</div>

<a id="req-2-2-2"></a>
### 2.2.2 Age / date of birth granularity

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The granularity level of age or date of birth data collected or processed per feature must be the least precise level at which the feature remains functional, selected from the following ordered scale (least to most precise):  
Age threshold check (yes/no) → Age bracket → Birth year → Birth month + year → Full date of birth → Full DOB + time of birth.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Age verification features must use threshold check only and must not retain DOB after the check is complete, unless a separate documented purpose requires retention.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each feature processing age/DOB data, confirm the granularity level is documented and justified. For age verification features, confirm DOB is not retained post-verification unless separately justified.

</div>

<a id="req-2-2-3"></a>
### 2.2.3 Identity granularity

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The granularity level of identity data collected or processed per feature must be the least linkable level at which the feature remains functional, selected from the following ordered scale (least to most linkable):  
Anonymous → Aggregated (e.g. Role or cohort) → Pseudonym (system-generated, not reversible without key) → Display name (user-chosen) → First name → Full name → Full name + unique identifier (e.g. national ID, email).

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"Least linkable" rather than "least precise" — reflects that identity minimization is about reducing linkability to a natural person, not just data volume.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each feature processing identity data, confirm the granularity level is documented and justified. Any feature using full name + identifier where a pseudonym would suffice is a finding.

</div>

<a id="req-2-2-4"></a>
### 2.2.4 Photo metadata

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The metadata retained with a photo per feature must be the least identifying level at which the feature remains functional, selected from the following ordered scale (least to most identifying), for example:  
None → Rendering-only (orientation, colour profile, dimensions) → Capture date → Precise capture timestamp → Full details with embedded GPS location.  
OR  
None → Rendering-only (orientation, colour profile, dimensions) → Device make/model → Device or lens serial number.  
The selected scale can be a combination of these values.  
Metadata outside this scale (e.g. embedded thumbnails, edit history, author fields, face or person tags) must be stripped unless the feature requires it.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Strip at the earliest point, client-side where possible. Reading metadata to drive a feature and then discarding it is acceptable. Apply to all derivatives too: resized and CDN copies, and shared or exported copies. Inference from the image content itself (faces, landmarks) is covered by 2.1.4.

Photos may also contain information that may infer location, age, other personal or interpersonal identifiers.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each feature handling photos, confirm the retained metadata level is documented and justified. Test: upload a photo seeded with GPS, serial number and author values, then check every stored, served and shared copy. Any copy retaining more than the documented level is a finding.

</div>

<a id="req-2-2-5"></a>
### 2.2.5 File metadata

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The metadata retained with a file per feature must be the least identifying level at which the feature remains functional, selected from the following ordered scale (least to most identifying):  
None → Technical only (type, size, encoding) → Coarse timestamps → Precise timestamps → Producing application and version → Author or organisation name → Account, host, file-path or device identifiers → Embedded revision history, tracked changes, comments or location/network traces.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Includes location inferred from metadata (network location, time zone, language region). Apply to files the application generates (exports, generated documents) as well as files users upload.  
Metadata may also contain author identification.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each feature handling files, confirm the retained metadata level is documented and justified. Test: submit a file seeded with author, file-path and tracked-change values, then check every stored, served and generated copy. Any copy retaining more than the documented level is a finding.

</div>

<a id="req-2-2-6"></a>
### 2.2.6 Communication, call and message history

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The detail of communication history retained per feature must be the least detailed level at which the feature remains functional, selected independently from each of the following two ordered scales.

Interaction metadata (least to most detailed):  
None → Delivery state only → Aggregate counts and durations → Per-contact counts → Per-interaction metadata (participants, timestamp, duration) → Per-interaction metadata with device or location.

Content (least to most revealing):  
None (relayed, then discarded) → Content-free indicators (e.g. attachment present, type, size) → Hash of content (keyed or salted) → Derived labels only (e.g. spam flag, language, detected entities) → Redacted or truncated excerpt → Text only → Text with attachments and media → Text, attachments and surrounding context (quoted history, edit and deletion history, link-preview data).

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Metadata alone reveals relationships and behavioural patterns, so a lower scale level is not automatically harmless. Counterparties are data subjects who may never have used the application. Access to contacts or an address book is a separate collection decision requiring its own justification under 2.1.1.

Hashes: a hash supports integrity checks, deduplication and abuse matching without keeping the text. It is not anonymous, though. Low-entropy content can be recovered by guessing, and any hash can confirm that a known message was sent or link two copies of the same message. Use a keyed or salted hash, and treat perceptual hashes of media as closer to the content than to a hash.  
Attachments: these are often more revealing than the message text. Select their level on its own, and apply 2.2.5 to the files themselves.  
Derived stores: search indexes, push-notification payloads (which pass through third-party gateways), caches, link-preview fetches, drafts, and edit and deletion history all hold content. They count towards the retained level.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review the data model and confirm the retained history level per feature is documented and justified.  
Test: after a communication occurs, and again after its content is deleted, confirm nothing richer than the documented level is retained. Any feature retaining per-interaction metadata or content where counts would suffice is a finding.  
Test by sending a message with an attachment and a link, then edit it and delete it.  
Check the database, the search index, caches, notification payloads and backups.  
Anything retained above the documented content level, such as an orphaned attachment or a surviving pre-edit version, is a finding.

</div>

<a id="req-2-2-7"></a>
### 2.2.7 Live streaming data

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The fidelity of live stream data (audio, video, sensor, or telemetry) collected or processed per feature must be the least detailed level at which the feature remains functional, selected from the following ordered scale (least to most detailed):  
Derived events only → Reduced fidelity (lower sample rate, resolution, bit depth, or cropped region) → Full fidelity, processed in memory only → Full fidelity, persisted.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Prefer deriving events on the device rather than transmitting the stream. Bound capture to active use of the feature rather than continuous capture. Discarding raw stream data after processing is covered by 3.5.3.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review the capture configuration and confirm the fidelity level is documented and justified. Test: observe network traffic while the feature is idle (no stream data sent) and while active (fidelity matches the documented level). Any capture or transmission above the documented level is a finding.

</div>

---

<p style="opacity:.7;font-size:.9em">
<a href="00-introduction.md">Introduction</a> · <a href="01-architecture-data-mapping.md">Previous: Architecture & Data Mapping</a> · <a href="03-data-lifecycle-management.md">Next: Data Lifecycle Management</a>
</p>
