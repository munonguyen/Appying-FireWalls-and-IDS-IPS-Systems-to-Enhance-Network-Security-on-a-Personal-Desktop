# 📊 Project Structure & File Organization Guide

**Project:** Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop

---

## 📦 Complete Project Contents

### Repository Statistics
- **Total Files**: 18 documents
- **Total Size**: ~450 KB
- **Languages**: Python 3, Markdown, Configuration
- **Documentation**: 11 markdown files
- **Code**: 4 Python scripts + 1 config file

---

## 🗂️ File Organization

```
/Users/munonguyen/Security/
│
├── 📚 PROJECT OVERVIEW
│   ├── README.md                          (10KB) - Main project overview
│   ├── INDEX.md                           (6.6KB) - Documentation index
│   └── ATTACK_SIMULATION_DATA_SUMMARY.md  (12KB) - Complete summary
│
├── 🎯 OBJECTIVES & GOALS
│   ├── OBJECTIVES.md                      (8.3KB) - Project objectives
│   ├── TECHNICAL_SETUP.md                 (11KB) - System architecture
│   └── EXPERIMENT_LOG.md                  (4.4KB) - Experiment status
│
├── 🔴 ATTACK SIMULATION SCRIPTS
│   ├── bruteforce_ssh_attack.py           (7.4KB) - SSH brute-force
│   ├── bruteforce_rdp_attack.py           (6.7KB) - RDP brute-force
│   ├── port_scanner.py                    (7.5KB) - Port scanning tool
│   └── run_all_tests.py                   (10KB) - Test orchestrator
│
├── 📊 DATA COLLECTION & ANALYSIS
│   ├── data_collector.py                  (17KB) - Data parser & analyzer
│   ├── DATA_COLLECTION_GUIDE.md           (5.1KB) - Collection methodology
│   └── ATTACK_SIMULATION_RESULTS.md       (12KB) - Results template
│
├── 📋 EXECUTION & TESTING
│   ├── EXECUTION_WORKFLOW.md              (13KB) - Step-by-step workflow
│   ├── ATTACK_TESTING_GUIDE.md            (8.6KB) - Detailed testing guide
│   ├── BRUTEFORCE_QUICK_START.md          (5.1KB) - Quick reference
│   └── TEAM_ROLES.md                      - [In main project]
│
├── 🔧 CONFIGURATION
│   ├── snort_custom_rules.conf            (6KB) - 15 detection rules
│   └── passwords.txt                      (557B) - Password wordlist
│
└── 📁 GIT REPOSITORY
    └── .git/                              - Version control
```

---

## 📋 Quick File Reference

### By Purpose

#### Main Documentation
| File | Size | Purpose | For Whom |
|------|------|---------|---------|
| README.md | 10KB | Project overview | Everyone |
| INDEX.md | 6.6KB | Navigation guide | First time users |
| OBJECTIVES.md | 8.3KB | Research goals | Researchers |

#### Technical Guides
| File | Size | Purpose | For Whom |
|------|------|---------|---------|
| TECHNICAL_SETUP.md | 11KB | System architecture | Technical team |
| EXECUTION_WORKFLOW.md | 13KB | Complete workflow | Test executors |
| DATA_COLLECTION_GUIDE.md | 5.1KB | Data methodology | Analysts |

#### Test Execution
| File | Size | Purpose | For Whom |
|------|------|---------|---------|
| ATTACK_TESTING_GUIDE.md | 8.6KB | Detailed procedures | Testers |
| BRUTEFORCE_QUICK_START.md | 5.1KB | Quick commands | Quick start |
| EXPERIMENT_LOG.md | 4.4KB | Status tracking | Project manager |

#### Attack Tools
| File | Size | Type | Scenarios |
|------|------|------|-----------|
| bruteforce_ssh_attack.py | 7.4KB | Python | SSH attacks |
| bruteforce_rdp_attack.py | 6.7KB | Python | RDP attacks |
| port_scanner.py | 7.5KB | Python | Reconnaissance |
| run_all_tests.py | 10KB | Python | Automation |

#### Analysis Tools
| File | Size | Type | Function |
|------|------|------|----------|
| data_collector.py | 17KB | Python | Parse & analyze |
| snort_custom_rules.conf | 6KB | Config | 15 detection rules |

#### Results & Analysis
| File | Size | Purpose | For Whom |
|------|------|---------|---------|
| ATTACK_SIMULATION_RESULTS.md | 12KB | Results template | Analysts |
| ATTACK_SIMULATION_DATA_SUMMARY.md | 12KB | Complete summary | Everyone |

---

## 🚀 Finding What You Need

### "I want to run tests immediately"
→ Start with: `BRUTEFORCE_QUICK_START.md`  
→ Then use: Attack simulation scripts

