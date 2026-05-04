# Project Documentation Index

## 📚 Complete Documentation Map

This file serves as a guide to all project documentation for easy navigation.

---

## 🎯 Start Here

### For Quick Overview

1. **[README.md](README.md)** - Main project overview, quick status, and navigation
   - Project abstract and summary
   - Team members and roles
   - Current status and progress
   - Key findings at a glance

---

## 📖 Main Documentation Files

### 1. **[README.md](README.md)** - Project Overview ⭐

- Executive summary
- Project objectives
- Team structure
- Technical architecture overview
- Current project status
- Quick reference table of contents

**When to use:** Starting point for anyone new to the project

---

### 2. **[OBJECTIVES.md](OBJECTIVES.md)** - Goals & Research Questions 🎯

- 4 primary objectives with detailed breakdowns
- 5 key research questions
- Test scenarios description
- Success metrics and validation plan
- Educational outcomes
- Literature foundations

**When to use:** Understanding what we're trying to achieve and why

---

### 3. **[TEAM_ROLES.md](TEAM_ROLES.md)** - Team Organization & Responsibilities 👥

- Individual team member roles
- Phase-by-phase responsibilities
- Current status of each team member
- Expected deliverables
- Presentation flow
- Success criteria for each phase

**When to use:** Understanding who does what and current progress

---

### 4. **[TECHNICAL_SETUP.md](TECHNICAL_SETUP.md)** - System Architecture & Implementation 🏗️

- Complete system architecture diagram
- Component details and configuration
- Windows Defender Firewall setup
- Npcap packet capture configuration
- Snort IDS/IPS engine details
- Custom Snort rules (complete rule sets)
- Test scenario execution steps
- Log file locations

**When to use:** Technical implementation details and configuration

---

### 5. **[EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)** - Test Results & Findings 🔬

- Current testing status for each attack type
- Malware (Flightsim) detection results
- Brute-force testing status
- Port scanning detection status
- Alert examples and log formats
- Expected vs. actual findings
- System performance observations

**When to use:** Viewing test results and experiment progress

---

### 6. **[INDEX.md](INDEX.md)** - Documentation Guide (this file) 📋

- Complete documentation map
- File descriptions and purposes
- Navigation guide

**When to use:** Finding specific information in the project

---

## 🔍 How to Find Information

### By Topic

**Project Planning & Goals**

- What are our objectives? → [OBJECTIVES.md](OBJECTIVES.md)
- What's the project status? → [README.md](README.md)
- What are success criteria? → [OBJECTIVES.md](OBJECTIVES.md#success-metrics)

**Team & Organization**

- Who's doing what? → [TEAM_ROLES.md](TEAM_ROLES.md)
- What's my responsibility? → [TEAM_ROLES.md](TEAM_ROLES.md)
- What's the project timeline? → [OBJECTIVES.md](OBJECTIVES.md#project-timeline)

**Technical Details**

- How is the system architected? → [TECHNICAL_SETUP.md](TECHNICAL_SETUP.md)
- What tools do we use? → [README.md](README.md) or [TECHNICAL_SETUP.md](TECHNICAL_SETUP.md)
- What are the Snort rules? → [TECHNICAL_SETUP.md](TECHNICAL_SETUP.md#snort-custom-rules)
- Where are logs stored? → [TECHNICAL_SETUP.md](TECHNICAL_SETUP.md#log-file-locations)

**Experiment & Results**

- What tests are we running? → [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)
- What are the test results? → [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)
- What's the current status? → [EXPERIMENT_LOG.md](EXPERIMENT_LOG.md)

---

## 📑 Document Relationships

```
README.md (Overview & Navigation Hub)
    ↓
    ├→ OBJECTIVES.md (What we want to achieve)
    │   └→ TEAM_ROLES.md (Who achieves it)
    │       └→ TECHNICAL_SETUP.md (How we do it)
    │           └→ EXPERIMENT_LOG.md (What we found)
    │
    └→ TECHNICAL_SETUP.md (System design)
        └→ EXPERIMENT_LOG.md (Actual results)
```

---

## 🗂️ File Organization

```
/Users/munonguyen/Security/
├── README.md                    ← Start here
├── OBJECTIVES.md                ← Project goals
├── TEAM_ROLES.md               ← Team structure
├── TECHNICAL_SETUP.md          ← Implementation guide
├── EXPERIMENT_LOG.md           ← Test results
├── INDEX.md                    ← This file
└── .git/                       ← Git repository
```

---

## 📌 Quick Reference

### Project At A Glance

- **Title:** Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop
- **Institution:** Hanoi University, Faculty of Information Technology
- **Course:** Network Security
- **Instructor:** Đoàn Trung Sơn
- **Team:** 4 students (My, Hoa, Bình, Yến)
- **Status:** In Progress
- **Created:** May 4, 2026

### Key Numbers

- **4** Primary Objectives
- **5** Research Questions
- **3** Attack Scenarios
- **4** Main Tools
- **14** References
- **4** Team Members

### Success Targets

- Detection Rate: >90%
- Blocking Rate: 70-100%
- False Positives: <2%
- Response Time: <1 second

---

## 🔗 Related Links

### Internal References

- All markdown files are cross-linked for easy navigation
- Use `[Link Text](filename.md)` format throughout
- GitHub repository: https://github.com/munonguyen/Appying-FireWalls-and-IDS-IPS-Systems-to-Enhance-Network-Security-on-a-Personal-Desktop

### External References

- Tool Documentation:
  - Snort: https://www.snort.org/
  - Npcap: https://npcap.org/
  - Flightsim: Kansa research tool
- Academic References:
  - All 14 citations in references sections

---

## 📝 How to Add New Documentation

1. Create new `.md` file with descriptive name
2. Add entry to this INDEX.md
3. Link from README.md if top-level
4. Update cross-references in existing files
5. Commit to git with clear message

---

## ✅ Documentation Checklist

- [x] README.md - Main overview
- [x] OBJECTIVES.md - Goals and metrics
- [x] TEAM_ROLES.md - Team organization
- [x] TECHNICAL_SETUP.md - Implementation details
- [x] EXPERIMENT_LOG.md - Test results
- [x] INDEX.md - Documentation guide

---

## 📋 For Different Audiences

### For Instructors

Start with: README.md → OBJECTIVES.md → TEAM_ROLES.md

### For Team Members

Start with: TEAM_ROLES.md → Your phase documentation → EXPERIMENT_LOG.md

### For Developers/Implementers

Start with: TECHNICAL_SETUP.md → EXPERIMENT_LOG.md

### For Results Analysts

Start with: EXPERIMENT_LOG.md → TECHNICAL_SETUP.md (rules/setup reference)

### For New Team Members

Start with: README.md → TEAM_ROLES.md → Specific phase docs

---

**Last Updated:** May 4, 2026  
**Documentation Status:** Complete ✅
