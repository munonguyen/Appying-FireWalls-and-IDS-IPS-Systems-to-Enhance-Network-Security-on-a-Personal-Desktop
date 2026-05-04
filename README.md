# Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop

**Hanoi University | Faculty of Information Technology**  
**Course:** Network Security  
**Instructor:** Đoàn Trung Sơn

---



---

## Abstract

In the context of rapidly increasing cybersecurity threats, personal desktop computers are becoming frequent targets of attacks such as malware, phishing, and unauthorized access. However, many individual users still lack appropriate security mechanisms, resulting in a high risk of data leakage and system intrusion.

This study focuses on evaluating the effectiveness of integrating a firewall with an Intrusion Detection and Prevention System (IDS/IPS) to enhance the security of personal computers. An experimental approach was employed by configuring firewall and IDS/IPS solutions, followed by testing through common attack scenarios such as port scanning, brute-force attacks, and malicious traffic injection.

**Key Findings:** Combining firewall and IDS/IPS mechanisms significantly improves the ability to detect and prevent threats compared to using either solution independently. Firewalls effectively control network traffic, while IDS/IPS helps identify more complex attack patterns.

**Keywords:** Firewalls, Intrusion Detection and Prevention System (IDS/IPS), Layered Security, Personal Desktop, Network Security

---

## 📑 Quick Navigation

- **[README.md](README.md)** ← Main project overview (this file)
- **[TEAM_ROLES.md](TEAM_ROLES.md)** - Team member responsibilities & progress
- **[TECHNICAL_SETUP.md](TECHNICAL_SETUP.md)** - System architecture & implementation details
- **[EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)** - Test execution logs & results
- **[OBJECTIVES.md](OBJECTIVES.md)** - Detailed project goals & motivation

---

## 🎯 Project Overview

### Research Problem

Personal desktop computers face increasing cybersecurity threats (malware, phishing, brute-force attacks) but often lack adequate protection mechanisms beyond basic firewalls and antivirus software.

### Research Solution

We evaluate a **layered security model** combining:

1. **Firewall** - Network traffic control & filtering
2. **IDS/IPS** - Deep packet inspection & threat detection

### Research Goal

Provide objective assessment of layered security effectiveness on personal computers and practical implementation guidelines for individual users.

---


---

## 🔬 Experimental Approach

### Attack Scenarios Tested

1. **Malware Simulation** - Flightsim C2 beaconing detection
2. **Brute-Force Attacks** - SSH/RDP authentication attacks
3. **Port Scanning** - Network reconnaissance detection

### Tools & Technologies

| Component         | Tool                      | Purpose                 |
| ----------------- | ------------------------- | ----------------------- |
| Firewall          | Windows Defender Firewall | Layer 1 Traffic Control |
| Packet Capture    | Npcap                     | Packet Interception     |
| IDS/IPS Engine    | Snort                     | Layer 2 Deep Analysis   |
| Malware Simulator | Flightsim                 | Safe Threat Simulation  |

### System Architecture

```
Threats → Firewall → Npcap → Snort IDS/IPS → Logs & Alerts → Protected Desktop
```

---

## 🎓 Why This Topic?

**1. Increasing Personal Cyber Threats**

- Personal/financial data stored on personal computers
- Growing threats from malware, spyware, phishing, hackers
- Individual users are among most vulnerable groups

**2. Understanding Security Technologies**

- Firewalls and IDS/IPS are essential security tools
- Study helps users understand practical protection strategies
- Foundation for extending to corporate/larger systems

**3. Practical & Feasible**

- Can be implemented on personal desktops
- No complex infrastructure required
- Practical application of security theory

---

## 📋 Objectives

### Primary Objectives

1. **Evaluate Effectiveness** - Assess how well combined firewall + IDS/IPS prevent/detect attacks
2. **Develop Configuration Model** - Best practices for balancing protection vs. resource usage
3. **Raise User Awareness** - Educate on layered security importance
4. **Compare Mechanisms** - Analyze standalone vs. combined approaches

### Success Metrics

| Metric          | Target    |
| --------------- | --------- |
| Detection Rate  | >90%      |
| Blocking Rate   | 70-100%   |
| False Positives | Low       |
| Response Time   | <1 second |

---

## 🏗️ Methodology

### Layered Security Model

**Layer 1: Firewall (Traffic Control)**

- Blocks unnecessary ports
- Restricts unknown IPs
- Protects critical services (SSH, RDP)
- Limits suspicious authentication attempts

**Layer 2: IDS/IPS (Deep Analysis)**

