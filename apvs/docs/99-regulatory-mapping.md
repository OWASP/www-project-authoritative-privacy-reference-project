---
layout: default
title: "Appendix A: Regulatory Mapping"
nav_order: 99
---

# Appendix A. Regulatory Mapping

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
This mapping is a working aid for engineers and privacy teams. It follows the requirements as they stand in this version and will change with them. It is not legal advice.
</div>

This appendix is reference material and sits outside the numbered chapters. APVS is organized around system design, and regulations are organized around legal duties, so the appendix connects the two from both directions. Each regulation has its own section below, with an overview, the detail for every provision and the provisions that APVS has nothing to say about. The last section starts from the requirements and lists the provisions each one supports.

Coverage tells you how far APVS goes for a provision. **●●● Direct** means the requirements cover the application-level obligation fairly completely, **●●○ Partial** means they cover part of it, and **●○○ Supporting** means they yield evidence or building blocks for it.

## A.1 GDPR

This mapping lists the GDPR articles that an application has to support technically and shows which APVS requirements help an application meet each one. Coverage "direct" means the APVS requirements address the application-level obligation fairly completely, "partial" means they address part of it, and "supporting" means they yield evidence or building blocks that other measures must complete. APVS is a verification standard for applications, so the mapping is a guide for engineers and cannot replace legal analysis of a specific processing activity.

### Overview

