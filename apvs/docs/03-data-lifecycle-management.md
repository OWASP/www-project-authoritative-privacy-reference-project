---
layout: default
title: "Chapter 3: Data Lifecycle Management"
nav_order: 4
---

# Chapter 3. Data Lifecycle Management

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance and verification text (shaded and in italics below) are in beta. Requirement type is waiting for community comments, and the chapter and section introductions are in beta as well. Wording will keep moving as feedback arrives.
</div>

Applies the minimality principles of Chapter 2 to each phase of the personal data lifecycle, from collection through processing, storage, sharing and deletion. It exists because the privacy risk of a piece of data changes as it moves through a system, and each phase has its own controls.

## About this chapter

Personal data has a life story. It arrives through a form, an API call or a sensor, gets processed, sits in storage for a while, may be handed to someone else, and eventually should disappear. Most privacy failures happen at the seams between those phases, such as a value that was needed for one second and ends up in a log for three years, a correction that reaches the database but never the search index, or a deletion request that clears the primary store while the backups carry on regardless. This chapter follows the data through each phase and states what an application must do there so that the outcome can be verified.

Chapter 2 is overarching. Its principles of collecting little, keeping it coarse, and holding it briefly apply to every phase, and this chapter does not restate them. It applies them phase by phase, so each section opens by recalling the relevant principle and then frames the requirements that are specific to that stage. A developer working on ingestion can read the collection section on its own, and an architect designing retention can do the same with storage, while both still work from one shared set of ideas.

Three base principles run through the whole chapter. First, data should live only as long as the purpose it serves, which makes deletion a designed feature with explicit triggers, defined windows and automatic enforcement. Second, the result of an operation is usually worth more to the system than the data that produced it, so a verified flag can outlive the ID scan, and computation that can happen on the data subject's own device should happen there. Third, identity should be separated from the data wherever the design allows it, through pseudonymous references, separately held mappings and logs that do not name people unless a documented need requires it.

The same attention applies to every copy and every recipient. Replicas, caches, logs, temporary files, backups and third parties all count as places where the data lives, so corrections, expiry and deletion must reach them all and leave evidence that they did. Where a real constraint makes immediate action impossible, the chapter asks for a defined and enforced maximum window.

## Sections at a glance

