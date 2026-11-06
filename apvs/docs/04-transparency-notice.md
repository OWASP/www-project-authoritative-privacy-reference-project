---
layout: default
title: "Chapter 4: Transparency & Notice"
nav_order: 5
---

# Chapter 4. Transparency & Notice

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance and verification text (shaded and in italics below) are in beta. Requirement type is waiting for community comments, and the chapter and section introductions are in beta as well. Wording will keep moving as feedback arrives.
</div>

This chapter covers how an application tells people what happens to their personal data, how it asks for and records their consent, and how it lets them see and change their privacy settings. It exists so that the information and choices offered to data subjects are accurate, timely and usable, and so that they can be verified.

## About this chapter

People can only exercise control over their personal data if they know what is happening to it and can act on that knowledge. This chapter treats transparency as a property of the application itself, something built into screens, APIs, settings and release processes, and therefore something a tester can check. It guards against two failures in particular, a system that collects more than people realize and a set of choices that look real but change nothing.

The first principle is that a notice must be specific and must arrive at the right moment. A notice shown before collection, scoped to the processing activity at hand, and stating categories, purposes, retention and recipients in concrete terms gives a person something to decide on. Because notices are sometimes read by software as well as by people, they should be machine accessible as well as human readable, and each version should be recorded so that it is always possible to say what a given person was shown on a given day.

The second principle is that consent is only worth recording if it was freely given through an interface that describes it accurately. Accepting and declining need equal prominence and equal effort, optional processing starts switched off, and each purpose is asked about separately with wording that describes the real consequences of each choice. Withdrawal sits in the same place as the original choice, and the record of each decision ties it to the notice version that was on screen at the time. Developers can verify most of this by loading the interface and comparing the two paths side by side.

The third principle is that a privacy setting is a statement about processing, so the processing must match it. A toggle that updates a database flag while a pipeline carries on regardless is worse than no toggle, because it creates false assurance. Settings should be easy to find, labeled consistently wherever they appear, gathered in one dashboard, and wired through to the components that actually process data. When defaults change after an update or a migration, or when the processing itself changes materially, the people affected hear about it before it takes effect.

Chapter 1 supplies the data map that notices and recipient disclosures are checked against, and Chapter 5 covers the features through which people act on what they have learned here.

## Sections at a glance

