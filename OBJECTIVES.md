# Project Objectives & Research Goals

## Research Focus

**Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop**

---

## 🎯 Primary Objectives

### Objective 1: Evaluate Effectiveness of Layered Security

**Goal:** Assess how well combined firewall + IDS/IPS mechanisms prevent and detect attacks

**What We Measure:**

- Detection rate of various attack types
- Blocking effectiveness vs. firewall alone
- Time to detect and respond to threats
- False positive rate (minimize)
- False negative rate (minimize)

**Success Criteria:**

- ✅ Detection rate >90%
- ✅ Blocking rate 70-100%
- ✅ False positives <5%
- ✅ Response time <1 second

---

### Objective 2: Develop Practical Desktop Security Configuration Model

**Goal:** Identify best practices for configuring Firewalls and IDS/IPS that balance protection vs. resource usage

**Configuration Aspects:**

- Firewall rule optimization
- IDS/IPS rule customization
- Resource consumption analysis
- Performance impact assessment
- Tuning for false positive reduction

**Deliverables:**

- ✅ Recommended firewall rules set
- ✅ Custom Snort detection rules
- ✅ Configuration best practices guide
- ✅ Resource consumption baseline

---

### Objective 3: Raise User Awareness of Personal Security

**Goal:** Educate individual users on importance and implementation of layered security

**Educational Aspects:**

- Why single-layer defense is insufficient
- How firewalls and IDS/IPS complement each other
- Practical implementation steps for personal users
- Common security mistakes and how to avoid them
- Maintenance and monitoring requirements

**Intended Impact:**

- ✅ Users understand layered security concept
- ✅ Users can implement on their own systems
- ✅ Users maintain and monitor security systems
- ✅ Users adopt proactive security posture

---

### Objective 4: Compare & Analyze Security Mechanisms

**Goal:** Objectively evaluate standalone vs. combined approaches

**Comparison Framework:**

| Aspect                | Firewall Only | IDS/IPS Only  | Combined     |
| --------------------- | ------------- | ------------- | ------------ |
| **Traffic Control**   | ✅ Excellent  | ❌ None       | ✅ Excellent |
| **Threat Detection**  | ⚠️ Limited    | ✅ Excellent  | ✅ Excellent |
| **Deep Inspection**   | ❌ No         | ✅ Yes        | ✅ Yes       |
| **Resource Usage**    | ✅ Low        | ⚠️ Medium     | ⚠️ Medium    |
| **False Positives**   | ✅ Low        | ❌ Medium     | ✅ Low       |
| **Encrypted Threats** | ❌ No         | ✅ Behavioral | ✅ Yes       |

---

## 🔬 Research Questions

### RQ1: Effectiveness

**Question:** How much more effective is a layered model compared to standalone firewall?

**Expected Finding:** >30% improvement in detection rate, >50% reduction in attack success

### RQ2: Resource Efficiency

**Question:** What is the resource overhead of adding IDS/IPS to an existing firewall?

**Expected Finding:** <10% CPU usage, <50MB memory for typical personal use

### RQ3: Practicality

**Question:** Can an average personal user deploy and maintain this system?

**Expected Finding:** Yes, with proper documentation and pre-configured rules

### RQ4: Coverage

**Question:** What types of attacks are caught by firewall vs. IDS/IPS vs. both?

**Expected Finding:** Firewall blocks 50-60%, IDS/IPS catches 30-40% of what firewall misses

### RQ5: False Positives

**Question:** How many legitimate connections are incorrectly flagged as threats?

**Expected Finding:** <2% false positive rate with properly tuned rules

---

## 📊 Test Scenarios

### Scenario 1: Malware (C2 Beaconing)

**Attack Type:** Flightsim malware simulation  
**Objective:** Evaluate detection of encrypted malicious traffic using legitimate ports

**Expected Behavior:**

- ❌ Firewall: Allows traffic (appears legitimate on port 443)
- ✅ IDS/IPS: Detects C2 beaconing pattern
- Result: **Combined system catches the threat**

---

### Scenario 2: Brute-Force Attack

**Attack Type:** Multiple failed SSH/RDP login attempts  
**Objective:** Evaluate protection against credential-based attacks

**Expected Behavior:**

- ⚠️ Firewall: May limit attempts (if configured)
- ✅ IDS/IPS: Detects pattern and alerts
- Result: **Combined system blocks attacker IP**

