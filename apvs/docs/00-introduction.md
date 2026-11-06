---
layout: default
title: "Introduction"
nav_order: 1
permalink: /
---

# OWASP Application Privacy Verification Standard

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance, verification and the chapter and section introductions are in beta, and the type of each requirement is waiting for community comments. The Status section below has the details.
</div>

## What APVS is

The Application Privacy Verification Standard (APVS) is a set of 79 testable requirements that describe what an application has to do, technically, to handle personal data responsibly. Similar to the OWASP Application Security Verification Standard (ASVS), each requirement is a single statement that a verifier can check against code, configuration or a running system, and each one carries a level that says how deep the verification needs to go. The requirements are anchored to the LINDDUN privacy threat taxonomy and organized around system design and components, which keeps the standard close to the way engineers describe their own systems. Legal interpretation stays with the people responsible for compliance, and APVS supplies the technical half of that conversation.

## Why it is useful

Privacy expectations usually reach development teams as legal text, written for lawyers and open to several readings, with no direct way to tell whether a given system meets them. APVS turns those expectations into statements that an engineer can implement and a reviewer can test, so a design review, a threat model or a penetration test can cover privacy alongside security. Teams get a shared vocabulary and a common scope, assessors get a baseline they can apply consistently from one system to the next, and organizations can choose a level for each system and track their progress against it. Security controls such as access control and encryption are already covered by ASVS, so APVS refers to those requirements and restates them only where a privacy perspective adds something new.

## Who it is for

Developers and architects can use the standard while they design and build, since the requirements describe concrete capabilities such as a personal data catalog, enforced retention or a consent record. Security engineers and testers use the verification text to plan their checks, and privacy engineers and auditors use the levels and the regulatory mapping to relate application behavior to legal obligations. Product owners and procurement teams can cite it as well, for instance by asking a vendor to meet Level 2 for a given application.

## How to use it

Start by choosing a level for the application.

| Level | Meaning | What verification needs |
|---|---|---|
| 🟢 L1 | Basic hygiene, the minimum bar | Inspection of documentation, code and configuration |
| 🟡 L2 | Standard baseline | Access to the running system and its configuration |
| 🟣 L3 | Applications that handle sensitive data at scale | Active testing of the running system |

The three levels describe how much verification an application warrants and do not form a maturity model, so applications in the same organization can sensibly sit at different levels. Each requirement also has a type. `APP` requirements are assessed for every application on its own, while `SYS` requirements describe infrastructure or platform capabilities that can be assessed once and relied on by all the applications running on that platform.

Chapter 1 is the natural starting point, because the data inventory, purpose records and data flow documentation it asks for are what the later chapters refer to when they talk about data elements, purposes and processing operations. Every requirement page has the same shape. The requirement is the normative statement, the guidance explains scope, examples and edge cases, and the verification text tells a reviewer how to confirm that the requirement is met. A privacy team that starts from a regulation can use the [regulatory mapping appendix](99-regulatory-mapping.md) to find the requirements that support a GDPR article or a CCPA/CPRA provision, and to find the provisions behind any requirement.

## What is inside

| Chapter | Title | Sections | Requirements | 🟢 L1 | 🟡 L2 | 🟣 L3 |
|---|---|---:|---:|---:|---:|---:|
| 1 | [Architecture & Data Mapping](01-architecture-data-mapping.md) | 4 | 9 | 1 | 5 | 3 |
| 2 | [Minimality](02-minimality.md) | 2 | 14 | 2 | 10 | 2 |
| 3 | [Data Lifecycle Management](03-data-lifecycle-management.md) | 5 | 25 | 4 | 11 | 10 |
| 4 | [Transparency & Notice](04-transparency-notice.md) | 3 | 25 | 10 | 13 | 2 |
| 5 | [Privacy Features](05-privacy-features.md) | 2 | 6 | 1 | 4 | 1 |
| | **Total** | | **79** | **18** | **43** | **18** |

The chapters are followed by an appendix. [Appendix A: Regulatory mapping](99-regulatory-mapping.md) relates GDPR articles and CCPA/CPRA provisions to these requirements and sits outside the numbered chapters.

## Status

Version 0.6 is an advanced draft, published for review and comment. The requirements are ready to be applied and challenged in earnest, and their wording and numbering can still change as comments arrive. Guidance and verification text are in beta and appear shaded and in italics throughout the chapters, so that nobody mistakes them for settled text. The chapter and section introductions are in beta as well. The type of each requirement, `APP` or `SYS`, is waiting for comments from the community and may be reassigned.

## Contributing

The standard is developed in the open, and review from people who build, test and audit applications is what moves it forward. The source of every chapter is a YAML file, and the pages here are generated from those files, so a change proposed against the YAML reaches every page at once. Comments, questions and suggestions are welcome as issues in the project repository, and concrete wording changes are welcome as pull requests.

Contributions that help most are

- review of requirement wording for clarity, testability and a positive, prescriptive phrasing,
- opinions on whether a requirement should be typed `APP` or `SYS`, and on the level it is assigned,
- improvements to guidance and verification text, especially practical examples and edge cases found in real assessments,
- gaps and overlaps, including requirements that duplicate ASVS or that need a privacy perspective added,
- experience reports from applying the standard to a real system, including requirements that proved hard to verify, and
- additions to the regulatory mapping appendix, such as further privacy laws.

---

<p style="opacity:.7;font-size:.9em">Next: <a href="01-architecture-data-mapping.md">Chapter 1, Architecture & Data Mapping</a> · <a href="99-regulatory-mapping.md">Appendix A: Regulatory mapping</a></p>