- Detects signature-based threats
- Identifies anomalous behaviors
- Catches encrypted payload threats
- Real-time alerting/blocking capability

### Key Strength

Firewall handles basic filtering (efficiency) + IDS/IPS performs deeper analysis (effectiveness) = Better detection & prevention

---

## 📈 Expected Results

### Malware Detection (Flightsim vs. Firewall+Snort)

| Metric          | Firewall Only | Firewall + IDS/IPS |
| --------------- | ------------- | ------------------ |
| Detection Rate  | 60%           | >90%               |
| False Positives | Medium        | Low                |
| Attack Success  | ~40%          | <10%               |

### Brute-Force Protection

- ✅ IDS detects consecutive failed logins
- ✅ Automatic blocking after 5-10 attempts
- ✅ Significant reduction in successful attempts

### Overall System Performance

- ✅ Reduced false positives
- ✅ Faster response time
- ✅ Multiple protection layers
- ✅ Comprehensive audit trail

---

## 📚 Research Foundation

This study builds on recent findings emphasizing:

- **NIST** - Layered monitoring with correlated analysis
- **Alshamrani et al.** - IDS/IPS integration for encrypted threats
- **Palo Alto Networks** - Detection of lateral movement & C2 traffic
- **Garcia-Teodoro et al.** - Hybrid IDS models combining signatures + anomalies

See **References** section below for complete citations.

---

## 🔗 Project Repository

**GitHub Repository:** [Applying Firewalls and IDS/IPS Systems](https://github.com/munonguyen/Appying-FireWalls-and-IDS-IPS-Systems-to-Enhance-Network-Security-on-a-Personal-Desktop)

---

## 📖 Detailed Documentation

- **[TEAM_ROLES.md](TEAM_ROLES.md)** - Full team member responsibilities & phase breakdown
- **[TECHNICAL_SETUP.md](TECHNICAL_SETUP.md)** - System architecture, tool configuration, custom Snort rules
- **[EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)** - Test scenarios, execution logs, preliminary results
- **[OBJECTIVES.md](OBJECTIVES.md)** - Detailed objectives and research questions

---

## 📝 References

[1] ENISA, Threat Landscape 2023, European Union Agency for Cybersecurity, Oct. 3, 2023  
[2] Phạm Lê, "An ninh mạng nửa đầu 2025: Việt Nam đối mặt làn sóng ransomware, phishing và APT," Tạp chí An ninh mạng Việt Nam, Sep. 12, 2025  
[3] L. Diana, P. Dini, and D. Paolini, "Overview on Intrusion Detection Systems for Computers Networking Security," Computers, vol. 14, no. 3, p. 87, Mar. 3, 2025  
[4] A. Trisolino, "Analysis of Security Configuration for IDS/IPS," Master's thesis, Politecnico di Torino, 2023  
[5] A. M. Diningrat, "Evaluation of Firewall and Intrusion Detection System (IDS) Technology Implementation," Institut Agama Islam Indonesia, Jun. 2025  
[6] K. Scarfone and P. Mell, Guide to Intrusion Detection and Prevention Systems (IDPS), NIST Special Publication 800-94, 2007  
[7] A. Alshamrani et al., "A survey on advanced persistent threats," IEEE Communications Surveys & Tutorials, vol. 21, no. 2, pp. 1851–1877, 2019  
[8] Palo Alto Networks, Unit 42 Annual Threat Report 2023, 2023  
[9] P. García-Teodoro et al., "Anomaly-based network intrusion detection," Computers & Security, vol. 28, nos. 1–2, pp. 18–28, 2009  
[10] R. A. A. Saleh et al., "Lightweight intrusion detection for IoT systems using artificial neural networks," in Security and Privacy in Communication Networks, 2024, pp. 45–59  
[11] R. Sommer and V. Paxson, "Outside the closed world: On using machine learning for network intrusion detection," 2010 IEEE Symposium on Security and Privacy, pp. 305–316  
[12] A. Karambelkar, "Next generation firewall using IPS & IDS," International Journal for Research in Applied Science and Engineering Technology, vol. 13, no. 4, pp. 2868–2874, Apr. 2025  
[13] M. Morimo et al., "Enhancing Performance of Intrusion Prevention Systems Through Firewall-IPS Coordination in SDN Environments," ACM Transactions on Autonomous and Adaptive Systems, vol. 20, no. 2, Article 15, pp. 1–15, 2025  
[14] Fortinet, Global Threat Landscape Report 2023, Fortinet Inc., 2023

---

**Last Updated:** May 4, 2026  
**Status:** In Progress ⏳  
**Next Milestone:** Complete experimental testing
