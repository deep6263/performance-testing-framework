# Performance Testing Framework

[![Performance Tests](https://github.com/deep6263/performance-testing-framework/actions/workflows/performance.yml/badge.svg)](https://github.com/deep6263/performance-testing-framework/actions/workflows/performance.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Locust](https://img.shields.io/badge/Locust-Performance%20Testing-green)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI-black)

An enterprise-style performance testing framework built with **Python and Locust** for load, stress, spike, and smoke testing of REST APIs.

The framework provides configurable load profiles, environment-based configuration, automated performance reports, response-time validation, failure-rate validation, and CI execution through GitHub Actions.

---

## 🚀 Features

- Smoke testing
- Load testing
- Stress testing
- Spike testing
- Configurable virtual users
- Configurable spawn rate
- Configurable test duration
- Environment-based configuration
- HTML performance reports
- CSV performance reports
- P95 response-time validation
- Failure-rate validation
- Automated PASS/FAIL quality gates
- Headless Locust execution
- GitHub Actions CI
- Performance reports uploaded as CI artifacts

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Load Profile       │
                    │   Configuration      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Profile Loader     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Locust Runner      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    REST API          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ HTML / CSV Reports   │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
             P95 Validation        Failure Rate
                    │                      │
                    └──────────┬───────────┘
                               ▼
                     Performance Quality
                           Gate