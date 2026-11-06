---
layout: default
title: "Chapter 5: Privacy Features"
nav_order: 6
---

# Chapter 5. Privacy Features

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.10);padding:.6em 1em;margin:1em 0;border-radius:4px;">
<strong>APVS version 0.6, advanced draft for publication and comments.</strong>
Guidance and verification text (shaded and in italics below) are in beta. Requirement type is waiting for community comments, and the chapter and section introductions are in beta as well. Wording will keep moving as feedback arrives.
</div>

Covers the capabilities an application must provide so that individuals can exercise control over their personal data and so that authorized staff can act on their requests. It exists because privacy outcomes depend on features that work inside the application, where they can be tested.

## About this chapter

Privacy promises only count when the application can keep them. A person who asks to see, export, restrict or delete their data, or who wants to switch off a kind of processing, needs a place in the product where that can happen, and the organization needs tooling that carries the request through to the stored data. This chapter specifies those privacy features and the controls around them, so that a verifier can look at a running application and confirm that the capabilities exist and behave as described.

The chapter deals only with what the application itself does. Requests that arrive by email, phone or paper, and the internal procedures an organization wraps around them, vary enormously between companies and fall outside what an application can be tested for. What the application must supply is the entry point for the individual, the means for authorized personnel to execute the request against real data, a proportionate check that the requester is who they claim to be, and a clear explanation of how to use all of this. The required features correspond to rights such as access, export, deletion and restriction, and the requirements are phrased as application capabilities so that they remain useful in jurisdictions with different legal vocabularies.

Three terms recur and are worth keeping apart. A user is someone who has an account and uses the system. A data subject is the person the personal data is about, who may or may not be a user, as with a colleague named in a shared document or a customer of a business that uses the software. An individual is the broader term for any person who may want to exercise a privacy feature, including people who hold no account. The requirements use the term that fits the context, and the choice matters because self-service features can only be offered to people the system can authenticate, while other individuals still need a documented way to reach the organization.

Two principles run through the chapter. Controls must be reachable without leaving the application or asking for help. Controls must also have real effect, so a changed setting has to alter what the system actually processes within a period that is disclosed to the person who changed it. Identity checks follow a proportionality principle in the same spirit as the minimality principles of Chapter 2, asking for no more verification than the sensitivity of the data and the right being exercised justify.

## Sections at a glance

