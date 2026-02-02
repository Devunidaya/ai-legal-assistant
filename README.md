⚔️ GenAI Legal Assistant for SMEs

demo video: 

deployment: 


A GenAI-powered legal intelligence platform designed to help Small and Medium Enterprises (SMEs) in India understand complex legal contracts, identify risks, and make informed decisions—without requiring legal expertise.

The system analyzes contracts, highlights unfavorable clauses, explains legal terms in plain business language, and generates actionable insights while maintaining confidentiality and auditability.

🚀 Project Overview

Legal contracts are often lengthy, complex, and difficult for non-legal professionals to interpret. This project aims to bridge that gap by building an AI-assisted legal analysis tool that:

Automatically analyzes contracts

Detects legal and business risks

Explains clauses in simple language

Assists SMEs in negotiation and compliance

Supports English and Hindi contracts

The platform is optimized for Indian SME use cases, focusing on common contractual risks and practical decision support.

🎯 Objectives

Simplify legal contract understanding for non-lawyers

Identify high-risk and non-SME-friendly clauses

Provide clause-level and contract-level risk scoring

Support multilingual contracts (English & Hindi)

Maintain data privacy with local-only processing

Generate professional summaries for legal consultation

🧠 Core Functional Capabilities
1️⃣ Legal NLP & Intelligence Tasks

Contract Type Classification

Clause & Sub-Clause Extraction

Named Entity Recognition (NER):

Parties

Dates

Jurisdiction

Financial Amounts

Liabilities

Obligation vs Right vs Prohibition Identification

Ambiguity Detection & Flagging

Clause Similarity Matching with Standard Templates

2️⃣ Risk Assessment Engine

Clause-level Risk Scores

Low

Medium

High

Contract-level Composite Risk Score

Identification of critical clauses:

Penalty clauses

Indemnity clauses

Unilateral termination rights

Arbitration & jurisdiction terms

Auto-renewal & lock-in periods

Non-compete clauses

Intellectual Property (IP) transfer clauses

3️⃣ User-Facing Outputs

Simplified contract summary

Clause-by-clause explanation in plain language

Highlighting of unfavorable clauses

Suggested renegotiation alternatives

SME-friendly standardized contract templates

Downloadable PDF summary for legal review

📂 Supported Input Formats

PDF (text-based)

DOC / DOCX

Plain Text (.txt)

📊 Data Elements Extracted

Parties involved

Financial amounts & penalties

Obligations & liabilities

Deliverables & performance metrics

Contract duration & timelines

Termination conditions

Jurisdiction & governing law

Rights & ownership (especially IP)

Confidentiality & NDA clauses

🌐 Multilingual Support

Input contracts supported in:

English

Hindi

Internal normalization:

Hindi → English (for NLP processing)

Output explanations:

Simple business English (SME-friendly)

🔐 Privacy, Security & Compliance

All documents processed locally

No external API calls for legal data

No storage of uploaded files

Optional JSON-based audit logs

Designed for confidentiality-sensitive legal workflows

🛠️ Technology Stack
Allowed & Used Tooling
Layer	Technology
LLM (Reasoning)	Claude 3 / GPT-4
NLP Processing	Python (spaCy / NLTK)
UI	Streamlit / Gradio
Storage	Local files, JSON logs
Integrations	❌ None
External Legal APIs	❌ Not allowed

⚠️ Note:
No external case law, statutes, or legal APIs are used—ensuring compliance with tooling restrictions.

🖥️ User Interface

Blue–Green professional LegalTech theme

Dashboard-style layout

Clause-level expanders

Risk indicators & highlights

PDF export for offline sharing

📈 Target Users

Small & Medium Business Owners

Startup Founders

Operations & HR Managers

Finance & Procurement Teams

Legal Consultants assisting SMEs

📌 Use Cases

Reviewing employment agreements before hiring

Evaluating vendor & supplier contracts

Assessing lease agreements for office space

Analyzing partnership deeds

Understanding service contracts & SLAs

📄 Output Artifacts

Risk-scored contract analysis

Plain-language explanations

Professional PDF summaries

Audit-ready analysis records

⚠️ Disclaimer

This tool is intended to assist decision-making, not replace professional legal advice.
Users are encouraged to consult qualified legal professionals before finalizing contracts.

👨‍💻 Project Status

✅ Core analysis engine implemented

✅ Streamlit UI completed

🚧 Advanced NLP & multilingual expansion (future scope)

🌟 Future Enhancements

Chat-based contract Q&A

Risk score visualizations

Multi-contract comparison

Version tracking & clause history

Light/Dark UI toggle

📜 License

This project is developed for educational and research purposes.
Commercial usage requires further compliance review.
