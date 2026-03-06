Enterprise DevSecOps Pipeline

🛡️ Architecture Overview

This repository demonstrates a fully automated, "Shift-Left" DevSecOps pipeline using GitHub Actions. It proves the ability to integrate aggressive security auditing directly into the CI/CD lifecycle, preventing vulnerable code and misconfigured infrastructure from reaching production.

⚙️ Security Toolchain Integrated

This pipeline automatically executes the following security gates on every push/pull request:

Secret Scanning (TruffleHog): Deep history scanning to ensure no API keys, AWS credentials, or sensitive tokens are committed to the codebase.

Static Application Security Testing (Bandit): SAST scanning of the Python microservice to detect logic flaws and security vulnerabilities.

Infrastructure as Code Linting (Hadolint): Static analysis of the Dockerfile to enforce security best practices (e.g., executing as a non-root user).

Container Vulnerability Scanning (Trivy): Deep OS and library-level scanning of the compiled Docker image to block critical/high CVEs before deployment to a container registry.

🐳 Secure Containerization

The included Dockerfile demonstrates enterprise hardening techniques:

Implementation of a strict Non-Root User (appuser).

Optimized layer caching.

Ephemeral build structures using minimal base images (python:slim).

Base package manager upgrades to patch vendor-embedded CVEs before application deployment.

Architected by Ayham Alhalabi DevSecOps Engineer & Security Consultant | View B2B Consulting Portfolio