---

### Scenario 3: Port Scanning

**Attack Type:** Network reconnaissance  
**Objective:** Evaluate detection of early-stage attacks

**Expected Behavior:**

- ⚠️ Firewall: Blocks packets but no alert
- ✅ IDS/IPS: Detects scanning pattern immediately
- Result: **Combined system provides early warning**

---

## 📈 Success Metrics

### Detection Effectiveness

```
Detection Rate = (Threats Detected / Total Threats) × 100
Target: >90% for combined system
```

### Prevention Effectiveness

```
Prevention Rate = (Threats Blocked / Threats Detected) × 100
Target: 70-100% for combined system
```

### False Positive Rate

```
FPR = (False Alerts / Total Traffic) × 100
Target: <2% for combined system
```

### Response Time

```
Response Time = Time from threat arrival to system alert
Target: <1 second for combined system
```

### System Performance Impact

```
Resource Overhead = (Resource with IDS/IPS - Resource without) / Resource without × 100
Target: <15% for CPU, <10% for memory
```

---

## 🎓 Educational Outcomes

### Students Will Understand

1. ✅ How firewalls control network traffic
2. ✅ How IDS/IPS detects complex attacks
3. ✅ Why layered security is necessary
4. ✅ How to configure security systems practically
5. ✅ How to interpret security logs

### Students Will Be Able To

1. ✅ Design layered security architecture
2. ✅ Configure firewall rules appropriately
3. ✅ Write custom IDS/IPS detection rules
4. ✅ Test security systems effectively
5. ✅ Analyze and interpret security alerts

---

## 🏆 Overall Research Goal

**Provide empirical evidence that:**

- Layered security model is practical for personal desktops
- Combining firewall + IDS/IPS significantly improves protection
- Individual users can implement and maintain this system
- Benefits outweigh resource costs

**Deliverable:**

- Comprehensive research report with practical implementation guide
- Best practices for personal desktop security
- Configurable system ready for wider adoption

---

## 🔄 Related Literature Foundations

This research builds on established concepts:

### Enterprise Security Models [NIST, Karambelkar]

- Multi-layer defense is industry standard
- Firewall + IDS/IPS coordination proven effective
- Deep packet inspection catches complex threats

### Threat Evolution [Alshamrani, Palo Alto]

- Modern attacks use encryption and legitimate ports
- Traditional firewalls insufficient for APT, C2 detection
- Behavioral analysis needed for new threat types

### Hybrid Detection [Garcia-Teodoro, Sommer]

- Signature + anomaly detection better than either alone
- Machine learning can improve detection accuracy
- Lightweight algorithms work for resource-constrained environments

---

## 📅 Project Timeline

| Phase | Objective                 | Duration | Owner | Status      |
| ----- | ------------------------- | -------- | ----- | ----------- |
| 1     | Introduction & Literature | Week 1   | My    | ✅ Done     |
| 2     | Problem Definition        | Week 2   | Hoa   | 🔄 Active   |
| 3     | Setup & Implementation    | Week 2-3 | Bình  | 🔄 Active   |
| 4     | Testing & Results         | Week 3-4 | Yến   | 🔄 Active   |
| 5     | Analysis & Documentation  | Week 4-5 | All   | ⏳ Upcoming |
| 6     | Final Presentation        | Week 5   | All   | ⏳ Upcoming |

---

## ✅ Validation Plan

### How We'll Verify Success

1. **Malware Test**
   - ✅ Flightsim generates C2 traffic
   - ✅ Npcap captures all packets
   - ✅ Snort alerts on suspicious patterns
   - ✅ Logs show timestamps and details

2. **Brute-Force Test**
   - ✅ Simulate multiple login attempts
   - ✅ Monitor Snort for pattern detection
   - ✅ Verify automatic IP blocking
   - ✅ Measure response time

3. **Port Scan Test**
   - ✅ Run port scanner against desktop
   - ✅ Verify early detection by IDS
   - ✅ Measure detection latency

4. **Metric Verification**
   - ✅ Calculate detection rates
   - ✅ Count false positives
   - ✅ Measure system resource usage
   - ✅ Compare baseline vs. protected

---

**Last Updated:** May 4, 2026  
**Research Status:** Objective Definition Complete ✅