### "I need to understand the project"
→ Start with: `README.md`  
→ Then read: `OBJECTIVES.md` → `TECHNICAL_SETUP.md`

### "I need step-by-step instructions"
→ Start with: `EXECUTION_WORKFLOW.md`  
→ Reference: `ATTACK_TESTING_GUIDE.md` for specifics

### "I need to analyze results"
→ Start with: `DATA_COLLECTION_GUIDE.md`  
→ Use: `data_collector.py`  
→ Record in: `ATTACK_SIMULATION_RESULTS.md`

### "I need to understand architecture"
→ Start with: `TECHNICAL_SETUP.md`  
→ Reference: System diagrams and rule specifications

### "I'm new to the project"
→ Start with: `INDEX.md`  
→ Then: `README.md` → Choose your path

---

## 🔍 Finding Information by Topic

### Attack Simulation
- How to run: `BRUTEFORCE_QUICK_START.md`, `ATTACK_TESTING_GUIDE.md`
- Code: `bruteforce_ssh_attack.py`, `bruteforce_rdp_attack.py`, `port_scanner.py`
- Orchestration: `run_all_tests.py`

### Data Collection
- Methodology: `DATA_COLLECTION_GUIDE.md`
- Implementation: `data_collector.py`
- Results template: `ATTACK_SIMULATION_RESULTS.md`

### IDS/IPS Setup
- Architecture: `TECHNICAL_SETUP.md`
- Detection rules: `snort_custom_rules.conf`
- Configuration: `TECHNICAL_SETUP.md` → "Component Details"

### Execution & Testing
- Complete workflow: `EXECUTION_WORKFLOW.md`
- Testing procedures: `ATTACK_TESTING_GUIDE.md`
- Quick start: `BRUTEFORCE_QUICK_START.md`

### Project Management
- Team roles: `TEAM_ROLES.md`
- Status: `EXPERIMENT_LOG.md`
- Progress: `README.md` → Status section

---

## 📊 Content Map

```
UNDERSTANDING THE PROJECT
    ↓
README.md (overview) → INDEX.md (navigation)
    ↓
├─ OBJECTIVES.md (goals & research questions)
├─ TECHNICAL_SETUP.md (system architecture)
└─ EXPERIMENT_LOG.md (status tracking)

EXECUTING TESTS
    ↓
EXECUTION_WORKFLOW.md (complete workflow)
    ├─ BRUTEFORCE_QUICK_START.md (quick commands)
    ├─ ATTACK_TESTING_GUIDE.md (detailed steps)
    └─ Attack Scripts (SSH, RDP, Port Scan)

COLLECTING DATA
    ↓
DATA_COLLECTION_GUIDE.md (methodology)
    └─ data_collector.py (automation)

ANALYZING RESULTS
    ↓
ATTACK_SIMULATION_RESULTS.md (template)
    └─ ATTACK_SIMULATION_DATA_SUMMARY.md (overview)
```

---

## 🔗 File Dependencies

```
README.md
├── Links to: INDEX.md
├── Links to: OBJECTIVES.md
├── Links to: TECHNICAL_SETUP.md
└── Links to: TEAM_ROLES.md

BRUTEFORCE_QUICK_START.md
├── References: bruteforce_ssh_attack.py
├── References: bruteforce_rdp_attack.py
├── References: port_scanner.py
└── References: passwords.txt

EXECUTION_WORKFLOW.md
├── Uses: All attack scripts
├── Uses: snort_custom_rules.conf
├── Uses: data_collector.py
└── Generates: test_results/

ATTACK_SIMULATION_RESULTS.md
├── Input from: All attack scripts
├── Input from: Snort logs
├── Input from: System monitoring
└── Template for: Analysis
```

---

## 💾 Data Files Explained

### passwords.txt
- **Size**: 557 bytes
- **Content**: Common passwords for brute-force testing
- **Usage**: `bruteforce_ssh_attack.py --wordlist passwords.txt`
- **Customization**: Add more passwords to `passwords.txt` as needed

### snort_custom_rules.conf
- **Size**: 6 KB
- **Content**: 15 Snort IDS detection rules
- **Coverage**: 
  - SSH brute-force (rules 3000002-3000004)
  - RDP brute-force (rules 3000005-3000007)
  - Port scanning (rules 3000008-3000013)
  - General attacks (rules 3000014-3000015)
- **Usage**: Load into Snort with `-c snort_custom_rules.conf`

---

## 📈 Output Files Generated During Testing

After running `data_collector.py`, generates:

```
test_results/
├── test_results.csv          (Test execution data)
├── snort_alerts.csv          (Parsed Snort alerts)
├── test_results.json         (Structured JSON)
├── test_report.html          (Visual HTML report)
├── attack_summary.json       (Attack summary)
└── analysis_report.txt       (Text analysis)
```