| Section | Title | Requirements | <span style="color:#1a7f37">L1</span> | <span style="color:#9a6700">L2</span> | <span style="color:#8250df">L3</span> |
|---|---|---:|---:|---:|---:|
| [4.1](#section-4-1) | Notice | 8 | 3 | 4 | 1 |
| [4.2](#section-4-2) | Consent Interface | 10 | 6 | 4 | 0 |
| [4.3](#section-4-3) | Privacy Settings | 7 | 1 | 5 | 1 |

---

<a id="section-4-1"></a>
## 4.1 Notice

Notices are the application's account of what it does with personal data, so this section covers when they appear, how specific they are, what they must contain, and how people hear about changes and about data obtained from other sources. Most requirements can be checked by comparing the notice text with what the system actually does.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [4.1.1](#req-4-1-1) | Privacy notice at collection | 🟢 L1 | `APP` |
| [4.1.2](#req-4-1-2) | Contextual notice per processing activity | 🟡 L2 | `APP` |
| [4.1.3](#req-4-1-3) | Notice content — required fields | 🟢 L1 | `APP` |
| [4.1.4](#req-4-1-4) | Named third-party recipients | 🟣 L3 | `APP` |
| [4.1.5](#req-4-1-5) | Retention period specificity in notice | 🟡 L2 | `APP` |
| [4.1.6](#req-4-1-6) | Notice for indirectly collected data | 🟡 L2 | `SYS` |
| [4.1.7](#req-4-1-7) | Material change notification | 🟡 L2 | `SYS` |
| [4.1.8](#req-4-1-8) | Automated decision-making disclosure | 🟢 L1 | `APP` |

<a id="req-4-1-1"></a>
### 4.1.1 Privacy notice at collection

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must present a privacy notice at or before the point of personal data collection, explaining in plain language what personal data is collected, how it is used, and how it is protected.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The notice must precede collection — it cannot be presented after data has been submitted.

this must be human readable and machine accessible as well, eg for collection via API or LLM scraping etc.

Privacy notice must be versioned, and every changed version recorded.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: walk the user journey to each collection point and confirm a notice is present before data is submitted. Any collection point without a preceding notice is a finding.

</div>

<a id="req-4-1-2"></a>
### 4.1.2 Contextual notice per processing activity

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Privacy notice must be presented at the granularity of the processing activity. A single global privacy policy does not satisfy notice requirements for individual collection points.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Each distinct processing activity requires its own contextual notice.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm each distinct collection point has contextual notice specific to that activity — a link to a general policy without contextual information is a finding.

</div>

<a id="req-4-1-3"></a>
### 4.1.3 Notice content — required fields

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The privacy notice must state, for each processing activity: (a) the personal data categories collected; (b) the processing purpose; (c) the retention period or criteria; (d) whether data is shared with third parties and if so, which categories of recipient.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Generic statements such as "to improve our service" do not satisfy field (b).

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review notice content against the four required fields. Any field absent or populated with a generic placeholder is a finding.

</div>

<a id="req-4-1-4"></a>
### 4.1.4 Named third-party recipients

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where personal data is shared with third parties, the privacy notice must identify the actual named recipients where practicable. Where only categories of recipients are provided, the category must specify the type, sector, and location of recipients with sufficient specificity to be meaningful.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"Third parties" includes all recipients — not just external companies but also joint controllers and processors. Generic categories such as "trusted partners" do not satisfy this requirement.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review notice recipient disclosures against actual data sharing flows (cross-reference 1.4.1). Generic or unspecific recipient descriptions are findings.

</div>

<a id="req-4-1-5"></a>
### 4.1.5 Retention period specificity in notice

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The privacy notice must state a specific retention period for each data category and processing purpose, or where a fixed period cannot be stated, the criteria used to determine it. A generic statement that data will be retained as long as necessary does not satisfy this requirement.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Different categories and purposes may have different periods; each must be stated.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review notice retention disclosures and compare to the application definition or configuration. Incorrect specficiation in the notice is a finding.

</div>

<a id="req-4-1-6"></a>
### 4.1.6 Notice for indirectly collected data

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Where personal data is collected from a source other than the data subject, the system must provide notice to the data subject within a reasonable period and no later than a defined and disclosed maximum period, or at the point of first communication if earlier.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Addresses indirect data collection flows — third-party data brokers, public sources, other controllers.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: identify indirect data collection flows in the system (cross-reference 1.4.1). Confirm a notice delivery mechanism exists with a documented timeline, as well as a process to trigger this mechansim. Absence of mechanism, timeline, or process is a finding.

</div>

<a id="req-4-1-7"></a>
### 4.1.7 Material change notification

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must notify data subjects when a material change occurs to the processing of their personal data - including addition of new processing purposes, new third-party recipients, or changes to retention periods - before the change takes effect.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"Material change" includes: new processing purpose, change of controller identity, change to how rights can be exercised. Non-material changes (spelling corrections, style changes) do not require notification. Notification must precede the change, not accompany it.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm a process exists to send notification to all affected data subjects before deploying a new version or configuration that implements one of these changes. A lack of process or enforced checklist is a finding.

</div>

<a id="req-4-1-8"></a>
### 4.1.8 Automated decision-making disclosure

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where the system performs automated decision-making for a data subject, the privacy notice must disclose: (a) the existence of the automated processing; (b) the logic involved; (c) the significance and envisaged consequences for the data subject.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The disclosure must be specific enough that the data subject can understand the consequences — "we use algorithms to personalise your experience" does not satisfy (b) or (c).

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: identify automated decision-making processing activities. Confirm the three required disclosure components exist in the notice for each. Any missing component is a finding.

</div>

---

<a id="section-4-2"></a>
## 4.2 Consent Interface

Consent interfaces are where a person's decision is captured, and design choices there can quietly steer that decision. This section sets out the properties that make a consent interaction a genuine choice, covering equal presentation of options, separate asks per purpose, accurate framing, easy withdrawal, and a reliable record of what was agreed.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [4.2.1](#req-4-2-1) | Visual parity of privacy choices | 🟢 L1 | `APP` |
| [4.2.2](#req-4-2-2) | No pre-selection or inaction consent | 🟢 L1 | `APP` |
| [4.2.3](#req-4-2-3) | Consent granularity — one purpose per consent act | 🟢 L1 | `APP` |
| [4.2.4](#req-4-2-4) | Consent separable from other matters | 🟢 L1 | `APP` |
| [4.2.5](#req-4-2-5) | Consent withdrawal | 🟡 L2 | `APP` |
| [4.2.6](#req-4-2-6) | Consent record | 🟡 L2 | `SYS` |
| [4.2.7](#req-4-2-7) | No forced consent for core functionality | 🟡 L2 | `APP` |
| [4.2.8](#req-4-2-8) | No pre-consent cookie initialisation | 🟡 L2 | `APP` |
| [4.2.9](#req-4-2-9) | Representative Framing of Privacy Choices | 🟢 L1 | `APP` |
| [4.2.10](#req-4-2-10) | No nagging | 🟢 L1 | `APP` |

<a id="req-4-2-1"></a>
### 4.2.1 Visual parity of privacy choices

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Accept and reject options in consent interfaces must have equal visual prominence. Size, colour, contrast, and placement must not direct attention toward privacy-invasive options or away from privacy-protective ones.  
Accepting must not require fewer steps than rejecting.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Equal prominence covers: size, colour weight, contrast ratio, and placement. Neither option may be visually de-emphasised relative to the other. Step count parity is the minimum — reject must not require more clicks, screens, or confirmations than accept.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review consent interface for visual asymmetry between accept and reject options. Any difference in size, colour weight, contrast, or placement that favours acceptance is a finding. Count steps to accept vs reject — any asymmetry is a finding.

Inspect: measure size, colour contrast, and placement of accept vs reject options. Any asymmetry that favours acceptance is a finding.

</div>

<a id="req-4-2-2"></a>
### 4.2.2 No pre-selection or inaction consent

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Consent must not be pre-selected or inferred from inaction. The default state of all consent controls must be unchecked or off, and require a user to opt-in, not to opt-out.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Pre-selection includes: pre-ticked checkboxes, toggles defaulting to on, and any design where the privacy-invasive option is active without explicit user action. Scrolling past a notice, closing a banner, or continuing to use the service does not constitute consent.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: load the consent interface without interaction and confirm all optional processing controls are off by default. Any pre-selected option is a finding.

</div>

<a id="req-4-2-3"></a>
### 4.2.3 Consent granularity — one purpose per consent act

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Consent must be obtainable separately for each distinct processing purpose. A layered consent interface may be used to reduce interaction burden: a first layer may present a summary choice — accept all or reject all — provided that a second layer offering per-purpose granular controls is reachable in no more steps, and with no less visual prominence, than the summary choice. Accepting one purpose must not be conditional on accepting another, at either layer.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Each purpose requires its own consent interaction — an "accept all" option may be provided alongside granular controls but must not substitute for them.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review consent flow for bundling of multiple purposes into a single consent act. Any single checkbox or confirmation covering more than one purpose is a finding.

</div>

<a id="req-4-2-4"></a>
### 4.2.4 Consent separable from other matters

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where consent is requested alongside other declarations (e.g. terms of service, account registration), the consent request must be clearly distinguishable from those other matters, presented separately, and in plain language.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Consent embedded within terms and conditions is invalid. Visual and structural separation is required — consent must not be continuous with surrounding non-consent content.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review consent collection points for bundling with non-consent content. Any consent request not visually and structurally separated from surrounding content is a finding.

</div>

<a id="req-4-2-5"></a>
### 4.2.5 Consent withdrawal

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Withdrawing consent must be as easy as giving it and must be accessible from the same context in which consent was given.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"As easy as giving it" means the same number of steps and the same channel. A consent given via a toggle must be withdrawable via the same toggle. Withdrawal must not require navigating to a separate settings area, contacting support, or sending a written request.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: follow the withdrawal path and confirm it requires no more steps than the consent path and is reachable from the same UI context. Any asymmetry in step count or channel is a finding.

</div>

<a id="req-4-2-6"></a>
### 4.2.6 Consent record

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must record for each consent transaction: (a) the identity of the data subject; (b) the timestamp; (c) the processing purpose consented to; (d) the version of the notice presented; (e) the mechanism by which consent was given. This record must be retained for the duration of the processing plus the applicable limitation period.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The controller must be able to demonstrate that consent was obtained. The record must capture what was shown to the data subject, not just that consent was given — version of notice is critical for this.

For delegated DSRs, the consent should note who consented for whom.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: request the consent record for a known data subject and confirm all five components are present. Test: confirm the record is generated automatically at the point of consent, not retrospectively.

</div>

<a id="req-4-2-7"></a>
### 4.2.7 No forced consent for core functionality

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must not require consent to non-essential processing as a condition of accessing core functionality, where that processing is not strictly necessary for the functionality requested.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

A feature that functions without the processing but gates access on consent is a finding.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: attempt to use core functionality without consenting to non-essential processing. Any blocking of core functionality conditional on non-essential consent is a finding.

</div>

<a id="req-4-2-8"></a>
### 4.2.8 No pre-consent cookie initialisation

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where cookies or equivalent tracking technologies are used for non-essential purposes, no such technology must be initialised before a consent signal is received and recorded.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Non-essential cookies include analytics, advertising, and personalisation trackers. Essential cookies (session management, security) are exempt.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: inspect network traffic and browser storage before any consent interaction. Any non-essential cookie or tracker present before a consent signal is a finding.

</div>

<a id="req-4-2-9"></a>
### 4.2.9 Representative Framing of Privacy Choices

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The interface must not misrepresent the necessity, urgency, or social validation of a privacy-related choice in a way that pressures the data subject toward a particular outcome.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Confirmshaming, false necessity, and fabricated urgency are distinct techniques with a shared mechanism: each misrepresents a fact — what is required, what happens if you decline, or how others are behaving — to pressure a privacy decision the interface's true state doesn't support.

Known manifestations include, without limitation:  
• False necessity — designating a field as required, mandatory, or blocking empty submission where the underlying data does not satisfy the necessity test.  
• Guilt or shame framing — labeling rejection or a privacy-protective choice in negative, guilt-inducing, or emotionally manipulative language.  
• Fabricated urgency or social proof — presenting scarcity signals, countdown timers, or claims about other users' behavior near a consent or privacy decision that are not verifiably true and current.  
This list is illustrative, not exhaustive — new manifestations of the same underlying pattern are covered by the general requirement even where not enumerated here.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect the interface presented at each privacy-related choice point for claims or framing that do not reflect the system's actual state — including necessity, urgency, and social validation claims. Any such claim that misrepresents the actual state is a finding.

</div>

<a id="req-4-2-10"></a>
### 4.2.10 No nagging

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must not re-prompt a data subject for consent to non-essential processing which they have already declined, within the same session or across sessions, unless the processing purpose or legal basis has materially changed.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

A "material change" is a genuine change to the nature of the processing — not a cosmetic reframing of the same request. Re-prompting with different wording for the same purpose is a finding.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: decline consent and continue using the system across multiple sessions. Any re-prompt for the same purpose without a documented material change is a finding.

</div>

---

<a id="section-4-3"></a>
## 4.3 Privacy Settings

Privacy settings let people review and change their choices after the first interaction. This section covers whether those settings can be found, whether they behave the same everywhere, whether they reflect and control the processing that really takes place, and whether the person can see the overall effect of their configuration.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [4.3.1](#req-4-3-1) | Privacy settings discoverability | 🟢 L1 | `APP` |
| [4.3.2](#req-4-3-2) | Functional privacy settings | 🟡 L2 | `APP` |
| [4.3.3](#req-4-3-3) | Consistent privacy settings | 🟡 L2 | `APP` |
| [4.3.4](#req-4-3-4) | Privacy settings reflect actual processing state | 🟡 L2 | `SYS` |
| [4.3.5](#req-4-3-5) | Settings reset notification | 🟡 L2 | `SYS` |
| [4.3.6](#req-4-3-6) | Privacy dashboard existence | 🟡 L2 | `SYS` |
| [4.3.7](#req-4-3-7) | Privacy report | 🟣 L3 | `SYS` |

<a id="req-4-3-1"></a>
### 4.3.1 Privacy settings discoverability

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Privacy settings must be directly accessible through standard system menus or settings, without requiring contact with support, submission of a request, or navigation to an external system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

"Standard system menus" means the settings or account menu a user would naturally navigate to. Privacy settings must not require knowledge of a direct URL, a support interaction, or a search to locate. WCAG AA contrast ratios apply. "Outside normal reading flow" means positioned where a user following standard reading patterns (top to bottom, left to right) would not encounter it.

Privacy settings must not be hidden, rendered in low contrast, positioned outside normal reading flow, or otherwise visually de-emphasised relative to non-privacy interface elements.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: attempt to locate privacy settings from the main interface using only standard navigation. Inability to reach settings within two navigational steps from any screen is a finding.

Inspect: review privacy control visibility against WCAG AA contrast ratios and reading flow positioning. Any control failing contrast requirements or positioned to reduce discoverability is a finding.

</div>

<a id="req-4-3-2"></a>
### 4.3.2 Functional privacy settings

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must not present privacy settings that are non-functional, misleading, or have no effect on actual data processing.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The most common failure mode is a consent UI that appears functional but does not propagate changes to the backend processing system. Controls that update a UI state without affecting actual processing are a finding.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: activate each privacy setting and confirm the corresponding processing stops. Inspect backend processing state after each change. Settings with no observable effect on processing are a finding.

</div>

<a id="req-4-3-3"></a>
### 4.3.3 Consistent privacy settings

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Privacy settings must use consistent labels, placement, language, and behaviour throughout the system. A setting that affects a given processing activity in one context must operate identically in all contexts where that processing occurs.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

A toggle that disables tracking on one screen must not re-enable it on another. Labels must be identical across contexts — different phrasing for the same control is a finding.

Consent and preference interfaces must not use double negatives, ambiguous phrasing, or language that obscures the consequence of the choice. The consequence of each option must be unambiguously determinable from the label alone.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review privacy settings across all system screens. Any inconsistency in label, placement, or functional behaviour is a finding.

Inspect: review consent and preference label language. Any option where the outcome requires interpretation or inference to understand is a finding.

</div>

<a id="req-4-3-4"></a>
### 4.3.4 Privacy settings reflect actual processing state

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Privacy settings must reflect the actual current state of processing. Where a setting is shown as off, the corresponding processing must not be occurring.  
Changes made to the privacy settings must take effect on actual processing immediately or within a technically justified and disclosed maximum period.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The two obligations are distinct: (a) changes must propagate to actual processing; (b) the dashboard display must reflect the updated state. Both must be satisfied — a dashboard that updates its display without affecting processing, or that affects processing without updating its display, is a finding.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: set a processing preference to off and inspect actual system processing. Confirm the setting reflects the live processing state at all times. Any divergence between displayed state and actual processing is a finding.

</div>

<a id="req-4-3-5"></a>
### 4.3.5 Settings reset notification

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Where privacy settings are reset — for example following an app update, account migration, or system change — the data subject must be notified of the reset and given the opportunity to review settings before processing resumes under the new defaults.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: simulate a system update that resets privacy settings. Confirm notification is triggered and settings review is offered before processing resumes. Absence of notification mechanism is a finding.

</div>

<a id="req-4-3-6"></a>
### 4.3.6 Privacy dashboard existence

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide a privacy dashboard through which data subjects can view and modify all their privacy settings in a single accessible interface, including: active consent states, processing purposes, and communication preferences.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The dashboard must be a single point of access — fragmented privacy settings spread across multiple menus do not satisfy this requirement. "View and modify" are both required — a read-only dashboard does not satisfy the modification obligation.

this is an overall interface allowing direct access to all privacy settings, instead of chasing each one seperately on each record, post, field, feature, etc.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm the dashboard exists and is accessible. Confirm it covers consent states, processing purposes, and communication preferences in a single interface. Absence of any of these three is a finding.

</div>

<a id="req-4-3-7"></a>
### 4.3.7 Privacy report

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide data subjects with access to a privacy impact summary showing the consequences of their current privacy settings — including what processing is active, what data is shared, and what would change if settings were modified.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Think: "Based on your current settings, your location data is shared with 3 advertising partners."

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm the privacy report or equivalent exists and is accessible from the dashboard. Confirm it reflects current settings state. A static generic report not reflecting the individual's actual settings is a finding.

</div>

---

<p style="opacity:.7;font-size:.9em">
<a href="00-introduction.md">Introduction</a> · <a href="03-data-lifecycle-management.md">Previous: Data Lifecycle Management</a> · <a href="05-privacy-features.md">Next: Privacy Features</a>
</p>
