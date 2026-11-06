---
layout: default
title: "Chapter 1: Architecture & Data Mapping"
nav_order: 2
---

# Chapter 1. Architecture & Data Mapping

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance and verification text (shaded and in italics below) are in beta. Requirement type is waiting for community comments, and the chapter and section introductions are in beta as well. Wording will keep moving as feedback arrives.
</div>

Covers how an application records which personal data it holds, why it holds it, whose it is, and where it travels. It exists because every later privacy control, from minimization to deletion, depends on knowing what the system actually contains.

## About this chapter

Privacy controls act on data, so they can only be as good as the system's knowledge of where that data is. This chapter asks an application to keep that knowledge in a form that machines and reviewers can both use, through a catalog of personal data elements, metadata on the records themselves, an index that gathers everything held about one person, and an inventory of the interfaces through which data enters and leaves. A team that cannot answer "what do we hold, why, and who else sees it" will find that deletion, access requests, retention and transparency each turn into a separate archaeology project.

The reasoning follows from how personal data behaves in real systems. It spreads into logs, caches, backups, search indexes, message queues and analytics stores, and it also arrives through client-side scripts and SDKs that nobody on the team explicitly invoked. Documentation written once and filed away drifts out of date at the first refactor. For that reason the requirements favor records that live inside the system, such as annotated schemas, record-level tags and machine-readable inventories, and they ask for automated comparison between what is declared and what the code, the build and the network egress actually do. A mismatch should fail a build or raise an alert, so that the map stays accurate as the system changes.

Purpose is the thread running through all of this. Every data element and every processing operation needs a specific purpose recorded before collection or processing starts, and a purpose that could be pasted unchanged onto a different field does not count as specific. Recording purpose early gives later chapters something concrete to check against, whether that is minimization, retention or notice.

Several of these artifacts also serve a purpose beyond the application. The data inventory, purpose register, metadata schema and data flow documentation form the system-level evidence base from which an organization can derive its Record of Processing Activities. The Record of Processing Activities itself is an organizational accountability document and sits outside this standard, which concentrates on the technical facts that such a record has to rest on.

Knowing whether a value was provided by the person, obtained from a third party or inferred by the system, and when it was last collected, lets later controls treat each kind of data appropriately. Being able to resolve every identifier of a person to one complete set of records is what makes access, correction and erasure feasible in practice.

## Sections at a glance