---

## 🎓 Learning Path

### For Security Researchers
1. Read: `OBJECTIVES.md` - Understand research goals
2. Study: `TECHNICAL_SETUP.md` - Learn system architecture  
3. Review: `snort_custom_rules.conf` - Understand detection rules
4. Run: Test scripts with monitoring
5. Analyze: Results using `data_collector.py`

### For Network Engineers
1. Read: `TECHNICAL_SETUP.md` - System overview
2. Study: `snort_custom_rules.conf` - Detection mechanisms
3. Execute: `EXECUTION_WORKFLOW.md` - Step-by-step
4. Monitor: `ATTACK_TESTING_GUIDE.md` - During tests
5. Analyze: `ATTACK_SIMULATION_RESULTS.md` - Results

### For Security Students
1. Start: `README.md` - Project overview
2. Learn: `OBJECTIVES.md` - Why we're doing this
3. Understand: `TECHNICAL_SETUP.md` - How it works
4. Practice: `BRUTEFORCE_QUICK_START.md` - Run tests
5. Study: `DATA_COLLECTION_GUIDE.md` - Data analysis

### For Project Managers
1. Check: `README.md` - Project status
2. Review: `TEAM_ROLES.md` - Team assignments
3. Track: `EXPERIMENT_LOG.md` - Progress
4. Monitor: `EXECUTION_WORKFLOW.md` - Timeline
5. Report: `ATTACK_SIMULATION_RESULTS.md` - Findings

---

## ✅ File Checklist

Before starting tests, verify:
- [ ] `README.md` exists (project overview)
- [ ] `OBJECTIVES.md` exists (goals clear)
- [ ] `TECHNICAL_SETUP.md` exists (architecture documented)
- [ ] Attack scripts exist and are executable
- [ ] `data_collector.py` exists (analysis tool ready)
- [ ] `snort_custom_rules.conf` exists (detection rules ready)
- [ ] `passwords.txt` exists (wordlist ready)
- [ ] `EXECUTION_WORKFLOW.md` exists (procedures documented)
- [ ] All documentation files exist (11 files)
- [ ] `.git` directory exists (version controlled)

---

## 📞 File Organization Best Practices

### For Team Collaboration
- **Keep backups**: `git push origin main`
- **Update regularly**: Commit after each phase
- **Comment code**: Python scripts have docstrings
- **Version docs**: Update version numbers in files

### For Running Tests
- **Keep organized**: Separate test results from code
- **Archive logs**: Keep raw logs for audit trail
- **Document everything**: Use `EXPERIMENT_LOG.md`
- **Version outputs**: Include date/time in filenames

### For Analysis
- **Use templates**: Fill `ATTACK_SIMULATION_RESULTS.md`
- **Export data**: Use `data_collector.py` regularly
- **Backup reports**: Keep copies of HTML/CSV outputs
- **Track changes**: Git commit after analysis

---

## 🔧 Maintenance & Updates

### Monthly Tasks
- [ ] Update Snort rules if new threats identified
- [ ] Review `EXPERIMENT_LOG.md` for new findings
- [ ] Archive old test results to `test_results_archive/`
- [ ] Update documentation with new procedures

### After Major Tests
- [ ] Export data with `data_collector.py`
- [ ] Generate HTML report
- [ ] Update `ATTACK_SIMULATION_RESULTS.md`
- [ ] Commit all changes to git
- [ ] Archive results with timestamp

### Quarterly Reviews
- [ ] Review all test data
- [ ] Update `OBJECTIVES.md` if goals change
- [ ] Refine Snort rules based on findings
- [ ] Update team role assignments
- [ ] Plan next testing cycle

---

## 📝 Documentation Standards

- **Markdown Files**: Formatted for GitHub rendering
- **Python Files**: Python 3.6+ with type hints
- **Config Files**: Commented for clarity
- **Links**: Cross-reference between files
- **Updates**: Maintain version history in git

---

## 🚀 Quick Navigation

**To view this file's location**: 
```
This file: /Users/munonguyen/Security/PROJECT_STRUCTURE.md
```

**To view all files**:
```bash
cd /Users/munonguyen/Security
ls -lah
```

**To see file count**:
```bash
find . -type f ! -path './.git/*' | wc -l
```

**To see total size**:
```bash
du -sh .
```

---

## 📊 Project Statistics

- **Python Scripts**: 4 files (~31 KB)
- **Documentation**: 11 files (~110 KB)
- **Configuration**: 1 file (~6 KB)
- **Data Files**: 1 file (~0.5 KB)
- **Total**: 18 files (~150 KB)
- **With .git**: ~450 KB

---

**Last Updated:** May 4, 2026  
**Status:** Complete ✅

Use this guide to navigate the project structure and find the information you need!
