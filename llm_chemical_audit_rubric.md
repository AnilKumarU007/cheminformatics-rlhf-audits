# Process-Supervised Reward Modeling (PRM) Rubric for Chemical Reasoning
## Overview
This rubric defines evaluation standards for auditing Large Language Model (LLM) outputs on advanced organic and physical chemistry reasoning tasks.
## Scoring Criteria (0 to 5 Scale) :-
* **Score 5 (Flawless):** Zero hallucination. Complete mechanistic rigor, correct thermodynamic vs. kinetic control distinction, proper stereochemical designation (CIP rules), and warning-free RDKit/Python code with defensive null-checks.
* **Score 3 (Minor Flaw):** Correct outcome or final product, but contains minor reasoning leaps or suboptimal computational syntax.
* **Score 1 (Critical Failure):** Major chemical hallucination (e.g., violating Woodward-Hoffmann orbital symmetry rules, confusing state functions with path functions, or using unvalidated SMILES parsing without error handling).
