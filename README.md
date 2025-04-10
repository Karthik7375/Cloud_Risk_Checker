# ☁️ Cloud Security Risk Scanner (with Synthetic Data)

A simulated threat detection engine that scans mock cloud infrastructure (IAM, S3 Buckets, Security Groups) for common misconfigurations. Built for learning, showcasing secure cloud practices, and testing security automations without needing access to real cloud accounts.

# 📘 Background Knowledge
🪣 Amazon S3 Buckets
Amazon S3 (Simple Storage Service) is used to store objects/files in the cloud. Misconfigured S3 buckets (like public read/write access) are a major data breach risk.

🔐 Security Groups
Security Groups are like firewalls for your cloud servers (EC2). If ports like 22 (SSH) or 3306 (MySQL) are open to 0.0.0.0/0, attackers can easily scan and exploit them.

👤 IAM (Identity and Access Management)
IAM controls who can do what. Users without Multi-Factor Authentication (MFA) or users with wildcard policies (*) pose a massive security risk if compromised.


## 🔍 What This Project Does

- 🪣 Detects publicly exposed S3 buckets.
- 🔓 Flags security groups with risky open ports (like SSH to `0.0.0.0/0`).
- 👤 Identifies IAM users without MFA or over-permissive policies.
- 🧪 Uses a synthetic data generator to create realistic-looking cloud config data.

> ⚠️ This is a learning tool for aspiring cloud security engineers. No real infrastructure is used or required.

---

## 📦 Project Structure

```bash
.
├── mock_data/
│   ├── iam_users.json
│   ├── s3_buckets.json
│   └── security_groups.json
├── generate_mock_data.py
└── risk_scanner.py
└── risk_rules.py
```



# ⚙️ Technologies Used
Python 3
JSON
Random/Synthetic Data Generation
Cloud Security Concepts


# 📌 Future Ideas
Integrate real AWS SDK (boto3) for scanning live accounts
Add scoring system for risk levels
Export reports (CSV, PDF)
Add basic dashboard (e.g., Streamlit)

# 🔒 Disclaimer
This project uses fake, synthetic data. No cloud credentials are used or exposed. Built strictly for educational and demo purposes.

