# Quantum-Bloomberg-March-2026
> **Project:** Financial Sentiment Modeling & Market Inflection Analysis
> **Architecture:** Qiskit | IBM Quantum (Heron/Eagle Backends)

![Build Status](https://img.shields.io/badge/Status-Verified-success)
![License](https://img.shields.io/badge/License-MIT-blue)

## 📌 Executive Summary
A specialized quantum circuit designed to model asset decoupling and volatility correlation. This specific iteration captures the **March 9, 2026** session, focusing on the divergence between the Nasdaq (^IXIC) rally and IBM's bearish resistance.

---

## 🛠 Technical Specification

### Asset Encoding (Qubit Mapping)
| Qubit | Asset | Signal | Logic |
| :--- | :--- | :--- | :--- |
| **Q0** | Nasdaq | +1.32% | Bullish initialization via $U(2.1, 0, 0)$ |
| **Q1** | IBM | -2.08% | Mixed sentiment via $U(1.0, 0.45, 0)$ |
| **Q2** | JEPQ | +1.28% | Hedge correlation via $U(2.0, 0, 0)$ |
| **Q3** | TSLA | +0.49% | Momentum anchor via $U(1.65, 0.15, 0)$ |

### Circuit Logic: The "Market Drag" Operator
To represent the influence of market volatility on hedged positions, the circuit implements a **Controlled-Z (CZ)** equivalent:
$$CZ = (I \otimes H) \cdot CX \cdot (I \otimes H)$$
This phase-flip modeling captures hidden correlations in statevector amplitudes, revealing inflections not visible in standard technical charts.

---

## 📑 Governance
* **Author:** Lauro Sergio Vasconcellos Beck
* **Role:** Enterprise Architect / Independent Technical Consultant