| Section | Title | Requirements | <span style="color:#1a7f37">L1</span> | <span style="color:#9a6700">L2</span> | <span style="color:#8250df">L3</span> |
|---|---|---:|---:|---:|---:|
| [3.1](#section-3-1) | Data Collection | 2 | 1 | 0 | 1 |
| [3.2](#section-3-2) | Data Processing | 5 | 1 | 2 | 2 |
| [3.3](#section-3-3) | Data Storage | 7 | 1 | 3 | 3 |
| [3.4](#section-3-4) | Data Export and Sharing | 4 | 0 | 2 | 2 |
| [3.5](#section-3-5) | Data Deletion | 7 | 1 | 4 | 2 |

---

<a id="section-3-1"></a>
## 3.1 Data Collection

Collection is the first point at which Chapter 2 can be applied, since data never taken in cannot leak later. This section covers what happens to data at the moment it arrives, including data that is only needed in flight and the cases where users should be warned before they hand over something they probably did not mean to share.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [3.1.1](#req-3-1-1) | Discard collected data if purpose is met | 🟢 L1 | `APP` |
| [3.1.2](#req-3-1-2) | Privacy-aware input nudges | 🟣 L3 | `APP` |

<a id="req-3-1-1"></a>
### 3.1.1 Discard collected data if purpose is met

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Personal data collected for a purpose that is fully satisfied during collection or immediate processing (for example validating, calculating, routing, alerting or authenticating) must be processed in-flight only, and discarded as soon as that processing completes. Do not even save this data to persistent storage.  
In-flight means the data is held solely in volatile working memory and in transit, for the duration of the operation.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

In plain terms: if the purpose is finished once the data has been used, use it in memory and let it go. Persistent storage is anything that outlives the operation: databases, files, logs, caches that outlive the operation, message-broker retention, dead-letter queues, stream checkpoints and state stores, backups, and payload capture by monitoring or debugging tools. Examples: an age check that does not store the date of birth; address or format validation; one-time codes; a sensor reading used only for a live decision; real-time alerting, threshold detection and stream analytics.

This applies to every collection channel, including forms, APIs, file uploads, device and sensor input, and live or streaming feeds.  
Emphasize and clarify ephemeral and transient data.  
Where a streaming pipeline requires intermediate buffering of personal data, the buffer retention window must be the minimum technically necessary, explicitly defined, and enforced by the system.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review streaming pipeline architecture. Confirm no persistence layer is written to where the purpose is satisfied at ingestion.  
Test: confirm no personal data appears in storage after a stream processing event where persistence is not required.

Inspect: for each collection channel, identify the purposes satisfied during collection or immediate processing, and review the architecture and configuration (broker retention, dead-letter queues, checkpoints and state stores, logging, monitoring and debugging payload capture) to confirm the data is handled in-flight only for those purposes.  
Test: process a test event for such a purpose containing a unique marker value, then search all persistent stores, logs, caches and monitoring tools for it. Any hit, or personal data in storage after a processing event where persistence is not required, is a finding.

</div>

<a id="req-3-1-2"></a>
### 3.1.2 Privacy-aware input nudges

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where the system detects that a user is about to submit personal data of elevated sensitivity that is not expected or necessary for the functionality of the system, the system must present a contextual nudge informing the user of the nature and consequence of sharing that data before the submission is processed.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Examples: alerting a user that a message contains health information before sending it to a third-party service; warning that precise location is being shared; flagging that text contains strong negative sentiment that may be retained. This is a privacy-aware UX pattern, not a blocking mechanism.

including but not limited to special category data, financial data, or data revealing emotional state

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: submit test inputs containing special category data, precise location, and other contextual markers. Confirm contextual nudges are presented before submission in each case. Absent nudges for elevated-sensitivity content are findings.

</div>

---

<a id="section-3-2"></a>
## 3.2 Data Processing

Processing is where collected data is put to use, and where the principles of Chapter 2 turn into concrete questions about when working data can be discarded and what must be kept. The requirements here tie deletion to the completion of each operation, keep outcomes separate from their source data, favor computation on the data subject's device, and check that data is used only for the purpose it was collected for.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [3.2.1](#req-3-2-1) | Deletion on processing completion | 🟢 L1 | `APP` |
| [3.2.2](#req-3-2-2) | Deletion trigger mechanism | 🟡 L2 | `SYS` |
| [3.2.3](#req-3-2-3) | Processing outcome recorded independently of source data | 🟡 L2 | `APP` |
| [3.2.4](#req-3-2-4) | Client-side computing | 🟣 L3 | `APP` |
| [3.2.5](#req-3-2-5) | Purpose limitation | 🟣 L3 | `APP` |

<a id="req-3-2-1"></a>
### 3.2.1 Deletion on processing completion

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Personal data collected or generated solely to fulfil a discrete, bounded processing operation must be deleted after that operation is complete.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The qualifier "discrete, bounded" is key: the processing operation has a defined start and end. Open-ended processing is not covered here.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: identify each bounded processing operation in the system. Confirm no personal data persists in storage after operation completion. Test: inspect storage state immediately after a test operation completes.

</div>

<a id="req-3-2-2"></a>
### 3.2.2 Deletion trigger mechanism

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must implement an explicit mechanism by which completion of a processing operation triggers deletion of the associated personal data, rather than relying solely on scheduled periodic cleanup.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This should be triggered automatically by the process completion which removes al lthe unneeded data at once.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm a deletion trigger exists that fires on operation completion. A system relying solely on a nightly or weekly cleanup job does not satisfy this requirement.

</div>

<a id="req-3-2-3"></a>
### 3.2.3 Processing outcome recorded independently of source data

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where a processing operation produces a decision, classification, or status that the system relies on afterwards, the system must store that result seperate from the personal data used to produce it, and without embedding personal data in that result.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Examples: identity verification (verified/not verified retained; ID scan deleted); age verification (threshold met: yes/no retained; date of birth deleted); fraud screening (risk classification retained; transaction data deleted).

Note that an outcome record tied to an identifiable user is still personal data and falls under retention.

separation is better than combined from privacy perspective. Mostly because now the (more sensitive) origin data can be removed once the (less sensitive) outcome is determined.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each decision-producing operation, confirm outcome and source data are stored separately. Test: delete source data for a test subject and confirm the outcome record remains accessible and functional.

</div>

<a id="req-3-2-4"></a>
### 3.2.4 Client-side computing

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

When personal data is being collected on the data subject's own device, if the processing purpose can be fulfilled on the data subject’s own device, the processing must take place there, and only its result may be sent to the backend.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This is particularly relevant for real-time data that can be aggregated, or processing operations requiring (sensitive) personal data from the data subject.

When possible, only aggregagated data or the processing result is being sent to the backend

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each processing activity, identify where it runs, and confirm those that could run on-device do.  
Test: capture traffic during the operation and confirm raw personal data is not transmitted, only the result.

</div>

<a id="req-3-2-5"></a>
### 3.2.5 Purpose limitation

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must check that personal data is being processed only for purposes in line with its documented collection purpose (see chapter 1), and only for the timeframe of the data that purpose requires.  
The processing purpose must not go beyond what the data subject was informed of at collection time.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Applies to every use of the data, including internal reuse and sharing (see also 3.4), not only the primary feature.

Purpose should be enforced technically where possible: records carry purpose tags (1.2.1), and services and pipelines that read them declare a purpose that is checked, so undeclared use fails or is flagged.

Timeframe: a purpose may need only part of the data. E.g. an app that only looks at the last 3 months of data: the purpose still holds, but data older than 3 months is outside it. Retention (3.3.1) is per data class and may be longer because of another purpose; each purpose is still limited to its own timeframe.

Examples of secondary use that commonly slips through: production data copied to test, dev, staging or analytics environments; customer data (support tickets, prompts, uploaded content) used to train or fine-tune models; data collected for security or fraud prevention reused for marketing.

Secondary purposes (edge case): where a secondary processing purpose is not covered by the collection purpose, processing may only proceed where a compatibility assessment or a separate legal basis is recorded in the purpose register prior to that processing beginning. The record must predate the processing — not be created after the fact.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each processing operation (1.4.3), confirm its documented purpose is within the collection purpose (1.2.2) of every data element it uses, and that the data timeframe it reads is within the timeframe documented for that purpose.  
Inspect: for each secondary processing use, confirm a dated compatibility assessment or legal basis entry exists in the purpose register that predates the processing. Absent or postdated records are findings.  
Test: run an operation under a purpose that is not registered for the data (e.g. read production records from a test environment, or feed them to a training job) and confirm it is blocked or flagged.  
Test: request data older than the documented timeframe for a purpose and confirm it is not used.  
Any other processing outside the collection purpose, or beyond the documented timeframe, is a finding.

</div>

---

<a id="section-3-3"></a>
## 3.3 Data Storage

Storage determines how long personal data stays and in what form it sits at rest, so it applies the retention and identifiability concerns of Chapter 2 to databases, caches and logs. The requirements ask for defined retention periods, automatic expiry, corrections that reach every copy, and pseudonymous references kept apart from the identities they stand for.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [3.3.1](#req-3-3-1) | Retention period defined per data class | 🟡 L2 | `APP` |
| [3.3.2](#req-3-3-2) | Residual retention window for temporary data | 🟡 L2 | `APP` |
| [3.3.3](#req-3-3-3) | Automated deletion at retention expiry | 🟣 L3 | `SYS` |
| [3.3.4](#req-3-3-4) | Corrected data propagation | 🟣 L3 | `SYS` |
| [3.3.5](#req-3-3-5) | Pseudonymous references | 🟢 L1 | `APP` |
| [3.3.6](#req-3-3-6) | Pseudonym/identity mapping separation | 🟣 L3 | `SYS` |
| [3.3.7](#req-3-3-7) | Pseudonymous audit logs | 🟡 L2 | `SYS` |

<a id="req-3-3-1"></a>
### 3.3.1 Retention period defined per data class

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

A minimal retention period must be defined for each personal data element or data class processed by the system. Where a fixed period cannot be stated, the criteria used to determine the period must be defined.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Deefine minimal retention period by defined purpose.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review the purpose register or equivalent for retention period entries per data type. Any data type without a defined period or defined criteria, or a needlessly long defined period, is a finding.

</div>

<a id="req-3-3-2"></a>
### 3.3.2 Residual retention window for temporary data

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where immediate deletion is not technically feasible (e.g. due to buffering, caching, or asynchronous processing), the system must define and enforce a maximum residual retention window, which must be the minimum technically necessary and must be documented.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The residual window must be enforced by the system, not merely documented as a policy.

tag: buffer, queue, cache, ...

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm the residual retention window is defined and documented for each component where immediate deletion is not feasible. Test: confirm the system enforces the window - data persisting beyond it is a finding.

</div>

<a id="req-3-3-3"></a>
### 3.3.3 Automated deletion at retention expiry

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must automatically delete personal data upon expiry of its defined retention period, according to the configured retention period per data type, without requiring manual intervention.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The phrase "without requiring manual intervention" is the key operative phrase. Periodic manual review is a compensating control, not a substitute.

Assess the data expiry in the context of the entire system and ecosystem. It is possible that (part of) the data is still required for other processing purposes or needs to be stored for legal obligations. Evidently these have priority over deletion. Still assess whether minimization (aggregation, partial deletion, ...) is possible while still adhering to the remaining purposes and obligations.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review storage configuration for retention period settings per data type. A storage system with only a single global retention period does not satisfy this requirement.  
Test: configure a test retention period, advance time past expiry, confirm data is deleted without manual action. Manual-only deletion processes do not satisfy this requirement.

</div>

<a id="req-3-3-4"></a>
### 3.3.4 Corrected data propagation

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

A corrected personal data value requested by a data subject must propagate to all storage components in which that data is held, including replicas, caches, and search indexes, within a defined and technically enforced maximum period.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<a id="req-3-3-5"></a>
### 3.3.5 Pseudonymous references

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Primary keys, foreign keys, references between components or systems, and URLs that refer to a data subject must use a system-generated pseudonymous identifier rather than a direct identifier. The pseudonym must not be derivable from the direct identifier without a secret key.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Direct identifiers (email address, phone number, national ID, full name) change, leak through URLs and referrer headers, and spread into every table, index and third party that copies them. A surrogate means identity lives in one mapping record. That makes deletion and rectification a single-point operation, and an email change doesn’t cascade through the system.  
Use random or keyed (HMAC) identifiers. An unkeyed hash of an email address is reversible by dictionary attack and is not a pseudonym.  
Where linkage across recipients or contexts isn’t needed, use a different pseudonym per recipient.  
Store the mapping separately. Guessable or sequential IDs are an access control matter (ASVS).  
This doesn’t prevent a user signing in with their email. The email lives in the mapping store, not in keys or references.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review database schemas, API routes, URL patterns and message payloads for keys and references. Any email address, phone number, national ID or name used as a key or reference is a finding.  
Test: change a test subject’s email address and confirm no keys or references need updating. Capture URLs and external calls and confirm none contain direct identifiers.

</div>

<a id="req-3-3-6"></a>
### 3.3.6 Pseudonym/identity mapping separation

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Where pseudonymisation is used, the mapping between pseudonym and real identity must be stored separately from the system using the pseudonym, with dedicated access controls for that system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Without separation, pseudonymisation provides no meaningful protection: any breach of the main system also reveals real identities.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm the pseudonym-to-identity mapping is stored in a separate system or data store. Confirm access controls to the mapping are independent of the system using the pseudonym. Co-location of mapping and pseudonymised data is a finding.

</div>

<a id="req-3-3-7"></a>
### 3.3.7 Pseudonymous audit logs

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

System and audit logs must use pseudonymous identifiers (that can be re-identified if necessary) rather than real names or national identifiers, unless attribution to a specific individual is a documented legal or security requirement of the log.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Identifying information is stored in a separate database. The pseudonym refers to it, but security admin does not need to be able to see who actually appears in the logs - real identity is only needed in exceptional circumstances, such as investigation, legal hold, incident response, when it can be resolved at that point through a controlled re-identification process.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review log schemas and sample log entries. Any log containing real names or national identifiers without a documented legal or security justification is a finding.

</div>

---

<a id="section-3-4"></a>
## 3.4 Data Export and Sharing

Sharing and export move data beyond the boundary where the application controls it, which makes the minimality of Chapter 2 harder to enforce afterwards. This section keeps recipients and exported fields to what the purpose requires, tracks access to sensitive data, and gives data subjects a usable copy of their own data.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [3.4.1](#req-3-4-1) | Share with minimal parties only | 🟡 L2 | `APP` |
| [3.4.2](#req-3-4-2) | Share minimal data only | 🟡 L2 | `APP` |
| [3.4.3](#req-3-4-3) | Application-level data access tracking | 🟣 L3 | `APP` |
| [3.4.4](#req-3-4-4) | Machine-readable export | 🟣 L3 | `SYS` |

<a id="req-3-4-1"></a>
### 3.4.1 Share with minimal parties only

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Personal data must be shared only with the recipients that are required for the specific purpose of the exchange, whether those recipients are fixed in advance or determined dynamically at runtime.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The purpose of the exchange is the organisation's own reason for sharing the data, defined before the exchange happens. It is not the recipient's service description.  
A recipient is required only if the purpose cannot be achieved without it. Where an equivalent result can be had by sharing with fewer parties, share with fewer.  
Easy-to-miss recipients include analytics and tracking services, email delivery providers, speech-to-text services, and advertisers.  
Data disclosed to other users of the service counts as dynamic sharing. The audience settings that decide who sees the data are part of the exchange.  
Applies to processors, partner integrations, and client-side components that transmit personal data to third-party servers.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect, fixed recipients: for each sharing flow, identify the specific purpose of the exchange as defined by the organisation. A purpose that could apply to any exchange, such as "business purposes", does not satisfy this requirement. Compare each recipient against what that purpose requires. Any recipient the purpose does not require is a finding.  
Inspect, dynamic recipients: identify the rules that decide who receives the data at runtime, such as audience settings. Confirm they are bounded by the purpose of the exchange.  
Test: share a test record and confirm it reaches only the intended recipients.

</div>

<a id="req-3-4-2"></a>
### 3.4.2 Share minimal data only

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Each export or external transmission must contain only the personal data that is required for the specific purpose of the exchange.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The purpose of the exchange is the organisation's own reason for sharing the data, defined before the exchange happens. It is not the recipient's service description.  
Define the purpose narrowly enough to say which fields are not needed. "Verify the user met the weekly activity threshold" supports sending one number. "Wellness programme" supports sending almost anything.  
To judge what the purpose requires, check each of: data types, granularity, encoding and embedded metadata, volume, frequency, and data subjects.  
Send aggregated or coarser values where the purpose allows. A smart meter sends aggregate consumption, not real-time readings.  
Strip embedded metadata. Remove location data from images and author or reviewer details from documents.  
Send data at the lowest frequency that works. Weekly weight readings may suffice where half-hourly ones are collected.  
Remove other individuals' data that appears inside a user's content.  
Include sensitive data types only when strictly required.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: for each export and external interface, identify the specific purpose of the exchange as defined by the organisation. A purpose that could apply to any exchange, such as "business purposes", does not satisfy this requirement. Compare what is sent against what that purpose requires on each dimension: data types, granularity, encoding and embedded metadata, volume, frequency, and data subjects. Any excess is a finding.  
Test: capture a sample export or payload and check it for unneeded fields, excess precision, embedded metadata, surplus records, and personal data of other individuals.

</div>

<a id="req-3-4-3"></a>
### 3.4.3 Application-level data access tracking

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Where the system processes sensitive personal data, or where law or the sensitivity of the processing requires audit of data access, the system must log every data access event, recording at minimum: the data accessed, the identity of the accessor, the time of access, and the purpose of access.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Logging is conditional. Typical triggers are special category data, financial data, healthcare, legal, or a legal mandate.  
In low-sensitivity contexts, system-level security logs may suffice.  
Capturing the purpose may mean accessors must state it when they open specific personal data, so it can be reported back to the data subject.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm access logging is enabled for each data store holding sensitive personal data and that each log entry contains the four required fields.  
Test: access a test record and confirm a log entry is written with all four fields.

</div>

<a id="req-3-4-4"></a>
### 3.4.4 Machine-readable export

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must enable a user to retrieve all their personal data and export it in a structured, non-proprietary, machine-readable format such as JSON or CSV.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Proprietary formats that require specific software to parse do not satisfy this requirement.  
Use descriptive field names and values rather than internal codes, and include a description of each field so the export can be interpreted without access to the system.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: export the data for a test subject and parse the result with a standard parser. Confirm no vendor software is needed and that the export covers all data held for that subject. Confirm each field can be understood from the export and its accompanying description alone.

</div>

---

<a id="section-3-5"></a>
## 3.5 Data Deletion

Deletion means permanently removing personal data so that it is no longer accessible or recoverable. The obligation can be met through secure deletion (logical overwriting, as described in NIST SP 800-88 Clear, which suffices for most application data), cryptographic erasure (destroying the encryption key, permitted only where secure deletion is not technically feasible and the data was already encrypted before storage) or physical destruction (NIST SP 800-88 Destroy, for media that cannot be sanitized by other means). Requirements that mention deletion refer to the obligation, whatever technique meets it, and that obligation arises when a retention period expires, when the purpose is complete, or when a data subject asks for it. Anonymization is explicitly excluded as a deletion technique. Cryptographic erasure also deserves caution, because ciphertext harvested today could be decrypted later if quantum-safe algorithms are not in use, so without physical protections against harvesting it may stop being a valid defense.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [3.5.1](#req-3-5-1) | Secure deletion as default | 🟢 L1 | `SYS` |
| [3.5.2](#req-3-5-2) | On Demand Deletion | 🟡 L2 | `SYS` |
| [3.5.3](#req-3-5-3) | Deletion from backups | 🟡 L2 | `SYS` |
| [3.5.4](#req-3-5-4) | Deletion from logs | 🟡 L2 | `SYS` |
| [3.5.5](#req-3-5-5) | Deletion of temporary data | 🟡 L2 | `SYS` |
| [3.5.6](#req-3-5-6) | Deletion from 3rd parties | 🟣 L3 | `SYS` |
| [3.5.7](#req-3-5-7) | Deletion evidence | 🟣 L3 | `SYS` |

<a id="req-3-5-1"></a>
### 3.5.1 Secure deletion as default

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Personal data which is subject to a deletion obligation must be erased by secure deletion from primary data stores.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Secure deletion is the default.

Cryptographic erasure requires two conditions: (a) technical infeasibility of secure deletion, AND (b) pre-existing encryption. Retroactive encryption to avoid deletion does not satisfy (b).

Cryptographic erasure is permitted as an alternative only where secure deletion is not technically feasible due to an architectural constraint, and only where encryption was applied to the data prior to storage. This infeasibility must be documented at design time.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review deletion implementation for each storage component. Any component using cryptographic erasure must have documented infeasibility of secure deletion and evidence of pre-existing encryption. Absence of either is a finding.

</div>

<a id="req-3-5-2"></a>
### 3.5.2 On Demand Deletion

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide a mechanism by which a deletion request, initiated by a data subject or by authorised personnel acting on their behalf, triggers the secure deletion process, without requiring manual intervention beyond authorising the request.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The point is one deletion pathway with two triggers, not a separate process for requests. A request-specific process is where backups, logs, caches, search indexes and derived data stores get missed.  
A bounded delay between request and deletion is acceptable (for example a cooling-off period), but it must be defined and enforced by the system.  
Personnel-initiated requests use the same mechanism, not direct database access, and their authorisation and the requester’s identity verification follow ASVS.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: identify the entry point for deletion requests (API, admin function, or queue event) and confirm it invokes the same deletion workflow as retention expiry rather than a separate code path. A process where engineers run manual queries per request does not satisfy this requirement.  
Test: seed a test subject’s data in each storage component (primary stores, replicas, caches, search indexes, derived stores, logs, and backups). Submit a request through each initiation path and confirm the data is removed from every component within the defined period. Any component still holding the data is a finding.

</div>

<a id="req-3-5-3"></a>
### 3.5.3 Deletion from backups

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Deletion must propagate to online and offline backups upon expiry of the applicable retention period, on-demand deletion, or any other deletion obligations.  
Where deletion from backups is not technically feasible, the restoration process must filter expired or deleted personal data such that it is not reinstated into live systems.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Restoration filtering is an explicit fallback, not an equal alternative: deletion from backups is preferred. The filtering must be automatic, not manual.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: trigger deletion for a test subject/record. Inspect backup contents at next backup cycle and confirm the deleted data is absent.

Test: simulate a restoration from a backup containing deleted data. Confirm deleted data does not appear in the restored live system.

</div>

<a id="req-3-5-4"></a>
### 3.5.4 Deletion from logs

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Deletion must extend to all stored logs containing personal data upon expiry of the applicable retention period, on-demand deletion, or any other deletion obligations.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Logs are the most commonly missed deletion scope. Note tension with security audit log requirements — guidance should address the conflict.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: trigger deletion for a test subject/record. Inspect log stores and confirm the subject's personal data fields are deleted or pseudonymised. Retention of personal data in logs beyond the retention period is a finding.

</div>

<a id="req-3-5-5"></a>
### 3.5.5 Deletion of temporary data

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Deletion must extend to all locations where personal data was written during processing, including caches, temp files, working memory snapshots, and intermediate pipeline outputs.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: trigger deletion for a test record. Inspect temporary storage, caches, and pipeline output locations. Any location retaining the data after deletion is a finding.

</div>

<a id="req-3-5-6"></a>
### 3.5.6 Deletion from 3rd parties

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

When personal data is deleted, the deletion process must also request deletion of that data from every recipient it was shared with, and record the outcome.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Applies to deletion triggered by retention expiry or on request. Where the recipient acts on the system’s behalf (for example a processor or cloud service), deletion must be completed and confirmed. Other recipients use the data for their own purposes, so the system can only make the request and record the response. For bounded operations, prefer recipients and settings that do not retain the data after the operation completes (zero-retention API options, for example).

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm each recipient has a deletion interface, or a documented reason it has none.  
Test: delete a test subject’s data and confirm a request reaches each recipient and its outcome is recorded.

</div>

<a id="req-3-5-7"></a>
### 3.5.7 Deletion evidence

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide evidence that deletion triggered by a deletion obligation has occurred, in the form of deletion logs or equivalent audit trail, without retaining the personal data itself in the log.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The constraint "without retaining the personal data itself in the log" is the technically hard part: deletion logs must record that deletion occurred without logging the deleted content.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review deletion log schema — confirm it records deletion events without retaining personal data fields. Test: trigger deletion and confirm a log entry exists. Log entries containing personal data content are a finding.

</div>

---

<p style="opacity:.7;font-size:.9em">
<a href="00-introduction.md">Introduction</a> · <a href="02-minimality.md">Previous: Minimality</a> · <a href="04-transparency-notice.md">Next: Transparency & Notice</a>
</p>