| Article | Title | Coverage | APVS requirements |
|---|---|---|---|
| [Art. 5(1)(a)](#gdpr-art-5-1-a) | Lawfulness, fairness and transparency | **●●○ Partial** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.2](04-transparency-notice.md#req-4-1-2), [4.1.7](04-transparency-notice.md#req-4-1-7), [4.2.9](04-transparency-notice.md#req-4-2-9), [4.3.2](04-transparency-notice.md#req-4-3-2), [4.1.3](04-transparency-notice.md#req-4-1-3) |
| [Art. 5(1)(b)](#gdpr-art-5-1-b) | Purpose limitation | **●●● Direct** | [1.2.2](01-architecture-data-mapping.md#req-1-2-2), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [2.1.3](02-minimality.md#req-2-1-3), [4.1.3](04-transparency-notice.md#req-4-1-3) |
| [Art. 5(1)(c)](#gdpr-art-5-1-c) | Data minimisation | **●●● Direct** | [2.1.1](02-minimality.md#req-2-1-1), [2.1.2](02-minimality.md#req-2-1-2), [2.1.4](02-minimality.md#req-2-1-4), [2.1.5](02-minimality.md#req-2-1-5), [2.1.6](02-minimality.md#req-2-1-6), [2.1.7](02-minimality.md#req-2-1-7), [2.2.1](02-minimality.md#req-2-2-1), [2.2.2](02-minimality.md#req-2-2-2), [2.2.3](02-minimality.md#req-2-2-3), [2.2.4](02-minimality.md#req-2-2-4), [2.2.5](02-minimality.md#req-2-2-5), [2.2.6](02-minimality.md#req-2-2-6), [2.2.7](02-minimality.md#req-2-2-7), [3.1.1](03-data-lifecycle-management.md#req-3-1-1), [3.2.4](03-data-lifecycle-management.md#req-3-2-4), [3.4.2](03-data-lifecycle-management.md#req-3-4-2) |
| [Art. 5(1)(d)](#gdpr-art-5-1-d) | Accuracy | **●●○ Partial** | [3.3.4](03-data-lifecycle-management.md#req-3-3-4), [1.2.3](01-architecture-data-mapping.md#req-1-2-3), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [5.1.2](05-privacy-features.md#req-5-1-2) |
| [Art. 5(1)(e)](#gdpr-art-5-1-e) | Storage limitation | **●●● Direct** | [3.3.1](03-data-lifecycle-management.md#req-3-3-1), [3.3.3](03-data-lifecycle-management.md#req-3-3-3), [3.3.2](03-data-lifecycle-management.md#req-3-3-2), [3.2.1](03-data-lifecycle-management.md#req-3-2-1), [3.2.2](03-data-lifecycle-management.md#req-3-2-2), [3.5.1](03-data-lifecycle-management.md#req-3-5-1), [3.5.3](03-data-lifecycle-management.md#req-3-5-3), [3.5.4](03-data-lifecycle-management.md#req-3-5-4), [3.5.5](03-data-lifecycle-management.md#req-3-5-5), [1.2.3](01-architecture-data-mapping.md#req-1-2-3), [2.1.3](02-minimality.md#req-2-1-3) |
| [Art. 5(1)(f)](#gdpr-art-5-1-f) | Integrity and confidentiality | **●○○ Supporting** | [3.3.6](03-data-lifecycle-management.md#req-3-3-6), [3.3.7](03-data-lifecycle-management.md#req-3-3-7), [3.4.3](03-data-lifecycle-management.md#req-3-4-3), [3.5.1](03-data-lifecycle-management.md#req-3-5-1) |
| [Art. 5(2)](#gdpr-art-5-2) | Accountability | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [3.5.7](03-data-lifecycle-management.md#req-3-5-7), [4.2.6](04-transparency-notice.md#req-4-2-6), [3.4.3](03-data-lifecycle-management.md#req-3-4-3) |
| [Art. 6(1)(a)](#gdpr-art-6-1-a) | Lawfulness of processing (consent as legal basis) | **●●○ Partial** | [4.2.2](04-transparency-notice.md#req-4-2-2), [4.2.3](04-transparency-notice.md#req-4-2-3), [4.2.1](04-transparency-notice.md#req-4-2-1), [4.2.9](04-transparency-notice.md#req-4-2-9), [4.2.10](04-transparency-notice.md#req-4-2-10), [4.2.8](04-transparency-notice.md#req-4-2-8), [4.2.6](04-transparency-notice.md#req-4-2-6), [4.2.7](04-transparency-notice.md#req-4-2-7), [4.2.5](04-transparency-notice.md#req-4-2-5), [4.1.1](04-transparency-notice.md#req-4-1-1) |
| [Art. 6(4)](#gdpr-art-6-4) | Lawfulness of processing (further processing) | **●●○ Partial** | [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [1.4.3](01-architecture-data-mapping.md#req-1-4-3) |
| [Art. 7(1)](#gdpr-art-7-1) | Conditions for consent (demonstrating consent) | **●●● Direct** | [4.2.6](04-transparency-notice.md#req-4-2-6), [4.1.1](04-transparency-notice.md#req-4-1-1) |
| [Art. 7(2)](#gdpr-art-7-2) | Conditions for consent (distinguishable request) | **●●● Direct** | [4.2.4](04-transparency-notice.md#req-4-2-4), [4.2.3](04-transparency-notice.md#req-4-2-3), [4.3.3](04-transparency-notice.md#req-4-3-3) |
| [Art. 7(3)](#gdpr-art-7-3) | Conditions for consent (withdrawal) | **●●● Direct** | [4.2.5](04-transparency-notice.md#req-4-2-5), [4.3.4](04-transparency-notice.md#req-4-3-4), [5.2.2](05-privacy-features.md#req-5-2-2) |
| [Art. 7(4)](#gdpr-art-7-4) | Conditions for consent (freely given) | **●●● Direct** | [4.2.7](04-transparency-notice.md#req-4-2-7), [2.1.5](02-minimality.md#req-2-1-5), [4.2.3](04-transparency-notice.md#req-4-2-3) |
| [Art. 8](#gdpr-art-8) | Conditions applicable to child's consent in relation to information society services | **●○○ Supporting** | [2.2.2](02-minimality.md#req-2-2-2) |
| [Art. 9](#gdpr-art-9) | Processing of special categories of personal data | **●○○ Supporting** | [3.1.2](03-data-lifecycle-management.md#req-3-1-2), [3.4.3](03-data-lifecycle-management.md#req-3-4-3), [2.1.4](02-minimality.md#req-2-1-4), [3.4.2](03-data-lifecycle-management.md#req-3-4-2) |
| [Art. 11](#gdpr-art-11) | Processing which does not require identification | **●○○ Supporting** | [2.2.3](02-minimality.md#req-2-2-3), [2.1.2](02-minimality.md#req-2-1-2), [1.3.2](01-architecture-data-mapping.md#req-1-3-2), [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Art. 12](#gdpr-art-12) | Transparent information, communication and modalities for the exercise of the rights of the data subject | **●●○ Partial** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.2](04-transparency-notice.md#req-4-1-2), [4.2.4](04-transparency-notice.md#req-4-2-4), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.4](05-privacy-features.md#req-5-1-4), [5.1.3](05-privacy-features.md#req-5-1-3), [5.1.2](05-privacy-features.md#req-5-1-2), [4.3.1](04-transparency-notice.md#req-4-3-1) |
| [Art. 13](#gdpr-art-13) | Information to be provided where personal data are collected from the data subject | **●●○ Partial** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.2](04-transparency-notice.md#req-4-1-2), [4.1.3](04-transparency-notice.md#req-4-1-3), [4.1.4](04-transparency-notice.md#req-4-1-4), [4.1.5](04-transparency-notice.md#req-4-1-5), [4.1.8](04-transparency-notice.md#req-4-1-8), [4.1.7](04-transparency-notice.md#req-4-1-7), [5.1.4](05-privacy-features.md#req-5-1-4), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.2](01-architecture-data-mapping.md#req-1-4-2) |
| [Art. 14](#gdpr-art-14) | Information to be provided where personal data have not been obtained from the data subject | **●●○ Partial** | [4.1.6](04-transparency-notice.md#req-4-1-6), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [4.1.3](04-transparency-notice.md#req-4-1-3), [4.1.4](04-transparency-notice.md#req-4-1-4), [4.1.5](04-transparency-notice.md#req-4-1-5), [4.1.8](04-transparency-notice.md#req-4-1-8), [4.1.7](04-transparency-notice.md#req-4-1-7) |
| [Art. 15](#gdpr-art-15) | Right of access by the data subject | **●●○ Partial** | [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [1.3.2](01-architecture-data-mapping.md#req-1-3-2), [3.4.4](03-data-lifecycle-management.md#req-3-4-4), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.2](05-privacy-features.md#req-5-1-2), [5.1.3](05-privacy-features.md#req-5-1-3), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [4.3.7](04-transparency-notice.md#req-4-3-7), [3.4.3](03-data-lifecycle-management.md#req-3-4-3) |
| [Art. 16](#gdpr-art-16) | Right to rectification | **●●○ Partial** | [3.3.4](03-data-lifecycle-management.md#req-3-3-4), [5.1.2](05-privacy-features.md#req-5-1-2), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Art. 17](#gdpr-art-17) | Right to erasure ('right to be forgotten') | **●●● Direct** | [3.5.2](03-data-lifecycle-management.md#req-3-5-2), [3.5.1](03-data-lifecycle-management.md#req-3-5-1), [3.5.3](03-data-lifecycle-management.md#req-3-5-3), [3.5.4](03-data-lifecycle-management.md#req-3-5-4), [3.5.5](03-data-lifecycle-management.md#req-3-5-5), [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [3.5.7](03-data-lifecycle-management.md#req-3-5-7), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.2](05-privacy-features.md#req-5-1-2), [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Art. 18](#gdpr-art-18) | Right to restriction of processing | **●●○ Partial** | [5.1.2](05-privacy-features.md#req-5-1-2), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [5.1.1](05-privacy-features.md#req-5-1-1), [5.2.2](05-privacy-features.md#req-5-2-2) |
| [Art. 19](#gdpr-art-19) | Notification obligation regarding rectification or erasure of personal data or restriction of processing | **●●○ Partial** | [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [3.4.1](03-data-lifecycle-management.md#req-3-4-1) |
| [Art. 20](#gdpr-art-20) | Right to data portability | **●●○ Partial** | [3.4.4](03-data-lifecycle-management.md#req-3-4-4), [5.1.2](05-privacy-features.md#req-5-1-2), [5.1.1](05-privacy-features.md#req-5-1-1), [1.3.1](01-architecture-data-mapping.md#req-1-3-1) |
| [Art. 21](#gdpr-art-21) | Right to object | **●●○ Partial** | [5.2.1](05-privacy-features.md#req-5-2-1), [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.4](04-transparency-notice.md#req-4-3-4), [4.3.6](04-transparency-notice.md#req-4-3-6), [4.3.2](04-transparency-notice.md#req-4-3-2) |
| [Art. 24](#gdpr-art-24) | Responsibility of the controller | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [3.5.7](03-data-lifecycle-management.md#req-3-5-7), [4.2.6](04-transparency-notice.md#req-4-2-6) |
| [Art. 25(1)](#gdpr-art-25-1) | Data protection by design | **●●○ Partial** | [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [2.1.1](02-minimality.md#req-2-1-1), [2.1.2](02-minimality.md#req-2-1-2), [2.1.6](02-minimality.md#req-2-1-6), [3.1.1](03-data-lifecycle-management.md#req-3-1-1), [3.2.3](03-data-lifecycle-management.md#req-3-2-3), [3.2.4](03-data-lifecycle-management.md#req-3-2-4), [3.3.5](03-data-lifecycle-management.md#req-3-3-5), [3.3.6](03-data-lifecycle-management.md#req-3-3-6), [3.3.3](03-data-lifecycle-management.md#req-3-3-3) |
| [Art. 25(2)](#gdpr-art-25-2) | Data protection by default | **●●● Direct** | [2.1.1](02-minimality.md#req-2-1-1), [2.1.5](02-minimality.md#req-2-1-5), [2.2.1](02-minimality.md#req-2-2-1), [4.2.2](04-transparency-notice.md#req-4-2-2), [3.3.1](03-data-lifecycle-management.md#req-3-3-1), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [4.3.5](04-transparency-notice.md#req-4-3-5), [2.1.2](02-minimality.md#req-2-1-2), [3.4.2](03-data-lifecycle-management.md#req-3-4-2), [3.3.3](03-data-lifecycle-management.md#req-3-3-3) |
| [Art. 28](#gdpr-art-28) | Processor | **●○○ Supporting** | [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [1.3.1](01-architecture-data-mapping.md#req-1-3-1) |
| [Art. 30](#gdpr-art-30) | Records of processing activities | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.2.2](01-architecture-data-mapping.md#req-1-2-2), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.2](01-architecture-data-mapping.md#req-1-4-2), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [3.3.1](03-data-lifecycle-management.md#req-3-3-1) |
| [Art. 32](#gdpr-art-32) | Security of processing | **●○○ Supporting** | [3.3.5](03-data-lifecycle-management.md#req-3-3-5), [3.3.6](03-data-lifecycle-management.md#req-3-3-6), [3.3.7](03-data-lifecycle-management.md#req-3-3-7), [3.4.3](03-data-lifecycle-management.md#req-3-4-3), [3.5.1](03-data-lifecycle-management.md#req-3-5-1) |
| [Art. 33](#gdpr-art-33) | Notification of a personal data breach to the supervisory authority | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [3.4.3](03-data-lifecycle-management.md#req-3-4-3) |
| [Art. 34](#gdpr-art-34) | Communication of a personal data breach to the data subject | **●○○ Supporting** | [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [1.3.2](01-architecture-data-mapping.md#req-1-3-2) |
| [Art. 35](#gdpr-art-35) | Data protection impact assessment | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [2.1.1](02-minimality.md#req-2-1-1), [2.1.2](02-minimality.md#req-2-1-2), [3.4.3](03-data-lifecycle-management.md#req-3-4-3) |

### Principles

<a id="gdpr-art-5-1-a"></a>
#### Art. 5(1)(a) Lawfulness, fairness and transparency

**●●○ Partial**

Personal data must be processed lawfully, fairly and in a way the data subject can see and understand.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | A versioned notice shown before collection gives the data subject the information needed to understand the processing. |
| [4.1.2 Contextual notice per processing activity](04-transparency-notice.md#req-4-1-2) | Notices tied to each processing activity keep the information relevant at the point where data is collected. |
| [4.1.7 Material change notification](04-transparency-notice.md#req-4-1-7) | Advance notification of material changes keeps later processing within what people were told. |
| [4.2.9 Representative Framing of Privacy Choices](04-transparency-notice.md#req-4-2-9) | Prohibiting misleading necessity, urgency and social proof claims supports fair treatment around privacy choices. |
| [4.3.2 Functional privacy settings](04-transparency-notice.md#req-4-3-2) | Privacy settings that really change processing keep the interface truthful about what happens to data. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Required notice fields make the processing transparent to the data subject. |

<a id="gdpr-art-5-1-b"></a>
#### Art. 5(1)(b) Purpose limitation

**●●● Direct**

Data may be collected only for specified, explicit and legitimate purposes and may not be used in ways that are incompatible with them.

| APVS requirement | How it helps |
|---|---|
| [1.2.2 Collection purpose specification](01-architecture-data-mapping.md#req-1-2-2) | A specific purpose must be recorded for every data element before collection starts, with a build check against the register. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | Every processing operation needs a registered specific purpose before it runs, which makes undeclared uses detectable. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Record-level purpose tags record the collection purposes against which use can be checked. |
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | Runtime checks compare each use of data with its collection purpose and timeframe and require a prior compatibility record for secondary uses. |
| [2.1.3 Necessity reassessment on change or retirement](02-minimality.md#req-2-1-3) | Reassessing necessity when a purpose ends removes data whose purpose has ended. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | The notice states the purpose for each processing activity, which anchors what the data subject was told. |

<a id="gdpr-art-5-1-c"></a>
#### Art. 5(1)(c) Data minimisation

**●●● Direct**

Personal data must be adequate, relevant and limited to what the purposes require.

| APVS requirement | How it helps |
|---|---|
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Each data element must be necessary for its documented purpose, and merely useful elements are excluded. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Necessary elements are collected in their least detailed form, at the lowest volume and frequency that serves the purpose. |
| [2.1.4 Derived data precision](02-minimality.md#req-2-1-4) | Inferred and derived data face the same necessity and precision limits as collected data. |
| [2.1.5 Optional data not functionally mandatory](02-minimality.md#req-2-1-5) | Core functions must work without optional data, so optional fields cannot become mandatory. |
| [2.1.6 Abstract and aggregate](02-minimality.md#req-2-1-6) | Aggregated output replaces raw data where it satisfies the purpose. |
| [2.1.7 Granularity degradation over time](02-minimality.md#req-2-1-7) | Longitudinal data loses granularity on a schedule as it ages. |
| [2.2.1 Location data granularity](02-minimality.md#req-2-2-1) | Location data is held at the least precise level on a defined scale. |
| [2.2.2 Age / date of birth granularity](02-minimality.md#req-2-2-2) | Age data is reduced to a threshold check or the coarsest level that works. |
| [2.2.3 Identity granularity](02-minimality.md#req-2-2-3) | Identity data is held at the least linkable level that the feature allows. |
| [2.2.4 Photo metadata](02-minimality.md#req-2-2-4) | Photo metadata is stripped beyond the documented level. |
| [2.2.5 File metadata](02-minimality.md#req-2-2-5) | File metadata such as author and path details is limited to what the feature needs. |
| [2.2.6 Communication, call and message history](02-minimality.md#req-2-2-6) | Communication history is retained only at the least detailed level for metadata and content. |
| [2.2.7 Live streaming data](02-minimality.md#req-2-2-7) | Live stream capture is limited to the lowest fidelity that works. |
| [3.1.1 Discard collected data if purpose is met](03-data-lifecycle-management.md#req-3-1-1) | Data whose purpose is met during processing is kept in memory only and never persisted. |
| [3.2.4 Client-side computing](03-data-lifecycle-management.md#req-3-2-4) | Processing that can run on the user's device does so, and only the result reaches the backend. |
| [3.4.2 Share minimal data only](03-data-lifecycle-management.md#req-3-4-2) | Exports and transmissions carry only the fields the purpose of the exchange requires. |

<a id="gdpr-art-5-1-d"></a>
#### Art. 5(1)(d) Accuracy

**●●○ Partial**

Personal data must be accurate and kept up to date, and inaccurate data must be corrected or erased without delay.

| APVS requirement | How it helps |
|---|---|
| [3.3.4 Corrected data propagation](03-data-lifecycle-management.md#req-3-3-4) | A corrected value must reach replicas, caches and search indexes within a defined and enforced period. |
| [1.2.3 Last collection timestamp](01-architecture-data-mapping.md#req-1-2-3) | A system-set collection timestamp shows how current each record is and advances on each re-collection. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Provenance and lineage tags tell a team how reliable a record is and where a correction must start. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tooling lets authorized staff locate data for a specific person, which is where a correction starts. |

<a id="gdpr-art-5-1-e"></a>
#### Art. 5(1)(e) Storage limitation

**●●● Direct**

Data may be kept in identifiable form only as long as the purposes require.

| APVS requirement | How it helps |
|---|---|
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | A minimal retention period or its determining criteria is defined for every data class. |
| [3.3.3 Automated deletion at retention expiry](03-data-lifecycle-management.md#req-3-3-3) | Data is deleted automatically when its retention period expires, with no manual step. |
| [3.3.2 Residual retention window for temporary data](03-data-lifecycle-management.md#req-3-3-2) | Where immediate deletion is infeasible, a maximum residual window is defined and enforced. |
| [3.2.1 Deletion on processing completion](03-data-lifecycle-management.md#req-3-2-1) | Data created for a bounded operation is deleted when the operation completes. |
| [3.2.2 Deletion trigger mechanism](03-data-lifecycle-management.md#req-3-2-2) | Completion of an operation triggers deletion directly, without waiting for a periodic cleanup. |
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Deletion obligations are met by secure deletion from primary stores. |
| [3.5.3 Deletion from backups](03-data-lifecycle-management.md#req-3-5-3) | Deletion reaches online and offline backups or is filtered on restore. |
| [3.5.4 Deletion from logs](03-data-lifecycle-management.md#req-3-5-4) | Deletion covers logs that contain personal data. |
| [3.5.5 Deletion of temporary data](03-data-lifecycle-management.md#req-3-5-5) | Deletion covers caches, temporary files and intermediate pipeline output. |
| [1.2.3 Last collection timestamp](01-architecture-data-mapping.md#req-1-2-3) | The collection timestamp is the reference point for age-based retention. |
| [2.1.3 Necessity reassessment on change or retirement](02-minimality.md#req-2-1-3) | Data is removed when a processing activity changes or retires. |

<a id="gdpr-art-5-1-f"></a>
#### Art. 5(1)(f) Integrity and confidentiality

**●○○ Supporting**

Data must be processed with appropriate security against unauthorized access, loss, destruction or damage.

| APVS requirement | How it helps |
|---|---|
| [3.3.6 Pseudonym/identity mapping separation](03-data-lifecycle-management.md#req-3-3-6) | Keeping the pseudonym mapping in a separate store limits what a breach of the main system reveals. |
| [3.3.7 Pseudonymous audit logs](03-data-lifecycle-management.md#req-3-3-7) | Pseudonymous identifiers in logs reduce exposure of identities to those who read them. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logging on sensitive data records who touched what and when. |
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Secure deletion prevents recovery of data that should no longer exist. |

<a id="gdpr-art-5-2"></a>
#### Art. 5(2) Accountability

**●○○ Supporting**

The controller must be able to demonstrate compliance with the principles in Art. 5(1).

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | An in-system catalog of personal data elements provides a verifiable basis for showing what is processed and why. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | The purpose register is evidence that each operation had a declared purpose beforehand. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Deletion logs show that deletion obligations were carried out without retaining the deleted data. |
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | Consent records show what was agreed, when and under which notice version. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logs give an audit trail of who used sensitive data and for what purpose. |

### Lawfulness and consent

<a id="gdpr-art-6-1-a"></a>
#### Art. 6(1)(a) Lawfulness of processing (consent as legal basis)

**●●○ Partial**

Where consent is the legal basis, it must be a freely given, specific, informed and unambiguous choice that exists before the processing starts.

| APVS requirement | How it helps |
|---|---|
| [4.2.2 No pre-selection or inaction consent](04-transparency-notice.md#req-4-2-2) | Consent controls default to off, so consent always comes from an affirmative act. |
| [4.2.3 Consent granularity — one purpose per consent act](04-transparency-notice.md#req-4-2-3) | Consent is obtained separately for each purpose, which keeps it specific. |
| [4.2.1 Visual parity of privacy choices](04-transparency-notice.md#req-4-2-1) | Accept and reject options have equal prominence and effort, which keeps the choice free. |
| [4.2.9 Representative Framing of Privacy Choices](04-transparency-notice.md#req-4-2-9) | Interfaces may not misstate necessity or urgency to push a decision. |
| [4.2.10 No nagging](04-transparency-notice.md#req-4-2-10) | A declined request is not repeated, so refusal is respected. |
| [4.2.8 No pre-consent cookie initialisation](04-transparency-notice.md#req-4-2-8) | Non-essential trackers stay dormant until a consent signal is recorded. |
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | The consent record documents the data subject, purpose, notice version and mechanism. |
| [4.2.7 No forced consent for core functionality](04-transparency-notice.md#req-4-2-7) | Consent is not demanded for non-essential processing as a condition of core functionality, which supports consent that is freely given. |
| [4.2.5 Consent withdrawal](04-transparency-notice.md#req-4-2-5) | Withdrawal is as easy as giving consent and sits in the same context. |
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | A notice before collection gives the information that makes consent informed. |

<a id="gdpr-art-6-4"></a>
#### Art. 6(4) Lawfulness of processing (further processing)

**●●○ Partial**

Processing for a purpose other than the original one needs a compatibility assessment or a separate legal basis.

| APVS requirement | How it helps |
|---|---|
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | A dated compatibility assessment or legal basis entry must exist in the purpose register before any secondary use begins. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | The register of processing purposes gives the place where such a record is checked against actual operations. |

<a id="gdpr-art-7-1"></a>
#### Art. 7(1) Conditions for consent (demonstrating consent)

**●●● Direct**

The controller must be able to demonstrate that the data subject consented.

| APVS requirement | How it helps |
|---|---|
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | Each consent transaction is recorded automatically with identity, time, purpose, notice version and mechanism. |
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Versioned notices make it possible to show exactly what the person saw when consenting. |

<a id="gdpr-art-7-2"></a>
#### Art. 7(2) Conditions for consent (distinguishable request)

**●●● Direct**

A consent request inside a wider declaration must be clearly distinguishable from other matters and written in plain language.

| APVS requirement | How it helps |
|---|---|
| [4.2.4 Consent separable from other matters](04-transparency-notice.md#req-4-2-4) | Consent requests are separated visually and structurally from terms and registration content. |
| [4.2.3 Consent granularity — one purpose per consent act](04-transparency-notice.md#req-4-2-3) | One consent act covers one purpose, so declarations are not bundled. |
| [4.3.3 Consistent privacy settings](04-transparency-notice.md#req-4-3-3) | Consent labels avoid double negatives and show the consequence of each option. |

<a id="gdpr-art-7-3"></a>
#### Art. 7(3) Conditions for consent (withdrawal)

**●●● Direct**

Consent can be withdrawn at any time, as easily as it was given.

| APVS requirement | How it helps |
|---|---|
| [4.2.5 Consent withdrawal](04-transparency-notice.md#req-4-2-5) | Withdrawal takes no more steps than giving consent and is available in the same context. |
| [4.3.4 Privacy settings reflect actual processing state](04-transparency-notice.md#req-4-3-4) | A setting that withdraws consent changes actual processing immediately or within a disclosed period. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | A changed setting must stop or start processing within a disclosed period. |

<a id="gdpr-art-7-4"></a>
#### Art. 7(4) Conditions for consent (freely given)

**●●● Direct**

Consent is not freely given where a service depends on consent to processing that the service does not need.

| APVS requirement | How it helps |
|---|---|
| [4.2.7 No forced consent for core functionality](04-transparency-notice.md#req-4-2-7) | Core functionality must remain usable without consent to non-essential processing. |
| [2.1.5 Optional data not functionally mandatory](02-minimality.md#req-2-1-5) | Optional data cannot be demanded by backend logic for core functions. |
| [4.2.3 Consent granularity — one purpose per consent act](04-transparency-notice.md#req-4-2-3) | Accepting one purpose cannot depend on accepting another. |

<a id="gdpr-art-8"></a>
#### Art. 8 Conditions applicable to child's consent in relation to information society services

**●○○ Supporting**

Where consent applies to online services offered to a child, the child's age must be established and a parent or guardian must authorize consent below the national age threshold.

| APVS requirement | How it helps |
|---|---|
| [2.2.2 Age / date of birth granularity](02-minimality.md#req-2-2-2) | Age checks use a threshold test and discard the date of birth, which lets a service determine the child threshold without keeping birth data. |

<a id="gdpr-art-9"></a>
#### Art. 9 Processing of special categories of personal data

**●○○ Supporting**

Special category data may be processed only under a specific exception, and the application should treat it with extra care.

| APVS requirement | How it helps |
|---|---|
| [3.1.2 Privacy-aware input nudges](03-data-lifecycle-management.md#req-3-1-2) | Users are nudged before they submit unexpected special category data, which reduces accidental collection. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access to special category data is logged with accessor, time and purpose. |
| [2.1.4 Derived data precision](02-minimality.md#req-2-1-4) | Inference of sensitive attributes such as health status is held to the same necessity limits as direct collection. |
| [3.4.2 Share minimal data only](03-data-lifecycle-management.md#req-3-4-2) | Exports carry only the data the purpose requires, which limits the spread of special category data. |

### Data subject rights

<a id="gdpr-art-11"></a>
#### Art. 11 Processing which does not require identification

**●○○ Supporting**

A controller need not keep or gather extra information only to identify people when its purposes do not require identification.

| APVS requirement | How it helps |
|---|---|
| [2.2.3 Identity granularity](02-minimality.md#req-2-2-3) | Identity is held at the least linkable level, down to anonymous where the feature allows. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | The minimum sufficient form includes no personal data at all where a feature can be redesigned to avoid it. |
| [1.3.2 Multiple identifier support](01-architecture-data-mapping.md#req-1-3-2) | The identifier index keeps identifiers only as long as rights fulfilment and documented purposes require. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Identity checks for rights requests are proportionate and do not collect more than needed. |

<a id="gdpr-art-15"></a>
#### Art. 15 Right of access by the data subject

**●●○ Partial**

A data subject can learn whether their data is processed and obtain a copy together with details such as purposes, recipients, retention and source.

| APVS requirement | How it helps |
|---|---|
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index finds all data about a person across every store, which an access response depends on. |
| [1.3.2 Multiple identifier support](01-architecture-data-mapping.md#req-1-3-2) | Multiple identifiers resolve to one subject, so access responses are complete. |
| [3.4.4 Machine-readable export](03-data-lifecycle-management.md#req-3-4-4) | Users can retrieve all their data in a structured, described, machine-readable export (Art. 15(3)). |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Registered users can start an access request from within the application. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools locate, retrieve and export a subject's data without database access. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Identity verification prevents release of data to the wrong person. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Record-level purpose and provenance tags supply the purposes and source details (Art. 15(1)(a), (g)). |
| [4.3.7 Privacy report](04-transparency-notice.md#req-4-3-7) | A personalized privacy report shows what processing is active and what is shared. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logs that capture purpose allow reporting back who used the data and why. |

<a id="gdpr-art-16"></a>
#### Art. 16 Right to rectification

**●●○ Partial**

Inaccurate personal data must be corrected without undue delay.

| APVS requirement | How it helps |
|---|---|
| [3.3.4 Corrected data propagation](03-data-lifecycle-management.md#req-3-3-4) | Corrections propagate to all storage components within a defined and enforced period. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools support rectification of a specific subject's data. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Users can start a rectification request from within the application. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Identity verification protects against changes requested by the wrong person. |

<a id="gdpr-art-17"></a>
#### Art. 17 Right to erasure ('right to be forgotten')

**●●● Direct**

Data must be erased without undue delay when a ground in the article applies, including loss of necessity and withdrawal of consent.

| APVS requirement | How it helps |
|---|---|
| [3.5.2 On Demand Deletion](03-data-lifecycle-management.md#req-3-5-2) | A deletion request triggers the same secure deletion workflow used for retention expiry, with no manual database work. |
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Erasure uses secure deletion, with cryptographic erasure only under documented limits. |
| [3.5.3 Deletion from backups](03-data-lifecycle-management.md#req-3-5-3) | Deletion reaches backups or is filtered on restore. |
| [3.5.4 Deletion from logs](03-data-lifecycle-management.md#req-3-5-4) | Deletion extends to logs. |
| [3.5.5 Deletion of temporary data](03-data-lifecycle-management.md#req-3-5-5) | Deletion extends to caches, temporary files and pipeline output. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Recipients are asked to delete shared data and the outcome is recorded (Art. 17(2)). |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Deletion evidence is kept without retaining the deleted data. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index shows where all of a person's data lives so that nothing is missed. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Users can start an erasure request from within the application. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools execute erasure for a specific subject. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Identity verification applies strongly to erasure because of its impact. |

<a id="gdpr-art-18"></a>
#### Art. 18 Right to restriction of processing

**●●○ Partial**

In the cases listed, processing of a person's data must be limited to storage until the situation is resolved.

| APVS requirement | How it helps |
|---|---|
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools must be able to restrict personal data for a specific subject. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index locates every place the restriction has to apply. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Users can start a restriction request from within the application. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Changes to processing preferences must take effect in actual processing within a disclosed period. |

<a id="gdpr-art-19"></a>
#### Art. 19 Notification obligation regarding rectification or erasure of personal data or restriction of processing

**●●○ Partial**

Recipients of the data must be told about rectification, erasure or restriction, and the data subject can ask who they are.

| APVS requirement | How it helps |
|---|---|
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Deletion requests go to every recipient and the response is recorded. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory identifies the external parties that receive personal data. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Limiting recipients to those required keeps the notification set small and known. |

<a id="gdpr-art-20"></a>
#### Art. 20 Right to data portability

**●●○ Partial**

A data subject can receive the data they provided in a structured, commonly used, machine-readable format and have it transmitted to another controller.

| APVS requirement | How it helps |
|---|---|
| [3.4.4 Machine-readable export](03-data-lifecycle-management.md#req-3-4-4) | Users can export all their data in a non-proprietary machine-readable format with field descriptions. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools can export a subject's data on request. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Users can start the export from within the application. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index makes sure the export covers all components. |

<a id="gdpr-art-21"></a>
#### Art. 21 Right to object

**●●○ Partial**

A data subject can object to certain processing, including direct marketing, and the processing must then stop unless overriding grounds exist.

| APVS requirement | How it helps |
|---|---|
| [5.2.1 Self-service privacy settings modification](05-privacy-features.md#req-5-2-1) | Users can change their privacy settings from within the application, which gives a channel for objecting. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | A setting change must stop the affected processing in the backend within a disclosed period. |
| [4.3.4 Privacy settings reflect actual processing state](04-transparency-notice.md#req-4-3-4) | A setting shown as off means the processing is not occurring. |
| [4.3.6 Privacy dashboard existence](04-transparency-notice.md#req-4-3-6) | A single dashboard lets users view and change processing purposes and communication preferences. |
| [4.3.2 Functional privacy settings](04-transparency-notice.md#req-4-3-2) | Settings must have a real effect on processing. |

### Transparency

<a id="gdpr-art-12"></a>
#### Art. 12 Transparent information, communication and modalities for the exercise of the rights of the data subject

**●●○ Partial**

Information and rights communications must be concise, intelligible and easy to reach, and the controller must facilitate requests and verify requesters proportionately.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Notices must use plain language and be accessible to both people and machines. |
| [4.1.2 Contextual notice per processing activity](04-transparency-notice.md#req-4-1-2) | Notices are given per processing activity, which keeps them concise and relevant. |
| [4.2.4 Consent separable from other matters](04-transparency-notice.md#req-4-2-4) | Consent text is presented separately and in plain language. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Registered users can start rights requests from inside the application. |
| [5.1.4 Service Communication](05-privacy-features.md#req-5-1-4) | The system explains how to use privacy features or request a human process. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Identity verification before fulfilling a request is proportionate to the right and the data. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tools let staff carry out requests without direct database access or custom scripting. |
| [4.3.1 Privacy settings discoverability](04-transparency-notice.md#req-4-3-1) | Privacy settings are reachable through standard menus without contacting support. |

<a id="gdpr-art-13"></a>
#### Art. 13 Information to be provided where personal data are collected from the data subject

**●●○ Partial**

At collection the controller must tell the data subject about purposes, recipients, retention, rights, automated decision-making and any new purpose.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | A notice is presented at or before collection. |
| [4.1.2 Contextual notice per processing activity](04-transparency-notice.md#req-4-1-2) | The information is given for each processing activity. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Categories, purposes, retention and recipients are stated for each activity (Art. 13(1)(c), (e), 13(2)(a)). |
| [4.1.4 Named third-party recipients](04-transparency-notice.md#req-4-1-4) | Recipients are named or described specifically (Art. 13(1)(e)). |
| [4.1.5 Retention period specificity in notice](04-transparency-notice.md#req-4-1-5) | A specific retention period or its criteria is stated (Art. 13(2)(a)). |
| [4.1.8 Automated decision-making disclosure](04-transparency-notice.md#req-4-1-8) | Automated decision-making, its logic and its consequences are disclosed (Art. 13(2)(f)). |
| [4.1.7 Material change notification](04-transparency-notice.md#req-4-1-7) | Data subjects are told before new purposes take effect (Art. 13(3)). |
| [5.1.4 Service Communication](05-privacy-features.md#req-5-1-4) | The system explains how rights can be exercised (Art. 13(2)(b)). |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory gives the factual basis for the recipient disclosures. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Passive third-party collectors and the recipients of data are inventoried, which feeds the recipient disclosure. |

<a id="gdpr-art-14"></a>
#### Art. 14 Information to be provided where personal data have not been obtained from the data subject

**●●○ Partial**

When data comes from another source, the controller must inform the data subject, including the source, within the set time limits.

| APVS requirement | How it helps |
|---|---|
| [4.1.6 Notice for indirectly collected data](04-transparency-notice.md#req-4-1-6) | A notice mechanism with a defined and disclosed maximum delay covers indirectly collected data (Art. 14(3)). |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Provenance tags record whether data was provided, obtained from a third party or inferred, which feeds the source disclosure (Art. 14(2)(f)). |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The inventory of incoming interfaces identifies the flows that trigger a notice. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Categories, purposes, retention and recipients are stated for each activity. |
| [4.1.4 Named third-party recipients](04-transparency-notice.md#req-4-1-4) | Recipients are named or described specifically. |
| [4.1.5 Retention period specificity in notice](04-transparency-notice.md#req-4-1-5) | A specific retention period or its criteria is stated. |
| [4.1.8 Automated decision-making disclosure](04-transparency-notice.md#req-4-1-8) | Automated decision-making is disclosed with its logic and consequences. |
| [4.1.7 Material change notification](04-transparency-notice.md#req-4-1-7) | Changes to purposes or recipients are notified before they take effect (Art. 14(4)). |

### Controller obligations

<a id="gdpr-art-24"></a>
#### Art. 24 Responsibility of the controller

**●○○ Supporting**

The controller must implement appropriate technical and organizational measures and be able to show that processing meets the Regulation.

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The catalog gives a verifiable record of what personal data the system handles. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory shows where data enters and leaves. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | The purpose register with an enforced build check is a technical measure that also serves as evidence. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Deletion logs demonstrate that erasure measures work. |
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | Consent records demonstrate the basis for consent-based processing. |

<a id="gdpr-art-25-1"></a>
#### Art. 25(1) Data protection by design

**●●○ Partial**

Suitable measures, such as pseudonymization and minimization, must be built into the design of processing and applied during it.

| APVS requirement | How it helps |
|---|---|
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | Processing cannot start without a registered purpose, which builds purpose into the design. |
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Necessity is tested for each data element at design time. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Data is collected in its least detailed form. |
| [2.1.6 Abstract and aggregate](02-minimality.md#req-2-1-6) | Aggregation replaces raw data where the purpose allows. |
| [3.1.1 Discard collected data if purpose is met](03-data-lifecycle-management.md#req-3-1-1) | In-flight only handling avoids storing data whose purpose is met. |
| [3.2.3 Processing outcome recorded independently of source data](03-data-lifecycle-management.md#req-3-2-3) | Outcomes are stored apart from the source data, so the sensitive input can be deleted. |
| [3.2.4 Client-side computing](03-data-lifecycle-management.md#req-3-2-4) | On-device processing keeps raw data off the backend. |
| [3.3.5 Pseudonymous references](03-data-lifecycle-management.md#req-3-3-5) | System-generated pseudonymous references replace direct identifiers in keys and URLs. |
| [3.3.6 Pseudonym/identity mapping separation](03-data-lifecycle-management.md#req-3-3-6) | The pseudonym mapping lives in a separate store with its own access controls. |
| [3.3.3 Automated deletion at retention expiry](03-data-lifecycle-management.md#req-3-3-3) | Automated deletion at retention expiry is built into the system. |

<a id="gdpr-art-25-2"></a>
#### Art. 25(2) Data protection by default

**●●● Direct**

By default only the data necessary for each purpose may be processed, in amount, extent, storage period and accessibility.

| APVS requirement | How it helps |
|---|---|
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Only necessary data elements are collected. |
| [2.1.5 Optional data not functionally mandatory](02-minimality.md#req-2-1-5) | Optional data is never needed for core functionality, so the default flow collects the least. |
| [2.2.1 Location data granularity](02-minimality.md#req-2-2-1) | Location is held at the least precise level the feature needs. |
| [4.2.2 No pre-selection or inaction consent](04-transparency-notice.md#req-4-2-2) | Consent controls start off. |
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | Each data class has a defined minimal retention period. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Sharing and audience settings are bounded by the purpose, so data is not exposed to an open-ended audience. |
| [4.3.5 Settings reset notification](04-transparency-notice.md#req-4-3-5) | Settings resets are announced and reviewable before processing resumes under new defaults. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Each necessary element is held in its minimum sufficient form, which limits the amount and extent of data processed. |
| [3.4.2 Share minimal data only](03-data-lifecycle-management.md#req-3-4-2) | Exports and transmissions carry only the data the purpose requires, which limits who can reach it. |
| [3.3.3 Automated deletion at retention expiry](03-data-lifecycle-management.md#req-3-3-3) | Data is deleted automatically when its retention period expires, which limits the period of storage. |

<a id="gdpr-art-28"></a>
#### Art. 28 Processor

**●○○ Supporting**

The controller must use processors that give sufficient guarantees and bind them by contract, including assistance with rights and deletion or return of data at the end of the service.

| APVS requirement | How it helps |
|---|---|
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory identifies the external parties that receive or can reach personal data. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Data goes only to recipients, including processors, that the purpose requires. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Deletion at processors must be completed and confirmed (Art. 28(3)(g)). |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index covers data held by processors, which supports assistance with rights requests (Art. 28(3)(e)). |

<a id="gdpr-art-30"></a>
#### Art. 30 Records of processing activities

**●○○ Supporting**

Controllers and processors must keep records of processing, including purposes, categories of data and subjects, recipients and retention.

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The catalog provides data categories and subject types. |
| [1.2.2 Collection purpose specification](01-architecture-data-mapping.md#req-1-2-2) | Collection purposes are registered for each element. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | Processing purposes are registered for each operation. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The inventory lists recipients and interface directions. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Passive collectors are included, so the record does not miss them. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Record-level metadata supports lineage and subject relationships. |
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | Retention periods per data class supply the envisaged erasure time limits. |

<a id="gdpr-art-35"></a>
#### Art. 35 Data protection impact assessment

**●○○ Supporting**

For high-risk processing the controller must assess the operations, their necessity and proportionality, and the risks and mitigations before processing starts.

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The catalog is a technical description of the data in scope (Art. 35(7)(a)). |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory documents data flows to and from external parties. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | The purpose register describes each processing operation and its purpose. |
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Necessity testing per data element supports the necessity assessment (Art. 35(7)(b)). |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Minimum sufficient form supports the proportionality assessment. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logging is one of the mitigations assessed for sensitive data. |

### Security and breach

<a id="gdpr-art-32"></a>
#### Art. 32 Security of processing

**●○○ Supporting**

Controllers and processors must apply technical and organizational measures matched to the risk, including pseudonymization and encryption.

| APVS requirement | How it helps |
|---|---|
| [3.3.5 Pseudonymous references](03-data-lifecycle-management.md#req-3-3-5) | Keyed or random pseudonymous references implement pseudonymization (Art. 32(1)(a)). |
| [3.3.6 Pseudonym/identity mapping separation](03-data-lifecycle-management.md#req-3-3-6) | Separate storage of the mapping makes pseudonymization protective. |
| [3.3.7 Pseudonymous audit logs](03-data-lifecycle-management.md#req-3-3-7) | Pseudonymous audit logs limit exposure of identities. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logging supports monitoring and review of sensitive data use. |
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Secure deletion, and cryptographic erasure only where encryption was applied in advance, limits residual exposure. |

<a id="gdpr-art-33"></a>
#### Art. 33 Notification of a personal data breach to the supervisory authority

**●○○ Supporting**

A breach must be reported to the supervisory authority within 72 hours, describing the data, subjects and consequences.

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The catalog tells responders which categories of data a compromised store held (Art. 33(3)(a)). |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index helps establish how many subjects and records are affected. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Access logs show what was accessed and by whom. |

<a id="gdpr-art-34"></a>
#### Art. 34 Communication of a personal data breach to the data subject

**●○○ Supporting**

When a breach is likely to create a high risk, the affected people must be told without undue delay.

| APVS requirement | How it helps |
|---|---|
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The identifier index identifies the people whose data sat in the affected stores. |
| [1.3.2 Multiple identifier support](01-architecture-data-mapping.md#req-1-3-2) | Multiple identifiers resolve to one subject, so affected people can be reached. |

### GDPR provisions without an APVS counterpart

| Article | Title | Why |
|---|---|---|
| Art. 6(1)(b) to (f) | Other lawful bases | Choosing and documenting contract, legal obligation, vital interest, public task or legitimate interest is a legal assessment, and APVS requirements address consent only. |
| Art. 22 | Automated individual decision-making, including profiling | APVS requires disclosure of automated decisions (mapped under Art. 13 and 14) but sets no requirement for human intervention, expressing a view or contesting a decision. |
| Art. 26 | Joint controllers | Arrangements between joint controllers are contractual and organizational. |
| Art. 27 | Representatives of controllers or processors not established in the Union | Designation of a representative is a legal and organizational matter. |
| Art. 31 | Cooperation with the supervisory authority | Cooperation is an organizational duty with no application-level counterpart. |
| Art. 33(1) and 33(4) | Breach notification procedure and timing | Assessing, deciding and notifying the authority within 72 hours is an incident response procedure that APVS does not define. |
| Art. 36 | Prior consultation | Consulting the supervisory authority is a procedural step after a DPIA. |
| Art. 37 to 39 | Data protection officer | Organizational role with no application-level counterpart. |
| Art. 40 to 43 | Codes of conduct and certification | These are voluntary governance mechanisms outside application requirements. |
| Art. 44 to 50 | Transfers to third countries or international organisations | Transfer mechanisms such as adequacy and standard clauses are legal arrangements, and APVS has no requirement on transfer location or safeguards. |

---

## A.2 CCPA and CPRA

This mapping lists provisions of the California Consumer Privacy Act as amended by the CPRA (Cal. Civ. Code 1798.100 and following) and the CPPA regulations (Cal. Code Regs. tit. 11, 7000 and following) that an application has to support technically, together with the APVS requirements that help an application meet them. Direct means APVS covers the application-level obligation fairly completely, partial means it covers part of it, and supporting means it yields evidence or building blocks only. APVS is a verification standard, so the mapping is a guide for engineers that reflects the statute and regulations as verified on 2 November 2026. The regulations on risk assessments and cybersecurity audits took effect on 1 January 2026 with phased deadlines running to 2030, and the automated decisionmaking technology requirements apply from 1 January 2027.

### Overview

| Provision | Title | Coverage | APVS requirements |
|---|---|---|---|
| [Cal. Civ. Code § 1798.100(a)(1) and (a)(2)](#ccpa-cal-civ-code-1798-100-a-1-and-a-2) | General Duties of Businesses that Collect Personal Information (notice at collection) | **●●○ Partial** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.2](04-transparency-notice.md#req-4-1-2), [4.1.3](04-transparency-notice.md#req-4-1-3), [4.1.4](04-transparency-notice.md#req-4-1-4), [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.2.2](01-architecture-data-mapping.md#req-1-2-2) |
| [Cal. Code Regs. tit. 11, § 7012](#ccpa-cal-code-regs-tit-11-7012) | Notice at Collection of Personal Information | **●●○ Partial** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.2](04-transparency-notice.md#req-4-1-2), [4.1.3](04-transparency-notice.md#req-4-1-3), [1.4.2](01-architecture-data-mapping.md#req-1-4-2), [1.4.1](01-architecture-data-mapping.md#req-1-4-1) |
| [Cal. Civ. Code § 1798.100(a)(3)](#ccpa-cal-civ-code-1798-100-a-3) | General Duties of Businesses that Collect Personal Information (retention) | **●●● Direct** | [4.1.3](04-transparency-notice.md#req-4-1-3), [4.1.5](04-transparency-notice.md#req-4-1-5), [3.3.1](03-data-lifecycle-management.md#req-3-3-1), [3.3.3](03-data-lifecycle-management.md#req-3-3-3), [3.3.2](03-data-lifecycle-management.md#req-3-3-2), [1.2.3](01-architecture-data-mapping.md#req-1-2-3) |
| [Cal. Code Regs. tit. 11, § 7011](#ccpa-cal-code-regs-tit-11-7011) | Privacy Policy | **●○○ Supporting** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.1.3](04-transparency-notice.md#req-4-1-3), [4.1.7](04-transparency-notice.md#req-4-1-7), [5.1.4](05-privacy-features.md#req-5-1-4) |
| [Cal. Code Regs. tit. 11, § 7003](#ccpa-cal-code-regs-tit-11-7003) | Requirements for Disclosures and Communications to Consumers | **●○○ Supporting** | [4.1.1](04-transparency-notice.md#req-4-1-1), [4.3.1](04-transparency-notice.md#req-4-3-1), [4.3.3](04-transparency-notice.md#req-4-3-3) |
| [Cal. Civ. Code § 1798.100(c)](#ccpa-cal-civ-code-1798-100-c) | General Duties of Businesses that Collect Personal Information (purpose limitation and minimization) | **●●● Direct** | [2.1.1](02-minimality.md#req-2-1-1), [2.1.2](02-minimality.md#req-2-1-2), [2.1.3](02-minimality.md#req-2-1-3), [2.1.4](02-minimality.md#req-2-1-4), [2.1.5](02-minimality.md#req-2-1-5), [2.1.6](02-minimality.md#req-2-1-6), [2.1.7](02-minimality.md#req-2-1-7), [2.2.1](02-minimality.md#req-2-2-1), [3.1.1](03-data-lifecycle-management.md#req-3-1-1), [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [3.4.2](03-data-lifecycle-management.md#req-3-4-2), [2.2.2](02-minimality.md#req-2-2-2), [2.2.3](02-minimality.md#req-2-2-3), [2.2.4](02-minimality.md#req-2-2-4), [2.2.5](02-minimality.md#req-2-2-5), [2.2.6](02-minimality.md#req-2-2-6), [2.2.7](02-minimality.md#req-2-2-7), [3.3.1](03-data-lifecycle-management.md#req-3-3-1) |
| [Cal. Code Regs. tit. 11, § 7002](#ccpa-cal-code-regs-tit-11-7002) | Restrictions on the Collection and Use of Personal Information | **●●○ Partial** | [1.2.2](01-architecture-data-mapping.md#req-1-2-2), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [4.2.3](04-transparency-notice.md#req-4-2-3), [2.1.1](02-minimality.md#req-2-1-1) |
| [Cal. Civ. Code § 1798.105](#ccpa-cal-civ-code-1798-105) | Consumers' Right to Delete Personal Information | **●●● Direct** | [3.5.1](03-data-lifecycle-management.md#req-3-5-1), [3.5.2](03-data-lifecycle-management.md#req-3-5-2), [3.5.3](03-data-lifecycle-management.md#req-3-5-3), [3.5.4](03-data-lifecycle-management.md#req-3-5-4), [3.5.5](03-data-lifecycle-management.md#req-3-5-5), [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [3.5.7](03-data-lifecycle-management.md#req-3-5-7), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [1.3.2](01-architecture-data-mapping.md#req-1-3-2), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Cal. Code Regs. tit. 11, § 7022](#ccpa-cal-code-regs-tit-11-7022) | Requests to Delete | **●●● Direct** | [3.5.1](03-data-lifecycle-management.md#req-3-5-1), [3.5.3](03-data-lifecycle-management.md#req-3-5-3), [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [3.5.7](03-data-lifecycle-management.md#req-3-5-7), [5.1.2](05-privacy-features.md#req-5-1-2), [3.5.2](03-data-lifecycle-management.md#req-3-5-2) |
| [Cal. Civ. Code § 1798.106](#ccpa-cal-civ-code-1798-106) | Consumers' Right to Correct Inaccurate Personal Information | **●●○ Partial** | [3.3.4](03-data-lifecycle-management.md#req-3-3-4), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.2](05-privacy-features.md#req-5-1-2) |
| [Cal. Code Regs. tit. 11, § 7023](#ccpa-cal-code-regs-tit-11-7023) | Requests to Correct | **●○○ Supporting** | [3.3.4](03-data-lifecycle-management.md#req-3-3-4), [1.2.1](01-architecture-data-mapping.md#req-1-2-1) |
| [Cal. Civ. Code § 1798.110](#ccpa-cal-civ-code-1798-110) | Consumers' Right to Know What Personal Information is Being Collected. Right to Access Personal Information | **●●○ Partial** | [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [1.3.2](01-architecture-data-mapping.md#req-1-3-2), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [3.4.4](03-data-lifecycle-management.md#req-3-4-4), [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.2](05-privacy-features.md#req-5-1-2) |
| [Cal. Civ. Code § 1798.115](#ccpa-cal-civ-code-1798-115) | Consumers' Right to Know What Personal Information is Sold or Shared and to Whom | **●○○ Supporting** | [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.2](01-architecture-data-mapping.md#req-1-4-2), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [4.3.7](04-transparency-notice.md#req-4-3-7) |
| [Cal. Code Regs. tit. 11, § 7024](#ccpa-cal-code-regs-tit-11-7024) | Requests to Know | **●●○ Partial** | [3.4.4](03-data-lifecycle-management.md#req-3-4-4), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [5.1.2](05-privacy-features.md#req-5-1-2) |
| [Cal. Civ. Code § 1798.120](#ccpa-cal-civ-code-1798-120) | Consumers' Right to Opt Out of Sale or Sharing of Personal Information | **●●○ Partial** | [5.2.1](05-privacy-features.md#req-5-2-1), [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.2](04-transparency-notice.md#req-4-3-2), [4.3.4](04-transparency-notice.md#req-4-3-4), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [1.4.2](01-architecture-data-mapping.md#req-1-4-2) |
| [Cal. Civ. Code § 1798.135(a)](#ccpa-cal-civ-code-1798-135-a) | Methods of Limiting Sale, Sharing, and Use of Personal Information and Use of Sensitive Personal Information (opt-out and limit links) | **●○○ Supporting** | [4.3.1](04-transparency-notice.md#req-4-3-1), [4.3.6](04-transparency-notice.md#req-4-3-6), [5.1.4](05-privacy-features.md#req-5-1-4) |
| [Cal. Code Regs. tit. 11, § 7025](#ccpa-cal-code-regs-tit-11-7025) | Opt-out Preference Signals | **●○○ Supporting** | [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.4](04-transparency-notice.md#req-4-3-4), [4.3.3](04-transparency-notice.md#req-4-3-3) |
| [Cal. Code Regs. tit. 11, § 7026](#ccpa-cal-code-regs-tit-11-7026) | Requests to Opt-out of Sale/Sharing | **●●○ Partial** | [5.2.1](05-privacy-features.md#req-5-2-1), [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.2](04-transparency-notice.md#req-4-3-2), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [3.5.6](03-data-lifecycle-management.md#req-3-5-6) |
| [Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027](#ccpa-cal-civ-code-1798-121-and-cal-code-regs-tit-11-7027) | Consumers' Right to Limit Use and Disclosure of Sensitive Personal Information; Requests to Limit Use and Disclosure of Sensitive Personal Information | **●○○ Supporting** | [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [5.2.1](05-privacy-features.md#req-5-2-1), [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.4](04-transparency-notice.md#req-4-3-4), [3.4.3](03-data-lifecycle-management.md#req-3-4-3) |
| [Cal. Code Regs. tit. 11, § 7028](#ccpa-cal-code-regs-tit-11-7028) | Requests to Opt-in After Opting-out of the Sale or Sharing of Personal Information or Limiting the Use and Disclosure of Sensitive Personal Information | **●●○ Partial** | [4.2.10](04-transparency-notice.md#req-4-2-10), [4.2.6](04-transparency-notice.md#req-4-2-6), [4.2.2](04-transparency-notice.md#req-4-2-2) |
| [Cal. Civ. Code § 1798.125 and Cal. Code Regs. tit. 11, § 7080](#ccpa-cal-civ-code-1798-125-and-cal-code-regs-tit-11-7080) | Consumers' Right of No Retaliation Following Opt Out or Exercise of Other Rights; Discriminatory Practices | **●●○ Partial** | [4.2.7](04-transparency-notice.md#req-4-2-7), [2.1.5](02-minimality.md#req-2-1-5), [4.2.9](04-transparency-notice.md#req-4-2-9) |
| [Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020](#ccpa-cal-civ-code-1798-130-a-1-and-cal-code-regs-tit-11-7020) | Notice, Disclosure, Correction, and Deletion Requirements; Methods for Submitting Requests to Delete, Requests to Correct, and Requests to Know | **●●○ Partial** | [5.1.1](05-privacy-features.md#req-5-1-1), [5.1.4](05-privacy-features.md#req-5-1-4), [4.3.1](04-transparency-notice.md#req-4-3-1), [4.3.6](04-transparency-notice.md#req-4-3-6), [5.1.2](05-privacy-features.md#req-5-1-2) |
| [Cal. Code Regs. tit. 11, § 7021](#ccpa-cal-code-regs-tit-11-7021) | Timelines for Responding to Requests to Delete, Requests to Correct, Requests to Know, Requests to Access ADMT, and Requests to Appeal ADMT | **●○○ Supporting** | [5.1.2](05-privacy-features.md#req-5-1-2), [3.5.2](03-data-lifecycle-management.md#req-3-5-2), [3.5.7](03-data-lifecycle-management.md#req-3-5-7) |
| [Cal. Code Regs. tit. 11, § 7060](#ccpa-cal-code-regs-tit-11-7060) | General Rules Regarding Verification | **●●○ Partial** | [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Cal. Code Regs. tit. 11, § 7063](#ccpa-cal-code-regs-tit-11-7063) | Authorized Agents | **●○○ Supporting** | [5.1.3](05-privacy-features.md#req-5-1-3) |
| [Cal. Code Regs. tit. 11, § 7004](#ccpa-cal-code-regs-tit-11-7004) | Requirements for Methods for Submitting CCPA Requests and Obtaining Consumer Consent | **●●● Direct** | [4.2.1](04-transparency-notice.md#req-4-2-1), [4.2.2](04-transparency-notice.md#req-4-2-2), [4.2.3](04-transparency-notice.md#req-4-2-3), [4.2.4](04-transparency-notice.md#req-4-2-4), [4.2.5](04-transparency-notice.md#req-4-2-5), [4.2.7](04-transparency-notice.md#req-4-2-7), [4.2.9](04-transparency-notice.md#req-4-2-9), [4.2.10](04-transparency-notice.md#req-4-2-10), [4.3.3](04-transparency-notice.md#req-4-3-3), [4.3.1](04-transparency-notice.md#req-4-3-1) |
| [Cal. Code Regs. tit. 11, § 7101](#ccpa-cal-code-regs-tit-11-7101) | Record-Keeping | **●○○ Supporting** | [4.2.6](04-transparency-notice.md#req-4-2-6), [3.5.7](03-data-lifecycle-management.md#req-3-5-7) |
| [Cal. Civ. Code § 1798.100(d)](#ccpa-cal-civ-code-1798-100-d) | General Duties of Businesses that Collect Personal Information (contracts with third parties, service providers and contractors) | **●○○ Supporting** | [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.2](01-architecture-data-mapping.md#req-1-4-2), [3.4.1](03-data-lifecycle-management.md#req-3-4-1), [3.4.2](03-data-lifecycle-management.md#req-3-4-2) |
| [Cal. Code Regs. tit. 11, § 7050](#ccpa-cal-code-regs-tit-11-7050) | Service Providers and Contractors | **●○○ Supporting** | [3.2.5](03-data-lifecycle-management.md#req-3-2-5), [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [3.4.1](03-data-lifecycle-management.md#req-3-4-1) |
| [Cal. Code Regs. tit. 11, § 7052](#ccpa-cal-code-regs-tit-11-7052) | Third Parties | **●○○ Supporting** | [3.5.6](03-data-lifecycle-management.md#req-3-5-6), [1.4.1](01-architecture-data-mapping.md#req-1-4-1) |
| [Cal. Code Regs. tit. 11, § 7152](#ccpa-cal-code-regs-tit-11-7152) | Risk Assessment Requirements | **●○○ Supporting** | [1.1.1](01-architecture-data-mapping.md#req-1-1-1), [1.2.1](01-architecture-data-mapping.md#req-1-2-1), [1.4.1](01-architecture-data-mapping.md#req-1-4-1), [1.4.3](01-architecture-data-mapping.md#req-1-4-3), [2.1.2](02-minimality.md#req-2-1-2), [3.3.1](03-data-lifecycle-management.md#req-3-3-1), [4.1.8](04-transparency-notice.md#req-4-1-8) |
| [Cal. Code Regs. tit. 11, § 7220](#ccpa-cal-code-regs-tit-11-7220) | Pre-use Notice Requirements | **●○○ Supporting** | [4.1.8](04-transparency-notice.md#req-4-1-8) |
| [Cal. Code Regs. tit. 11, § 7221](#ccpa-cal-code-regs-tit-11-7221) | Requests to Opt-Out of ADMT | **●○○ Supporting** | [5.2.1](05-privacy-features.md#req-5-2-1), [5.2.2](05-privacy-features.md#req-5-2-2), [4.3.2](04-transparency-notice.md#req-4-3-2) |
| [Cal. Code Regs. tit. 11, § 7222](#ccpa-cal-code-regs-tit-11-7222) | Requests to Access ADMT | **●○○ Supporting** | [4.1.8](04-transparency-notice.md#req-4-1-8), [1.3.1](01-architecture-data-mapping.md#req-1-3-1), [5.1.1](05-privacy-features.md#req-5-1-1) |

### Notice and transparency

<a id="ccpa-cal-civ-code-1798-100-a-1-and-a-2"></a>
#### Cal. Civ. Code § 1798.100(a)(1) and (a)(2) General Duties of Businesses that Collect Personal Information (notice at collection)

**●●○ Partial**

Tell consumers, at or before the point of collection, which categories of personal information and sensitive personal information are collected, the purposes for which they are collected or used, and whether they are sold or shared.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Requires a notice at or before collection that is readable by people and accessible to machines, with every version recorded. |
| [4.1.2 Contextual notice per processing activity](04-transparency-notice.md#req-4-1-2) | Requires the notice to be given for each processing activity, which fits collection points that serve different purposes. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Requires the notice to state the data categories, the specific purpose, the retention period and whether recipients receive the data. |
| [4.1.4 Named third-party recipients](04-transparency-notice.md#req-4-1-4) | Asks for named recipients or specific recipient categories, which supports the disclosure of who receives sold or shared data. |
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The in-system catalog of data elements and purposes supplies the facts a notice has to state. |
| [1.2.2 Collection purpose specification](01-architecture-data-mapping.md#req-1-2-2) | A specific collection purpose recorded before collection gives the notice its purpose statement. |

<a id="ccpa-cal-code-regs-tit-11-7012"></a>
#### Cal. Code Regs. tit. 11, § 7012 Notice at Collection of Personal Information

**●●○ Partial**

Present the notice at collection in a way consumers can see before data is collected, including on each collection channel, and make sure third parties that collect data through the business's site or app are covered.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Requires the notice to precede collection and to be versioned. |
| [4.1.2 Contextual notice per processing activity](04-transparency-notice.md#req-4-1-2) | Requires a contextual notice at each collection point rather than a single global policy. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Defines the minimum content of the notice per processing activity. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Inventories analytics SDKs, pixels and similar components that collect data without explicit invocation, which are the third-party collectors the notice has to account for. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | Keeps a machine-readable inventory of external interfaces that can be checked against what the notice discloses. |

<a id="ccpa-cal-civ-code-1798-100-a-3"></a>
#### Cal. Civ. Code § 1798.100(a)(3) General Duties of Businesses that Collect Personal Information (retention)

**●●● Direct**

Disclose how long each category of personal information is kept, or the criteria used to set that period, and do not keep it longer than reasonably necessary for the disclosed purpose.

| APVS requirement | How it helps |
|---|---|
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Requires the notice to state the retention period or criteria for each processing activity. |
| [4.1.5 Retention period specificity in notice](04-transparency-notice.md#req-4-1-5) | Requires a specific period per data category and purpose and rules out a generic as long as necessary statement. |
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | Defines a retention period or criteria for every data element or class, which is the source for the disclosure. |
| [3.3.3 Automated deletion at retention expiry](03-data-lifecycle-management.md#req-3-3-3) | Deletes data automatically when its retention period expires. |
| [3.3.2 Residual retention window for temporary data](03-data-lifecycle-management.md#req-3-3-2) | Bounds the time temporary copies can persist when immediate deletion is not feasible. |
| [1.2.3 Last collection timestamp](01-architecture-data-mapping.md#req-1-2-3) | Records when data was last collected, which is the reference point for enforcing retention. |

<a id="ccpa-cal-code-regs-tit-11-7011"></a>
#### Cal. Code Regs. tit. 11, § 7011 Privacy Policy

**●○○ Supporting**

Publish a comprehensive privacy policy that describes data practices and consumer rights, explains how to exercise them, and is kept current.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Requires a versioned notice with a recorded history of changes. |
| [4.1.3 Notice content — required fields](04-transparency-notice.md#req-4-1-3) | Supplies categories, purposes, retention and sharing statements for the policy text. |
| [4.1.7 Material change notification](04-transparency-notice.md#req-4-1-7) | Requires affected people to be told of material changes before they take effect. |
| [5.1.4 Service Communication](05-privacy-features.md#req-5-1-4) | Requires a clear explanation of how individuals can use privacy features or reach a human process. |

<a id="ccpa-cal-code-regs-tit-11-7003"></a>
#### Cal. Code Regs. tit. 11, § 7003 Requirements for Disclosures and Communications to Consumers

**●○○ Supporting**

Make required disclosures easy to read and understand, in plain language, and accessible to the consumers addressed.

| APVS requirement | How it helps |
|---|---|
| [4.1.1 Privacy notice at collection](04-transparency-notice.md#req-4-1-1) | Requires the notice to use plain language about what is collected, how it is used and how it is protected. |
| [4.3.1 Privacy settings discoverability](04-transparency-notice.md#req-4-3-1) | Requires privacy controls to meet WCAG AA contrast and to sit within normal reading flow. |
| [4.3.3 Consistent privacy settings](04-transparency-notice.md#req-4-3-3) | Requires consistent labels and unambiguous wording for privacy choices. |

### Purpose and minimization

<a id="ccpa-cal-civ-code-1798-100-c"></a>
#### Cal. Civ. Code § 1798.100(c) General Duties of Businesses that Collect Personal Information (purpose limitation and minimization)

**●●● Direct**

Keep collection, use, retention and sharing reasonably necessary and proportionate to the purposes for which the information was collected.

| APVS requirement | How it helps |
|---|---|
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Limits collection to elements that are necessary for the documented purpose. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Requires the least data, coarsest granularity and narrowest volume and frequency that still serve the purpose. |
| [2.1.3 Necessity reassessment on change or retirement](02-minimality.md#req-2-1-3) | Requires necessity to be reassessed when a processing activity changes or ends. |
| [2.1.4 Derived data precision](02-minimality.md#req-2-1-4) | Applies the same limits to inferred and derived data. |
| [2.1.5 Optional data not functionally mandatory](02-minimality.md#req-2-1-5) | Requires core functionality to work without optional data. |
| [2.1.6 Abstract and aggregate](02-minimality.md#req-2-1-6) | Prefers aggregated or de-identified output and discards the raw data. |
| [2.1.7 Granularity degradation over time](02-minimality.md#req-2-1-7) | Reduces granularity of longitudinal data as it ages. |
| [2.2.1 Location data granularity](02-minimality.md#req-2-2-1) | Sets a least-precise-level rule for location data. |
| [3.1.1 Discard collected data if purpose is met](03-data-lifecycle-management.md#req-3-1-1) | Keeps data that is used only during collection in memory and out of storage. |
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | Checks processing against the collection purpose and the data timeframe the purpose needs. |
| [3.4.2 Share minimal data only](03-data-lifecycle-management.md#req-3-4-2) | Limits each export or transmission to the data the purpose of the exchange requires. |
| [2.2.2 Age / date of birth granularity](02-minimality.md#req-2-2-2) | Age data is held at the least precise level the feature needs. |
| [2.2.3 Identity granularity](02-minimality.md#req-2-2-3) | Identity data is held at the least linkable level the feature allows. |
| [2.2.4 Photo metadata](02-minimality.md#req-2-2-4) | Photo metadata is limited to the documented level. |
| [2.2.5 File metadata](02-minimality.md#req-2-2-5) | File metadata is limited to what the feature needs. |
| [2.2.6 Communication, call and message history](02-minimality.md#req-2-2-6) | Communication history is kept at the least detailed level that works. |
| [2.2.7 Live streaming data](02-minimality.md#req-2-2-7) | Live stream data is limited to the lowest fidelity that works. |
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | A retention period is defined for each data class, so data is kept only as long as reasonably necessary. |

<a id="ccpa-cal-code-regs-tit-11-7002"></a>
#### Cal. Code Regs. tit. 11, § 7002 Restrictions on the Collection and Use of Personal Information

**●●○ Partial**

Collect and use personal information only for purposes consistent with consumers' reasonable expectations, and obtain consent before using it for an unrelated or incompatible purpose.

| APVS requirement | How it helps |
|---|---|
| [1.2.2 Collection purpose specification](01-architecture-data-mapping.md#req-1-2-2) | Requires a specific collection purpose to be recorded before collection and blocks collection without one. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | Requires a registered purpose for each processing operation before it runs. |
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | Blocks or flags use outside the collection purpose and requires a dated compatibility assessment or legal basis for secondary use. |
| [4.2.3 Consent granularity — one purpose per consent act](04-transparency-notice.md#req-4-2-3) | Requires separate consent for each distinct purpose, which fits the consent needed for an unrelated purpose. |
| [2.1.1 Necessity of each data element](02-minimality.md#req-2-1-1) | Keeps collected elements tied to what the documented purpose needs. |

### Consumer rights

<a id="ccpa-cal-civ-code-1798-105"></a>
#### Cal. Civ. Code § 1798.105 Consumers' Right to Delete Personal Information

**●●● Direct**

On a verified request, delete the consumer's personal information from the business's records and direct service providers, contractors and relevant third parties to do the same.

| APVS requirement | How it helps |
|---|---|
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Makes secure deletion the default method for data under a deletion obligation. |
| [3.5.2 On Demand Deletion](03-data-lifecycle-management.md#req-3-5-2) | Provides one deletion pathway that a request can trigger without manual database work. |
| [3.5.3 Deletion from backups](03-data-lifecycle-management.md#req-3-5-3) | Extends deletion to backups, or filters deleted data out on restoration. |
| [3.5.4 Deletion from logs](03-data-lifecycle-management.md#req-3-5-4) | Extends deletion to logs that contain personal data. |
| [3.5.5 Deletion of temporary data](03-data-lifecycle-management.md#req-3-5-5) | Extends deletion to caches, temporary files and intermediate outputs. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Sends deletion requests to every recipient of the data and records the outcome. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Produces deletion evidence without keeping the deleted content. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The subject index makes it possible to find all data held about the requester. |
| [1.3.2 Multiple identifier support](01-architecture-data-mapping.md#req-1-3-2) | Resolves every known identifier of a person to the same record set. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Lets a registered user start a request from inside the application. |
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | A request is fulfilled only after proportionate identity verification. |

<a id="ccpa-cal-code-regs-tit-11-7022"></a>
#### Cal. Code Regs. tit. 11, § 7022 Requests to Delete

**●●● Direct**

Carry out deletion by erasing or de-identifying the data, tell service providers, contractors and third parties to delete it, and keep a record of the request.

| APVS requirement | How it helps |
|---|---|
| [3.5.1 Secure deletion as default](03-data-lifecycle-management.md#req-3-5-1) | Defines how erasure is performed, including the narrow conditions for cryptographic erasure. |
| [3.5.3 Deletion from backups](03-data-lifecycle-management.md#req-3-5-3) | Covers archived and backup systems through deletion or restoration filtering. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Covers notifying recipients and recording what they answer. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Provides an audit trail that deletion occurred without retaining the data. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Gives authorized staff an administrative function to execute erasure without direct database access. |
| [3.5.2 On Demand Deletion](03-data-lifecycle-management.md#req-3-5-2) | Provides an on-demand deletion mechanism that a data subject or authorized personnel can trigger. |

<a id="ccpa-cal-civ-code-1798-106"></a>
#### Cal. Civ. Code § 1798.106 Consumers' Right to Correct Inaccurate Personal Information

**●●○ Partial**

On a verified request, correct inaccurate personal information and have the correction reach the places where the data is held.

| APVS requirement | How it helps |
|---|---|
| [3.3.4 Corrected data propagation](03-data-lifecycle-management.md#req-3-3-4) | Requires a corrected value to propagate to replicas, caches and search indexes within an enforced period. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | Locates every copy of the data that needs the correction. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Lets a user start the request in the application. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Administrative tooling lets staff locate and act on the data of a specific person, and its verification step covers rectification requests. |

<a id="ccpa-cal-code-regs-tit-11-7023"></a>
#### Cal. Code Regs. tit. 11, § 7023 Requests to Correct

**●○○ Supporting**

Assess the accuracy of the disputed data using the information supplied, make the correction in the business's systems, and tell the consumer the outcome.

| APVS requirement | How it helps |
|---|---|
| [3.3.4 Corrected data propagation](03-data-lifecycle-management.md#req-3-3-4) | Ensures an accepted correction reaches every storage component. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Provenance and lineage tags help decide whether the disputed value is reliable. |

<a id="ccpa-cal-civ-code-1798-110"></a>
#### Cal. Civ. Code § 1798.110 Consumers' Right to Know What Personal Information is Being Collected. Right to Access Personal Information

**●●○ Partial**

On a verified request, disclose the categories and specific pieces of personal information collected, the sources, the purposes, and the categories of third parties it was disclosed to.

| APVS requirement | How it helps |
|---|---|
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | Retrieves everything attributable to one person across storage components. |
| [1.3.2 Multiple identifier support](01-architecture-data-mapping.md#req-1-3-2) | Handles several identifiers for the same person. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Record-level tags for purpose and provenance supply the sources and purposes to report. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory identifies the external parties that receive data. |
| [3.4.4 Machine-readable export](03-data-lifecycle-management.md#req-3-4-4) | Exports a person's data in a structured, machine-readable format. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Lets a user initiate an access request in the application. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Lets administrators locate and retrieve a person's data without custom scripting. |

<a id="ccpa-cal-civ-code-1798-115"></a>
#### Cal. Civ. Code § 1798.115 Consumers' Right to Know What Personal Information is Sold or Shared and to Whom

**●○○ Supporting**

On request, disclose the categories of personal information sold or shared about the consumer and the categories of parties that received each.

| APVS requirement | How it helps |
|---|---|
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | Records the external party, data categories and purpose of every outbound interface, which is the raw material for the answer. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Records passive collectors that receive data without explicit application calls. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Limits sharing to required recipients, which keeps the disclosure list short and accurate. |
| [4.3.7 Privacy report](04-transparency-notice.md#req-4-3-7) | A privacy report shows individuals what is shared with whom under their current settings. |

<a id="ccpa-cal-code-regs-tit-11-7024"></a>
#### Cal. Code Regs. tit. 11, § 7024 Requests to Know

**●●○ Partial**

Return the specific pieces of personal information and the required category disclosures, in a usable format, and look back beyond twelve months where the data exists.

| APVS requirement | How it helps |
|---|---|
| [3.4.4 Machine-readable export](03-data-lifecycle-management.md#req-3-4-4) | Requires a structured export with described fields that can be read without access to the system. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The index makes it possible to enumerate data in logs, caches and derived stores as well as primary databases. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Gives administrators a way to retrieve and export a person's data. |

### Opt-out and limiting

<a id="ccpa-cal-civ-code-1798-120"></a>
#### Cal. Civ. Code § 1798.120 Consumers' Right to Opt Out of Sale or Sharing of Personal Information

**●●○ Partial**

Let consumers direct a business at any time to stop selling or sharing their personal information, and make that choice take effect in processing.

| APVS requirement | How it helps |
|---|---|
| [5.2.1 Self-service privacy settings modification](05-privacy-features.md#req-5-2-1) | Lets users change their privacy settings from inside the application. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Requires a setting change to take effect on processing immediately or within a disclosed maximum period. |
| [4.3.2 Functional privacy settings](04-transparency-notice.md#req-4-3-2) | Requires privacy settings to have a real effect on processing. |
| [4.3.4 Privacy settings reflect actual processing state](04-transparency-notice.md#req-4-3-4) | Requires displayed settings to match actual processing state. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Limits recipients to those the purpose requires, which bounds the set affected by a sharing opt-out. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Finds the advertising and analytics components that share data. |

<a id="ccpa-cal-civ-code-1798-135-a"></a>
#### Cal. Civ. Code § 1798.135(a) Methods of Limiting Sale, Sharing, and Use of Personal Information and Use of Sensitive Personal Information (opt-out and limit links)

**●○○ Supporting**

Provide clear and conspicuous links, or an alternative opt-out link, that lead to the opt-out of sale or sharing and the limit on sensitive personal information use (see also Cal. Code Regs. tit. 11, 7013, 7014 and 7015).

| APVS requirement | How it helps |
|---|---|
| [4.3.1 Privacy settings discoverability](04-transparency-notice.md#req-4-3-1) | Requires privacy controls to be reachable within two steps from the standard menus and not visually de-emphasized. |
| [4.3.6 Privacy dashboard existence](04-transparency-notice.md#req-4-3-6) | Provides a single dashboard where such choices can sit. |
| [5.1.4 Service Communication](05-privacy-features.md#req-5-1-4) | Requires a clear description of how people reach these features. |

<a id="ccpa-cal-code-regs-tit-11-7025"></a>
#### Cal. Code Regs. tit. 11, § 7025 Opt-out Preference Signals

**●○○ Supporting**

Treat a browser or device opt-out preference signal such as Global Privacy Control as a valid request to opt out of sale and sharing, and show that the signal was honored.

| APVS requirement | How it helps |
|---|---|
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Covers applying a changed choice to processing, though no APVS requirement addresses detecting the signal itself. |
| [4.3.4 Privacy settings reflect actual processing state](04-transparency-notice.md#req-4-3-4) | Requires the stated privacy state to match the processing that actually occurs. |
| [4.3.3 Consistent privacy settings](04-transparency-notice.md#req-4-3-3) | Requires a choice to operate identically in every context where the processing occurs. |

<a id="ccpa-cal-code-regs-tit-11-7026"></a>
#### Cal. Code Regs. tit. 11, § 7026 Requests to Opt-out of Sale/Sharing

**●●○ Partial**

Offer an opt-out method as easy as other request methods, act on it without delay, and pass the request to the third parties the data was made available to.

| APVS requirement | How it helps |
|---|---|
| [5.2.1 Self-service privacy settings modification](05-privacy-features.md#req-5-2-1) | Provides self-service modification of settings without support contact. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Applies the change to processing within a disclosed period. |
| [4.3.2 Functional privacy settings](04-transparency-notice.md#req-4-3-2) | Confirms the control stops the corresponding processing. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Limits recipients, which gives a defined set of parties to notify. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Provides a model for sending a request to recipients and recording their response. |

<a id="ccpa-cal-civ-code-1798-121-and-cal-code-regs-tit-11-7027"></a>
#### Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027 Consumers' Right to Limit Use and Disclosure of Sensitive Personal Information; Requests to Limit Use and Disclosure of Sensitive Personal Information

**●○○ Supporting**

Let consumers limit the use of their sensitive personal information to what is necessary to provide the requested goods or services, and apply that limit across the business's processing.

| APVS requirement | How it helps |
|---|---|
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | Enforces purpose checks at the point of use, which is where a limit on sensitive data use takes effect. |
| [5.2.1 Self-service privacy settings modification](05-privacy-features.md#req-5-2-1) | Lets users set the limit from inside the application. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Makes the limit take effect on processing within a disclosed period. |
| [4.3.4 Privacy settings reflect actual processing state](04-transparency-notice.md#req-4-3-4) | Keeps the displayed setting aligned with what processing does. |
| [3.4.3 Application-level data access tracking](03-data-lifecycle-management.md#req-3-4-3) | Logs each access to sensitive data with its purpose, which supports checking compliance with a limit. |

<a id="ccpa-cal-code-regs-tit-11-7028"></a>
#### Cal. Code Regs. tit. 11, § 7028 Requests to Opt-in After Opting-out of the Sale or Sharing of Personal Information or Limiting the Use and Disclosure of Sensitive Personal Information

**●●○ Partial**

Accept an opt-in after an opt-out only through a clear process, and do not repeatedly prompt a consumer who has opted out.

| APVS requirement | How it helps |
|---|---|
| [4.2.10 No nagging](04-transparency-notice.md#req-4-2-10) | Prohibits re-prompting for a purpose the person has already declined unless the processing materially changed. |
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | Records each consent transaction with timestamp, purpose and notice version. |
| [4.2.2 No pre-selection or inaction consent](04-transparency-notice.md#req-4-2-2) | Requires consent to be an explicit action and never a default. |

<a id="ccpa-cal-civ-code-1798-125-and-cal-code-regs-tit-11-7080"></a>
#### Cal. Civ. Code § 1798.125 and Cal. Code Regs. tit. 11, § 7080 Consumers' Right of No Retaliation Following Opt Out or Exercise of Other Rights; Discriminatory Practices

**●●○ Partial**

Do not deny service, change prices or degrade quality because a consumer exercised a privacy right.

| APVS requirement | How it helps |
|---|---|
| [4.2.7 No forced consent for core functionality](04-transparency-notice.md#req-4-2-7) | Prohibits conditioning core functionality on consent to non-essential processing. |
| [2.1.5 Optional data not functionally mandatory](02-minimality.md#req-2-1-5) | Requires core functionality to work when optional data is withheld. |
| [4.2.9 Representative Framing of Privacy Choices](04-transparency-notice.md#req-4-2-9) | Prohibits false necessity and pressure framing around privacy choices. |

### Requests and consent

<a id="ccpa-cal-civ-code-1798-130-a-1-and-cal-code-regs-tit-11-7020"></a>
#### Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020 Notice, Disclosure, Correction, and Deletion Requirements; Methods for Submitting Requests to Delete, Requests to Correct, and Requests to Know

**●●○ Partial**

Offer designated methods for submitting requests, including an online method where the business operates online, and make them easy to find and use.

| APVS requirement | How it helps |
|---|---|
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Requires in-application self-service initiation reachable within two navigation steps. |
| [5.1.4 Service Communication](05-privacy-features.md#req-5-1-4) | Requires the system to explain how to use these features or ask for a human process. |
| [4.3.1 Privacy settings discoverability](04-transparency-notice.md#req-4-3-1) | Makes privacy controls discoverable from standard menus. |
| [4.3.6 Privacy dashboard existence](04-transparency-notice.md#req-4-3-6) | Gives one dashboard for viewing and changing privacy settings. |
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Lets staff execute requests that arrive through other channels. |

<a id="ccpa-cal-code-regs-tit-11-7021"></a>
#### Cal. Code Regs. tit. 11, § 7021 Timelines for Responding to Requests to Delete, Requests to Correct, Requests to Know, Requests to Access ADMT, and Requests to Appeal ADMT

**●○○ Supporting**

Confirm receipt of a request within ten business days and respond within forty-five calendar days, with a limited extension when notice is given.

| APVS requirement | How it helps |
|---|---|
| [5.1.2 Admin execution capability](05-privacy-features.md#req-5-1-2) | Gives administrators the tooling to carry out a request without direct database access or custom scripting. |
| [3.5.2 On Demand Deletion](03-data-lifecycle-management.md#req-3-5-2) | Requires any delay between a deletion request and deletion to be defined and enforced by the system. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Produces evidence of when deletion took place. |

<a id="ccpa-cal-code-regs-tit-11-7060"></a>
#### Cal. Code Regs. tit. 11, § 7060 General Rules Regarding Verification

**●●○ Partial**

Verify that the person making a request to delete, correct or know is the consumer concerned, using a method proportionate to the risk, and delete verification data once it is no longer needed (see also 7061 and 7062).

| APVS requirement | How it helps |
|---|---|
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Requires proportionate identity verification before fulfilling a request, and per its guidance removal of identity data afterwards. |

<a id="ccpa-cal-code-regs-tit-11-7063"></a>
#### Cal. Code Regs. tit. 11, § 7063 Authorized Agents

**●○○ Supporting**

Accept requests from an agent the consumer has authorized, after verifying the agent's authority.

| APVS requirement | How it helps |
|---|---|
| [5.1.3 Identity verification](05-privacy-features.md#req-5-1-3) | Calls for provisions for delegated requests and confirmation of the authority behind them. |

<a id="ccpa-cal-code-regs-tit-11-7004"></a>
#### Cal. Code Regs. tit. 11, § 7004 Requirements for Methods for Submitting CCPA Requests and Obtaining Consumer Consent

**●●● Direct**

Design request and consent interfaces in plain language, with symmetry in choice, no confusing wording and no choice architecture that impairs a free, specific, informed and unambiguous choice, so that consent obtained through dark patterns is not valid.

| APVS requirement | How it helps |
|---|---|
| [4.2.1 Visual parity of privacy choices](04-transparency-notice.md#req-4-2-1) | Requires equal prominence and no more steps to accept than to reject. |
| [4.2.2 No pre-selection or inaction consent](04-transparency-notice.md#req-4-2-2) | Prohibits pre-selected and inferred consent. |
| [4.2.3 Consent granularity — one purpose per consent act](04-transparency-notice.md#req-4-2-3) | Requires separate consent per purpose and a second layer that is as easy to reach as the summary choice. |
| [4.2.4 Consent separable from other matters](04-transparency-notice.md#req-4-2-4) | Requires consent to be separated from terms and other declarations. |
| [4.2.5 Consent withdrawal](04-transparency-notice.md#req-4-2-5) | Requires withdrawal to be as easy as giving consent. |
| [4.2.7 No forced consent for core functionality](04-transparency-notice.md#req-4-2-7) | Prohibits bundling non-essential consent with access to core functionality. |
| [4.2.9 Representative Framing of Privacy Choices](04-transparency-notice.md#req-4-2-9) | Prohibits confirmshaming, false necessity and fabricated urgency. |
| [4.2.10 No nagging](04-transparency-notice.md#req-4-2-10) | Prohibits repeated prompts after a decline. |
| [4.3.3 Consistent privacy settings](04-transparency-notice.md#req-4-3-3) | Prohibits double negatives and ambiguous labels in privacy settings. |
| [4.3.1 Privacy settings discoverability](04-transparency-notice.md#req-4-3-1) | Keeps privacy controls easy to locate and legible. |

<a id="ccpa-cal-code-regs-tit-11-7101"></a>
#### Cal. Code Regs. tit. 11, § 7101 Record-Keeping

**●○○ Supporting**

Keep records of consumer requests and how the business responded for the required period.

| APVS requirement | How it helps |
|---|---|
| [4.2.6 Consent record](04-transparency-notice.md#req-4-2-6) | Records each consent transaction with the data subject, time, purpose, notice version and mechanism. |
| [3.5.7 Deletion evidence](03-data-lifecycle-management.md#req-3-5-7) | Provides a deletion log that proves the outcome without storing the deleted data. |

### Service providers and third parties

<a id="ccpa-cal-civ-code-1798-100-d"></a>
#### Cal. Civ. Code § 1798.100(d) General Duties of Businesses that Collect Personal Information (contracts with third parties, service providers and contractors)

**●○○ Supporting**

Bind each third party, service provider and contractor by contract to limited and specified purposes, so the business needs to know who receives data and why.

| APVS requirement | How it helps |
|---|---|
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | Records the external party, data categories and purpose for each interface, which is the information the contract has to match. |
| [1.4.2 Passive and third-party collection](01-architecture-data-mapping.md#req-1-4-2) | Finds passive collectors that would otherwise lack a contract and a stated purpose. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Limits sharing to recipients the purpose requires. |
| [3.4.2 Share minimal data only](03-data-lifecycle-management.md#req-3-4-2) | Limits each transmission to the fields the purpose requires. |

<a id="ccpa-cal-code-regs-tit-11-7050"></a>
#### Cal. Code Regs. tit. 11, § 7050 Service Providers and Contractors

**●○○ Supporting**

Keep service providers and contractors within the business purpose in the contract, and make sure they can assist with consumer requests.

| APVS requirement | How it helps |
|---|---|
| [3.2.5 Purpose limitation](03-data-lifecycle-management.md#req-3-2-5) | Flags use of customer data outside its collection purpose, such as feeding it to model training. |
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Requires deletion requests to reach processors and the outcome to be confirmed. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | The index covers data held by processors, which lets the business answer requests for it. |
| [3.4.1 Share with minimal parties only](03-data-lifecycle-management.md#req-3-4-1) | Treats processors as recipients that must be required for the purpose of the exchange. |

<a id="ccpa-cal-code-regs-tit-11-7052"></a>
#### Cal. Code Regs. tit. 11, § 7052 Third Parties

**●○○ Supporting**

Pass consumer deletion, opt-out and limit requests to third parties that received the data and expect them to comply.

| APVS requirement | How it helps |
|---|---|
| [3.5.6 Deletion from 3rd parties](03-data-lifecycle-management.md#req-3-5-6) | Sends deletion requests to every recipient and records each response. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | Identifies the third parties that need to receive such requests. |

### Assessments and audits

<a id="ccpa-cal-code-regs-tit-11-7152"></a>
#### Cal. Code Regs. tit. 11, § 7152 Risk Assessment Requirements

**●○○ Supporting**

When processing triggers an assessment under 7150, such as selling or sharing data, processing sensitive personal information or using automated decisionmaking for significant decisions, document the operational elements, the categories of data, the purposes, the retention, the benefits and negative impacts, and the safeguards.

| APVS requirement | How it helps |
|---|---|
| [1.1.1 Personal data catalog](01-architecture-data-mapping.md#req-1-1-1) | The data catalog supplies the categories of personal data involved in each processing activity. |
| [1.2.1 Metadata tagging of personal records](01-architecture-data-mapping.md#req-1-2-1) | Record-level tags supply purposes, lineage and provenance. |
| [1.4.1 External Interfaces Documentation](01-architecture-data-mapping.md#req-1-4-1) | The interface inventory supplies the recipients and flows to describe. |
| [1.4.3 Processing purpose specification](01-architecture-data-mapping.md#req-1-4-3) | The processing purpose register supplies the stated purpose of each operation. |
| [2.1.2 Minimum sufficient data](02-minimality.md#req-2-1-2) | Minimization decisions are evidence that data volume and granularity were weighed against the purpose. |
| [3.3.1 Retention period defined per data class](03-data-lifecycle-management.md#req-3-3-1) | Defined retention periods supply the retention element. |
| [4.1.8 Automated decision-making disclosure](04-transparency-notice.md#req-4-1-8) | Identifies automated decision-making activities that fall into the assessment. |

<a id="ccpa-cal-code-regs-tit-11-7220"></a>
#### Cal. Code Regs. tit. 11, § 7220 Pre-use Notice Requirements

**●○○ Supporting**

Before using automated decisionmaking technology for a significant decision, give a prominent notice of its purpose, how to opt out, the data that affects outputs and how outputs are used.

| APVS requirement | How it helps |
|---|---|
| [4.1.8 Automated decision-making disclosure](04-transparency-notice.md#req-4-1-8) | Requires disclosure of the automated processing, its logic and its consequences for the person. |

<a id="ccpa-cal-code-regs-tit-11-7221"></a>
#### Cal. Code Regs. tit. 11, § 7221 Requests to Opt-Out of ADMT

**●○○ Supporting**

Let consumers opt out of automated decisionmaking technology used for significant decisions, unless a permitted exception such as a human appeal applies, and stop using the data within the required period.

| APVS requirement | How it helps |
|---|---|
| [5.2.1 Self-service privacy settings modification](05-privacy-features.md#req-5-2-1) | Provides self-service modification of settings inside the application. |
| [5.2.2 Settings changes propagate to processing](05-privacy-features.md#req-5-2-2) | Applies the change to processing within a disclosed period. |
| [4.3.2 Functional privacy settings](04-transparency-notice.md#req-4-3-2) | Confirms the setting stops the corresponding processing. |

<a id="ccpa-cal-code-regs-tit-11-7222"></a>
#### Cal. Code Regs. tit. 11, § 7222 Requests to Access ADMT

**●○○ Supporting**

On request, explain the purpose, logic and outcome of automated decisionmaking used for a significant decision about the consumer.

| APVS requirement | How it helps |
|---|---|
| [4.1.8 Automated decision-making disclosure](04-transparency-notice.md#req-4-1-8) | Requires documentation of the logic and consequences, which is the content the response draws on. |
| [1.3.1 Data subject identifier index](01-architecture-data-mapping.md#req-1-3-1) | Finds the inputs and outputs attributable to the requesting person. |
| [5.1.1 User Initiation](05-privacy-features.md#req-5-1-1) | Lets a user start the request in the application. |

### CCPA and CPRA provisions without an APVS counterpart

| Provision | Title | Why |
|---|---|---|
| Cal. Civ. Code § 1798.100(e) and 1798.150 | Reasonable security procedures and breach liability | APVS defers security controls to ASVS and does not set security requirements for protecting personal information. |
| Cal. Code Regs. tit. 11, §§ 7120 to 7124 | Cybersecurity audits (requirement, timing, independence, scope, certification) | These are organizational audits of a cybersecurity program, and APVS contains no security control requirements to map. |
| Cal. Civ. Code § 1798.120(c) and Cal. Code Regs. tit. 11, §§ 7070 and 7071 | Opt-in for sale or sharing of data of consumers under 16 | APVS has no requirement on age-gated or parental opt-in flows for sale or sharing. |
| Cal. Code Regs. tit. 11, § 7016 and Cal. Civ. Code § 1798.125(b) | Notice of financial incentive | APVS has no requirement on describing financial incentives or the value of consumer data. |
| Cal. Code Regs. tit. 11, § 7100 | Training | Staff training on consumer request handling is organizational and outside the scope of application requirements. |

---

## A.3 From requirement to regulation

| Requirement | Title | GDPR | CCPA and CPRA |
|---|---|---|---|
| [1.1.1](01-architecture-data-mapping.md#req-1-1-1) | Personal data catalog | Art. 5(2), Art. 24, Art. 30, Art. 33, Art. 35 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2), Cal. Code Regs. tit. 11, § 7152 |
| [1.2.1](01-architecture-data-mapping.md#req-1-2-1) | Metadata tagging of personal records | Art. 5(1)(b), Art. 5(1)(d), Art. 14, Art. 15, Art. 30 | Cal. Code Regs. tit. 11, § 7023, Cal. Civ. Code § 1798.110, Cal. Code Regs. tit. 11, § 7152 |
| [1.2.2](01-architecture-data-mapping.md#req-1-2-2) | Collection purpose specification | Art. 5(1)(b), Art. 30 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2), Cal. Code Regs. tit. 11, § 7002 |
| [1.2.3](01-architecture-data-mapping.md#req-1-2-3) | Last collection timestamp | Art. 5(1)(d), Art. 5(1)(e) | Cal. Civ. Code § 1798.100(a)(3) |
| [1.3.1](01-architecture-data-mapping.md#req-1-3-1) | Data subject identifier index | Art. 15, Art. 17, Art. 18, Art. 20, Art. 28, Art. 33, Art. 34 | Cal. Civ. Code § 1798.105, Cal. Civ. Code § 1798.106, Cal. Civ. Code § 1798.110, Cal. Code Regs. tit. 11, § 7024, Cal. Code Regs. tit. 11, § 7050, Cal. Code Regs. tit. 11, § 7222 |
| [1.3.2](01-architecture-data-mapping.md#req-1-3-2) | Multiple identifier support | Art. 11, Art. 15, Art. 34 | Cal. Civ. Code § 1798.105, Cal. Civ. Code § 1798.110 |
| [1.4.1](01-architecture-data-mapping.md#req-1-4-1) | External Interfaces Documentation | Art. 13, Art. 14, Art. 19, Art. 24, Art. 28, Art. 30, Art. 35 | Cal. Code Regs. tit. 11, § 7012, Cal. Civ. Code § 1798.110, Cal. Civ. Code § 1798.115, Cal. Civ. Code § 1798.100(d), Cal. Code Regs. tit. 11, § 7052, Cal. Code Regs. tit. 11, § 7152 |
| [1.4.2](01-architecture-data-mapping.md#req-1-4-2) | Passive and third-party collection | Art. 13, Art. 30 | Cal. Code Regs. tit. 11, § 7012, Cal. Civ. Code § 1798.115, Cal. Civ. Code § 1798.120, Cal. Civ. Code § 1798.100(d) |
| [1.4.3](01-architecture-data-mapping.md#req-1-4-3) | Processing purpose specification | Art. 5(1)(b), Art. 5(2), Art. 6(4), Art. 24, Art. 25(1), Art. 30, Art. 35 | Cal. Code Regs. tit. 11, § 7002, Cal. Code Regs. tit. 11, § 7152 |
| [2.1.1](02-minimality.md#req-2-1-1) | Necessity of each data element | Art. 5(1)(c), Art. 25(1), Art. 25(2), Art. 35 | Cal. Civ. Code § 1798.100(c), Cal. Code Regs. tit. 11, § 7002 |
| [2.1.2](02-minimality.md#req-2-1-2) | Minimum sufficient data | Art. 5(1)(c), Art. 11, Art. 25(1), Art. 25(2), Art. 35 | Cal. Civ. Code § 1798.100(c), Cal. Code Regs. tit. 11, § 7152 |
| [2.1.3](02-minimality.md#req-2-1-3) | Necessity reassessment on change or retirement | Art. 5(1)(b), Art. 5(1)(e) | Cal. Civ. Code § 1798.100(c) |
| [2.1.4](02-minimality.md#req-2-1-4) | Derived data precision | Art. 5(1)(c), Art. 9 | Cal. Civ. Code § 1798.100(c) |
| [2.1.5](02-minimality.md#req-2-1-5) | Optional data not functionally mandatory | Art. 5(1)(c), Art. 7(4), Art. 25(2) | Cal. Civ. Code § 1798.100(c), Cal. Civ. Code § 1798.125 and Cal. Code Regs. tit. 11, § 7080 |
| [2.1.6](02-minimality.md#req-2-1-6) | Abstract and aggregate | Art. 5(1)(c), Art. 25(1) | Cal. Civ. Code § 1798.100(c) |
| [2.1.7](02-minimality.md#req-2-1-7) | Granularity degradation over time | Art. 5(1)(c) | Cal. Civ. Code § 1798.100(c) |
| [2.2.1](02-minimality.md#req-2-2-1) | Location data granularity | Art. 5(1)(c), Art. 25(2) | Cal. Civ. Code § 1798.100(c) |
| [2.2.2](02-minimality.md#req-2-2-2) | Age / date of birth granularity | Art. 5(1)(c), Art. 8 | Cal. Civ. Code § 1798.100(c) |
| [2.2.3](02-minimality.md#req-2-2-3) | Identity granularity | Art. 5(1)(c), Art. 11 | Cal. Civ. Code § 1798.100(c) |
| [2.2.4](02-minimality.md#req-2-2-4) | Photo metadata | Art. 5(1)(c) | Cal. Civ. Code § 1798.100(c) |
| [2.2.5](02-minimality.md#req-2-2-5) | File metadata | Art. 5(1)(c) | Cal. Civ. Code § 1798.100(c) |
| [2.2.6](02-minimality.md#req-2-2-6) | Communication, call and message history | Art. 5(1)(c) | Cal. Civ. Code § 1798.100(c) |
| [2.2.7](02-minimality.md#req-2-2-7) | Live streaming data | Art. 5(1)(c) | Cal. Civ. Code § 1798.100(c) |
| [3.1.1](03-data-lifecycle-management.md#req-3-1-1) | Discard collected data if purpose is met | Art. 5(1)(c), Art. 25(1) | Cal. Civ. Code § 1798.100(c) |
| [3.1.2](03-data-lifecycle-management.md#req-3-1-2) | Privacy-aware input nudges | Art. 9 |  |
| [3.2.1](03-data-lifecycle-management.md#req-3-2-1) | Deletion on processing completion | Art. 5(1)(e) |  |
| [3.2.2](03-data-lifecycle-management.md#req-3-2-2) | Deletion trigger mechanism | Art. 5(1)(e) |  |
| [3.2.3](03-data-lifecycle-management.md#req-3-2-3) | Processing outcome recorded independently of source data | Art. 25(1) |  |
| [3.2.4](03-data-lifecycle-management.md#req-3-2-4) | Client-side computing | Art. 5(1)(c), Art. 25(1) |  |
| [3.2.5](03-data-lifecycle-management.md#req-3-2-5) | Purpose limitation | Art. 5(1)(b), Art. 6(4) | Cal. Civ. Code § 1798.100(c), Cal. Code Regs. tit. 11, § 7002, Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027, Cal. Code Regs. tit. 11, § 7050 |
| [3.3.1](03-data-lifecycle-management.md#req-3-3-1) | Retention period defined per data class | Art. 5(1)(e), Art. 25(2), Art. 30 | Cal. Civ. Code § 1798.100(a)(3), Cal. Civ. Code § 1798.100(c), Cal. Code Regs. tit. 11, § 7152 |
| [3.3.2](03-data-lifecycle-management.md#req-3-3-2) | Residual retention window for temporary data | Art. 5(1)(e) | Cal. Civ. Code § 1798.100(a)(3) |
| [3.3.3](03-data-lifecycle-management.md#req-3-3-3) | Automated deletion at retention expiry | Art. 5(1)(e), Art. 25(1), Art. 25(2) | Cal. Civ. Code § 1798.100(a)(3) |
| [3.3.4](03-data-lifecycle-management.md#req-3-3-4) | Corrected data propagation | Art. 5(1)(d), Art. 16 | Cal. Civ. Code § 1798.106, Cal. Code Regs. tit. 11, § 7023 |
| [3.3.5](03-data-lifecycle-management.md#req-3-3-5) | Pseudonymous references | Art. 25(1), Art. 32 |  |
| [3.3.6](03-data-lifecycle-management.md#req-3-3-6) | Pseudonym/identity mapping separation | Art. 5(1)(f), Art. 25(1), Art. 32 |  |
| [3.3.7](03-data-lifecycle-management.md#req-3-3-7) | Pseudonymous audit logs | Art. 5(1)(f), Art. 32 |  |
| [3.4.1](03-data-lifecycle-management.md#req-3-4-1) | Share with minimal parties only | Art. 19, Art. 25(2), Art. 28 | Cal. Civ. Code § 1798.115, Cal. Civ. Code § 1798.120, Cal. Code Regs. tit. 11, § 7026, Cal. Civ. Code § 1798.100(d), Cal. Code Regs. tit. 11, § 7050 |
| [3.4.2](03-data-lifecycle-management.md#req-3-4-2) | Share minimal data only | Art. 5(1)(c), Art. 9, Art. 25(2) | Cal. Civ. Code § 1798.100(c), Cal. Civ. Code § 1798.100(d) |
| [3.4.3](03-data-lifecycle-management.md#req-3-4-3) | Application-level data access tracking | Art. 5(1)(f), Art. 5(2), Art. 9, Art. 15, Art. 32, Art. 33, Art. 35 | Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027 |
| [3.4.4](03-data-lifecycle-management.md#req-3-4-4) | Machine-readable export | Art. 15, Art. 20 | Cal. Civ. Code § 1798.110, Cal. Code Regs. tit. 11, § 7024 |
| [3.5.1](03-data-lifecycle-management.md#req-3-5-1) | Secure deletion as default | Art. 5(1)(e), Art. 5(1)(f), Art. 17, Art. 32 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7022 |
| [3.5.2](03-data-lifecycle-management.md#req-3-5-2) | On Demand Deletion | Art. 17 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7022, Cal. Code Regs. tit. 11, § 7021 |
| [3.5.3](03-data-lifecycle-management.md#req-3-5-3) | Deletion from backups | Art. 5(1)(e), Art. 17 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7022 |
| [3.5.4](03-data-lifecycle-management.md#req-3-5-4) | Deletion from logs | Art. 5(1)(e), Art. 17 | Cal. Civ. Code § 1798.105 |
| [3.5.5](03-data-lifecycle-management.md#req-3-5-5) | Deletion of temporary data | Art. 5(1)(e), Art. 17 | Cal. Civ. Code § 1798.105 |
| [3.5.6](03-data-lifecycle-management.md#req-3-5-6) | Deletion from 3rd parties | Art. 17, Art. 19, Art. 28 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7022, Cal. Code Regs. tit. 11, § 7026, Cal. Code Regs. tit. 11, § 7050, Cal. Code Regs. tit. 11, § 7052 |
| [3.5.7](03-data-lifecycle-management.md#req-3-5-7) | Deletion evidence | Art. 5(2), Art. 17, Art. 24 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7022, Cal. Code Regs. tit. 11, § 7021, Cal. Code Regs. tit. 11, § 7101 |
| [4.1.1](04-transparency-notice.md#req-4-1-1) | Privacy notice at collection | Art. 5(1)(a), Art. 6(1)(a), Art. 7(1), Art. 12, Art. 13 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2), Cal. Code Regs. tit. 11, § 7012, Cal. Code Regs. tit. 11, § 7011, Cal. Code Regs. tit. 11, § 7003 |
| [4.1.2](04-transparency-notice.md#req-4-1-2) | Contextual notice per processing activity | Art. 5(1)(a), Art. 12, Art. 13 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2), Cal. Code Regs. tit. 11, § 7012 |
| [4.1.3](04-transparency-notice.md#req-4-1-3) | Notice content — required fields | Art. 5(1)(a), Art. 5(1)(b), Art. 13, Art. 14 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2), Cal. Code Regs. tit. 11, § 7012, Cal. Civ. Code § 1798.100(a)(3), Cal. Code Regs. tit. 11, § 7011 |
| [4.1.4](04-transparency-notice.md#req-4-1-4) | Named third-party recipients | Art. 13, Art. 14 | Cal. Civ. Code § 1798.100(a)(1) and (a)(2) |
| [4.1.5](04-transparency-notice.md#req-4-1-5) | Retention period specificity in notice | Art. 13, Art. 14 | Cal. Civ. Code § 1798.100(a)(3) |
| [4.1.6](04-transparency-notice.md#req-4-1-6) | Notice for indirectly collected data | Art. 14 |  |
| [4.1.7](04-transparency-notice.md#req-4-1-7) | Material change notification | Art. 5(1)(a), Art. 13, Art. 14 | Cal. Code Regs. tit. 11, § 7011 |
| [4.1.8](04-transparency-notice.md#req-4-1-8) | Automated decision-making disclosure | Art. 13, Art. 14 | Cal. Code Regs. tit. 11, § 7152, Cal. Code Regs. tit. 11, § 7220, Cal. Code Regs. tit. 11, § 7222 |
| [4.2.1](04-transparency-notice.md#req-4-2-1) | Visual parity of privacy choices | Art. 6(1)(a) | Cal. Code Regs. tit. 11, § 7004 |
| [4.2.2](04-transparency-notice.md#req-4-2-2) | No pre-selection or inaction consent | Art. 6(1)(a), Art. 25(2) | Cal. Code Regs. tit. 11, § 7028, Cal. Code Regs. tit. 11, § 7004 |
| [4.2.3](04-transparency-notice.md#req-4-2-3) | Consent granularity — one purpose per consent act | Art. 6(1)(a), Art. 7(2), Art. 7(4) | Cal. Code Regs. tit. 11, § 7002, Cal. Code Regs. tit. 11, § 7004 |
| [4.2.4](04-transparency-notice.md#req-4-2-4) | Consent separable from other matters | Art. 7(2), Art. 12 | Cal. Code Regs. tit. 11, § 7004 |
| [4.2.5](04-transparency-notice.md#req-4-2-5) | Consent withdrawal | Art. 6(1)(a), Art. 7(3) | Cal. Code Regs. tit. 11, § 7004 |
| [4.2.6](04-transparency-notice.md#req-4-2-6) | Consent record | Art. 5(2), Art. 6(1)(a), Art. 7(1), Art. 24 | Cal. Code Regs. tit. 11, § 7028, Cal. Code Regs. tit. 11, § 7101 |
| [4.2.7](04-transparency-notice.md#req-4-2-7) | No forced consent for core functionality | Art. 6(1)(a), Art. 7(4) | Cal. Civ. Code § 1798.125 and Cal. Code Regs. tit. 11, § 7080, Cal. Code Regs. tit. 11, § 7004 |
| [4.2.8](04-transparency-notice.md#req-4-2-8) | No pre-consent cookie initialisation | Art. 6(1)(a) |  |
| [4.2.9](04-transparency-notice.md#req-4-2-9) | Representative Framing of Privacy Choices | Art. 5(1)(a), Art. 6(1)(a) | Cal. Civ. Code § 1798.125 and Cal. Code Regs. tit. 11, § 7080, Cal. Code Regs. tit. 11, § 7004 |
| [4.2.10](04-transparency-notice.md#req-4-2-10) | No nagging | Art. 6(1)(a) | Cal. Code Regs. tit. 11, § 7028, Cal. Code Regs. tit. 11, § 7004 |
| [4.3.1](04-transparency-notice.md#req-4-3-1) | Privacy settings discoverability | Art. 12 | Cal. Code Regs. tit. 11, § 7003, Cal. Civ. Code § 1798.135(a), Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020, Cal. Code Regs. tit. 11, § 7004 |
| [4.3.2](04-transparency-notice.md#req-4-3-2) | Functional privacy settings | Art. 5(1)(a), Art. 21 | Cal. Civ. Code § 1798.120, Cal. Code Regs. tit. 11, § 7026, Cal. Code Regs. tit. 11, § 7221 |
| [4.3.3](04-transparency-notice.md#req-4-3-3) | Consistent privacy settings | Art. 7(2) | Cal. Code Regs. tit. 11, § 7003, Cal. Code Regs. tit. 11, § 7025, Cal. Code Regs. tit. 11, § 7004 |
| [4.3.4](04-transparency-notice.md#req-4-3-4) | Privacy settings reflect actual processing state | Art. 7(3), Art. 21 | Cal. Civ. Code § 1798.120, Cal. Code Regs. tit. 11, § 7025, Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027 |
| [4.3.5](04-transparency-notice.md#req-4-3-5) | Settings reset notification | Art. 25(2) |  |
| [4.3.6](04-transparency-notice.md#req-4-3-6) | Privacy dashboard existence | Art. 21 | Cal. Civ. Code § 1798.135(a), Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020 |
| [4.3.7](04-transparency-notice.md#req-4-3-7) | Privacy report | Art. 15 | Cal. Civ. Code § 1798.115 |
| [5.1.1](05-privacy-features.md#req-5-1-1) | User Initiation | Art. 12, Art. 15, Art. 16, Art. 17, Art. 18, Art. 20 | Cal. Civ. Code § 1798.105, Cal. Civ. Code § 1798.106, Cal. Civ. Code § 1798.110, Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020, Cal. Code Regs. tit. 11, § 7222 |
| [5.1.2](05-privacy-features.md#req-5-1-2) | Admin execution capability | Art. 5(1)(d), Art. 12, Art. 15, Art. 16, Art. 17, Art. 18, Art. 20 | Cal. Code Regs. tit. 11, § 7022, Cal. Civ. Code § 1798.106, Cal. Civ. Code § 1798.110, Cal. Code Regs. tit. 11, § 7024, Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020, Cal. Code Regs. tit. 11, § 7021 |
| [5.1.3](05-privacy-features.md#req-5-1-3) | Identity verification | Art. 11, Art. 12, Art. 15, Art. 16, Art. 17 | Cal. Civ. Code § 1798.105, Cal. Code Regs. tit. 11, § 7060, Cal. Code Regs. tit. 11, § 7063 |
| [5.1.4](05-privacy-features.md#req-5-1-4) | Service Communication | Art. 12, Art. 13 | Cal. Code Regs. tit. 11, § 7011, Cal. Civ. Code § 1798.135(a), Cal. Civ. Code § 1798.130(a)(1) and Cal. Code Regs. tit. 11, § 7020 |
| [5.2.1](05-privacy-features.md#req-5-2-1) | Self-service privacy settings modification | Art. 21 | Cal. Civ. Code § 1798.120, Cal. Code Regs. tit. 11, § 7026, Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027, Cal. Code Regs. tit. 11, § 7221 |
| [5.2.2](05-privacy-features.md#req-5-2-2) | Settings changes propagate to processing | Art. 7(3), Art. 18, Art. 21 | Cal. Civ. Code § 1798.120, Cal. Code Regs. tit. 11, § 7025, Cal. Code Regs. tit. 11, § 7026, Cal. Civ. Code § 1798.121 and Cal. Code Regs. tit. 11, § 7027, Cal. Code Regs. tit. 11, § 7221 |

---

<p style="opacity:.7;font-size:.9em"><a href="00-introduction.md">Introduction</a> · <a href="05-privacy-features.md">Previous: Privacy Features</a></p>