| Section | Title | Requirements | <span style="color:#1a7f37">L1</span> | <span style="color:#9a6700">L2</span> | <span style="color:#8250df">L3</span> |
|---|---|---:|---:|---:|---:|
| [1.1](#section-1-1) | Data Inventory | 1 | 1 | 0 | 0 |
| [1.2](#section-1-2) | Metadata Tagging | 3 | 0 | 3 | 0 |
| [1.3](#section-1-3) | Data Subject Linkage | 2 | 0 | 0 | 2 |
| [1.4](#section-1-4) | Data Flow Documentation | 3 | 0 | 2 | 1 |

---

<a id="section-1-1"></a>
## 1.1 Data Inventory

The data inventory is the foundation for everything else in the standard. It lists the personal data elements the system handles, including the less visible places such as logs, backups and derived data, without ever holding the values themselves.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [1.1.1](#req-1-1-1) | Personal data catalog | 🟢 L1 | `SYS` |

<a id="req-1-1-1"></a>
### 1.1.1 Personal data catalog

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must maintain a catalog of personal data elements collected, stored, or processed. For each element the catalog must record: the data category, the field or attribute name, the data subject type to which it relates, and the processing purpose(s) it serves. The catalog must not contain actual personal data values.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Scope: "stored or processed" includes the places personal data is most often missed: logs, backups, caches, search indexes, message queues, analytics and telemetry stores, and derived or inferred data. A catalog that covers only primary databases is incomplete.

Note this catalog must be implemented in the system (e.g. an annotated database schema), just documentation does not suffice.

This does not necessarily assume data in a database, but that is one possibility (of many).  
Note this does mean fields are "all or nothing". For example, if a field is used to store a comment with free-form text in a chat app, the field could contain personal information in part or wholly; this must enter the data catalog.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review database schemas, API definitions, and data store contents against the catalog. Any personal data element present in the system but absent from the catalog is a finding.

</div>

---

<a id="section-1-2"></a>
## 1.2 Metadata Tagging

Record-level metadata describes each piece of stored personal data: what it is, why it was collected, whom it concerns, where it came from and when it was last collected. This gives retention, minimization and rights handling the facts they need, and it makes the purpose of collection explicit before the first value arrives.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [1.2.1](#req-1-2-1) | Metadata tagging of personal records | 🟡 L2 | `APP` |
| [1.2.2](#req-1-2-2) | Collection purpose specification | 🟡 L2 | `APP` |
| [1.2.3](#req-1-2-3) | Last collection timestamp | 🟡 L2 | `APP` |

<a id="req-1-2-1"></a>
### 1.2.1 Metadata tagging of personal records

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Personal data in storage must be tagged with metadata, including: data type, collection purpose(s), business purpose(s), associated data subjects and their relationship to the data, data lineage, and data provenance classification (whether the data was provided directly by the data subject, collected from a third party, or derived or inferred by the system).

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Note that "Personal data catalog" (v1.1.1) referes to architectural structure and storage locations, whereas this requirement refers to record-level metadata.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: sample personal data records across storage components and confirm metadata tags are present and populated according to the schema. Untagged records are a finding.

</div>

<a id="req-1-2-2"></a>
### 1.2.2 Collection purpose specification

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Each personal data element collected by the system must have a documented, specific collection purpose, recorded in the metadata or catalog before collection begins.  
The system may not collect data elements that do not have a specified purpose in the system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

A purpose stated at the level of the system or organisation as a whole does not satisfy this requirement. A purpose that could be copy-pasted unchanged to a different data element fails this test. Examples of insufficient purposes: "to improve our service", "for business purposes", "analytics".

The record must exist before the first value is collected, not be back-filled afterwards.

The automated check can confirm that an entry exists and is not empty or a placeholder. Judging whether a purpose is specific remains a review task.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: review purpose entries. Any purpose that would apply unchanged to a different data element or processing activity is a finding.  
Inspect: confirm an automated check matches schemas and API definitions against the purpose register on every change and fails the build or release on a mismatch. A missing check, or one that does not block, is a finding.  
Test: add a personal data field with no purpose entry to a schema or API definition and confirm the pipeline fails.  
Verify by: comparing database schemas and API request payloads against the purpose register. Any collected field without a corresponding collection purpose entry is a finding.

</div>

<a id="req-1-2-3"></a>
### 1.2.3 Last collection timestamp

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must record, for each personal data record, the time at which the system last collected that data.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This is the time the system collected the data, not the time of the event the data describes, and not the time the record was last modified. Edits, migrations, and backups restoring the record must leave it unchanged.

The system sets the timestamp itself; a value supplied by a client or caller is not used.

It is the reference point for retention periods and for progressively reducing the granularity of aging data (Ch3). Without it, age-based handling has to guess from other fields.

If the same data is recollected, the system must set this timestamp automatically at each collection event, including each time the data is re-collected or refreshed from the data subject or another source.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: sample personal data records across storage components. Any record without a collection timestamp is a finding.  
Test: collect a new record and confirm the timestamp matches the collection time. Collect the same data again and confirm the timestamp advances. Supply a timestamp value in the request and confirm it is ignored. Modify the record through an unrelated edit and confirm the timestamp does not change.

</div>

---

<a id="section-1-3"></a>
## 1.3 Data Subject Linkage

Data subject linkage lets the system find everything it holds about one person, whichever identifier is used to ask. This capability is what makes access, correction and erasure workable across many storage components.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [1.3.1](#req-1-3-1) | Data subject identifier index | 🟣 L3 | `SYS` |
| [1.3.2](#req-1-3-2) | Multiple identifier support | 🟣 L3 | `SYS` |

<a id="req-1-3-1"></a>
### 1.3.1 Data subject identifier index

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must index all personal data on data subject identifiers, such that all data attributable to a specific data subject can be retrieved across all storage components.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The index must reference personal data by identifier or pointer; it must not contain actual personal data values.

The index must be sufficiently detailed that a reviewer can locate any personal data element in the system without prior knowledge of the system architecture.

Scope: the index must make it possible to enumerate all personal data held about a specific data subject across all storage components, including primary databases, logs, backups, caches, derived data, and data held by processors on behalf of the controller.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: insert personal data for a test subject across multiple storage components using a known identifier. Query the index and confirm all inserted records are returned. Any record not returned is a finding.

Test 2: inspecting the index for presence of actual personal data values -- any index entry containing personal data content rather than a reference or pointer is a finding. Select a sample of data elements and confirm each can be located in the system using only the index.

</div>

<a id="req-1-3-2"></a>
### 1.3.2 Multiple identifier support

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The data subject identifier index must support multiple identifiers per data subject (e.g. email address, account ID, device identifier) and must resolve all known identifiers to the same subject record. The index must not retain identifiers beyond what is necessary to fulfil data subject rights and other documented purposes.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: create a test subject with two distinct identifiers across different components. Query on each identifier separately and confirm both return the complete dataset. Any identifier that returns an incomplete result is a finding.

</div>

---

<a id="section-1-4"></a>
## 1.4 Data Flow Documentation

Data flow documentation covers what crosses the boundary of the system, including collection that happens passively through third-party components, and the purpose behind each processing operation. It is kept machine-readable, and where components can be detected automatically the inventory is checked against them, so that new flows show up as soon as they exist.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [1.4.1](#req-1-4-1) | External Interfaces Documentation | 🟡 L2 | `APP` |
| [1.4.2](#req-1-4-2) | Passive and third-party collection | 🟡 L2 | `APP` |
| [1.4.3](#req-1-4-3) | Processing purpose specification | 🟣 L3 | `APP` |

<a id="req-1-4-1"></a>
### 1.4.1 External Interfaces Documentation

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must maintain a machine-readable inventory of all external interfaces involving personal data, including: personal data received from external sources; personal data transmitted to third parties or external systems; and personal data accessible to external parties through APIs, exports, or direct access.

For each interface, the inventory must identify the external party, the personal data categories involved, the direction of interface, and the processing purpose it serves.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Includes client-side components that transmit personal data to third-party servers, even where the application does not directly initiate or control the transmission. Incoming flows, such as data received from data brokers, identity providers, or partner systems, are in scope alongside outbound flows.

Build-time comparison catches declared integrations (API clients, dependencies); egress monitoring catches the rest. Both are needed, since neither sees everything.

The system must automatically compare the inventory against actual integrations (API clients and definitions, third-party scripts and SDKs, and network egress), and must raise an alert for any external interface involving personal data that is not in the inventory.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Architecture review: compare documented external flows against actual system integrations, API definitions, and network egress. Any external flow involving personal data that is absent from documentation is a finding.  
Inspect: confirm an automated comparison of the inventory against integrations and network egress exists and fails the build or raises an alert on a mismatch. A missing comparison, or one that covers only some of these sources, is a finding.  
Test: add a new third-party endpoint or SDK that receives personal data and confirm the comparison flags it.

</div>

<a id="req-1-4-2"></a>
### 1.4.2 Passive and third-party collection

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must maintain a machine-readable inventory of third-party components that collect personal data without being explicitly invoked by application code, such as analytics SDKs, tags, pixels, crash reporters, and device-identifier libraries, and of the personal data each one collects (for example device identifiers, IP address, and request headers). The system must automatically detect such components in builds and in deployed client code, and must fail the build or raise an alert for any component that is not in the inventory.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

E.g. analytics SDKs, tags, crash reporters, device identifiers, and IP or headers captured in logs.  
Indirect collection: purchased, scraped, or inferred data should record its source at ingestion.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: compare dependency manifests, build artifacts, and tag manager configuration against the inventory. Any component that collects personal data and is absent from the inventory is a finding.  
Inspect: confirm automated detection exists and fails the build or raises an alert when a new SDK or tag is added.  
Test: load the application in a clean browser or device session and capture network traffic. Any third-party endpoint receiving personal data that is not in the inventory is a finding.

</div>

<a id="req-1-4-3"></a>
### 1.4.3 Processing purpose specification

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

Each processing operation performed on personal data - including storage, internal use, sharing, and further processing - must have a documented, specific purpose registered in the system before the operation begins.  
The system may not perform the processing without having a specified purpose in the system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Specific as defined in 1.2.2. Record, with the purpose, the timeframe of data the operation needs (see 3.2.5).

The automated match covers operations that can be identified in code or configuration. Operations that cannot (ad-hoc queries, manual exports) still need a registered purpose and are verified by inspection.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Verify by: tracing data flows — queries, API calls, data sharing integrations — against the purpose register. Any processing operation not covered by a registered processing purpose is a finding.  
Inspect: confirm an automated check matches operations identifiable in code or configuration against the purpose register and fails the build or release on a mismatch. A missing or non-blocking check is a finding.  
Test: add a new query, job, or integration that processes personal data without a registered purpose and confirm the pipeline fails.

</div>

---

<p style="opacity:.7;font-size:.9em">
<a href="00-introduction.md">Introduction</a> · <a href="02-minimality.md">Next: Minimality</a>
</p>