| Section | Title | Requirements | <span style="color:#1a7f37">L1</span> | <span style="color:#9a6700">L2</span> | <span style="color:#8250df">L3</span> |
|---|---|---:|---:|---:|---:|
| [5.1](#section-5-1) | Privacy Feature Enablement | 4 | 1 | 2 | 1 |
| [5.2](#section-5-2) | Privacy Settings Control (Intervenability) | 2 | 0 | 2 | 0 |

---

<a id="section-5-1"></a>
## 5.1 Privacy Feature Enablement

This section covers how privacy features are made available and carried out, from the self-service entry point for registered users and the tooling that lets authorized staff act on a request to the proportionate check of who is asking and the clear communication of how to reach these features. How an organization runs its internal procedures around them is out of scope.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [5.1.1](#req-5-1-1) | User Initiation | 🟣 L3 | `SYS` |
| [5.1.2](#req-5-1-2) | Admin execution capability | 🟡 L2 | `SYS` |
| [5.1.3](#req-5-1-3) | Identity verification | 🟡 L2 | `SYS` |
| [5.1.4](#req-5-1-4) | Service Communication | 🟢 L1 | `SYS` |

<a id="req-5-1-1"></a>
### 5.1.1 User Initiation

<span title="Level 3, sensitive data at scale" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#8250df;background:rgba(130,80,223,.14);border:1px solid #8250df">L3</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide registered users with self-service access to initiate each supported privacy feature directly from within the system interface, without requiring contact with support or navigation to an external system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This requirement is that a mechanism exists and is reachable — not that it is automated.

This is NOT about submitting DSR in general (eg via janitor), that is outside the scope of the application.  
This requirement is specifically around registered users, logged in and self-service.

This does not mean the response is instant.

This requirement governs the initiation point only — the mechanism by which a user triggers a capability.

How that is actually executed is procedural and depends on how the org and privacy team are dealing with this. This is out of scope for APVS.

this is for fulfilling DSR

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm DSR submission interface exists within the application. Confirm it is reachable within two navigational steps. Confirm it does not require support contact or external navigation.

Inspect: attempt to initiate each personal data capability from within the system interface using a registered user account. Any capability that requires support contact, external navigation, or is unreachable within standard system navigation is a finding.

</div>

<a id="req-5-1-2"></a>
### 5.1.2 Admin execution capability

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide administrative capabilities that enable authorized personnel to locate, retrieve, export, delete, and restrict personal data for a specific data subject in response to a data subject request, without requiring direct database access or custom scripting.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

The system must provide the tooling — how the organisation uses it is procedural and out of scope.

This is about fullfilling the requests from individuals. We make abstraction of the underlying procedures--whether this is done through email to the DPO and the DPO checks the data themselves, or there is a very extensive process and tool support at the privacy team side that automates requests to the app data--we want to express that those data (capabilitues) requests can get executed within the system, initiated by the org person authorized to do so.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect: confirm an admin interface or equivalent capability exists for each DSR type (access, erasure, portability, restriction, rectification). Absence of admin capability for any DSR type requiring system access is a finding.

</div>

<a id="req-5-1-3"></a>
### 5.1.3 Identity verification

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must provide a mechanism to verify the identity of a data subject before fulfilling a privacy feature, proportionate to the sensitivity of the data held and the nature of the right requested.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Verification must not overcollect — a full KYC process is disproportionate for low-sensitivity requests. The proportionality principle means: higher-impact rights (erasure, access to sensitive data) may require stronger verification than lower-impact rights.

Either through basic authentication (user is known and authenticated, so is authorized for DSRs, or a process is supported to verify the requestor's identity)

There must be provisions for delegated DSRs (e.g. "power of attorney" or "health care proxy" situations).  
As well as age thresholds for DSRs, minors probably cannot (?) perform a DSR on their own, therefore legal guardianship must be confirmed.  
Consult legal counsel.

Identity data must be removed upon completion of the request.

Implementation options may include direct authentication, automated identification services, and such.  
These might be fully automated, or human in the loop.

Even if this is not implemented, legally identity must be verified manually / out of band

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Inspect + Test: confirm a verification step exists in the DSR flow. Confirm it does not require disproportionate personal data collection. Test that an unverified or mismatched identity cannot retrieve another subject's data.

</div>

<a id="req-5-1-4"></a>
### 5.1.4 Service Communication

<span title="Level 1, basic hygiene" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#1a7f37;background:rgba(26,127,55,.14);border:1px solid #1a7f37">L1</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

The system must clearly and explicitly describe to individuals how they can access these features or request a human process to serve these features.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Not yet provided.

</div>

---

<a id="section-5-2"></a>
## 5.2 Privacy Settings Control (Intervenability)

This section covers intervenability, the ability of people to steer how their data is used through privacy settings. Users can change their own settings from within the application, and those changes reach the processing itself within an immediate or disclosed period, so that a setting reflects what the system really does.

| ID | Requirement | Level | Type |
|---|---|:---:|:---:|
| [5.2.1](#req-5-2-1) | Self-service privacy settings modification | 🟡 L2 | `APP` |
| [5.2.2](#req-5-2-2) | Settings changes propagate to processing | 🟡 L2 | `SYS` |

<a id="req-5-2-1"></a>
### 5.2.1 Self-service privacy settings modification

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="Application-specific" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#0969da;background:rgba(9,105,218,.12);border:1px solid #0969da">APP</span>

**Requirement**

The system must enable users to modify their own privacy settings from within the system interface, without requiring contact with support, submission of a request, or navigation to an external system.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This is a technical capability requirement — the system must support self-service modification.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: attempt to modify each privacy setting from within the system without support contact. Any setting that cannot be modified without external assistance is a finding.

</div>

<a id="req-5-2-2"></a>
### 5.2.2 Settings changes propagate to processing

<span title="Level 2, standard baseline" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#9a6700;background:rgba(154,103,0,.14);border:1px solid #9a6700">L2</span> <span title="System-wide" style="display:inline-block;padding:0 .55em;border-radius:1em;font-size:.85em;font-weight:600;color:#57606a;background:rgba(87,96,106,.16);border:1px solid #57606a">SYS</span>

**Requirement**

Changes made to privacy settings must take effect on actual processing immediately or within a technically justified and disclosed maximum period.

<div markdown="1" style="border-left:4px solid #b7791f;background:rgba(183,121,31,.08);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Guidance</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

This requirement covers the backend effect — the system must actually stop or start processing in response to the change.

</div>

<div markdown="1" style="border-left:4px solid #6b7fa6;background:rgba(107,127,166,.10);padding:.4em 1em;margin:.8em 0;border-radius:4px;font-style:italic;">
<strong style="font-style:normal">Verification</strong> <span style="font-style:normal;font-size:.8em;opacity:.75">(beta)</span>

Test: modify a privacy setting and monitor actual processing. Confirm processing changes within the disclosed period. Continued processing beyond the disclosed period after a restriction is a finding.

</div>

---

<p style="opacity:.7;font-size:.9em">
<a href="00-introduction.md">Introduction</a> · <a href="04-transparency-notice.md">Previous: Transparency & Notice</a> · <a href="99-regulatory-mapping.md">Next: Appendix A: Regulatory mapping</a>
</p>
