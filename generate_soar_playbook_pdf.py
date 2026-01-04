from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black
import os

# Define the output path
output_dir = "AEGIS_Official_Docs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = os.path.join(output_dir, "AEGIS_SOC_Playbooks_SOAR_Automation.pdf")

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name="TitleStyle", fontSize=22, textColor=HexColor("#C62828"), spaceAfter=20))
styles.add(ParagraphStyle(name="HeaderStyle", fontSize=15, spaceAfter=12))
styles.add(ParagraphStyle(name="BodyStyle", fontSize=11, leading=15, spaceAfter=10))

content = []

content.append(Paragraph("AEGIS SOC Playbooks", styles["TitleStyle"]))
content.append(Paragraph("SOAR & Security Automation Manual", styles["BodyStyle"]))
content.append(Spacer(1, 20))

content.append(Paragraph("1. Purpose & Scope", styles["HeaderStyle"]))
content.append(Paragraph(
    "This document defines automated Security Orchestration, Automation, and Response (SOAR) "
    "playbooks implemented within the AEGIS Cyber Intelligence Platform to ensure rapid, consistent, "
    "and intelligence-driven incident response.",
    styles["BodyStyle"]
))

content.append(Paragraph("2. SOAR Architecture Overview", styles["HeaderStyle"]))
content.append(Paragraph(
    "AEGIS SOAR integrates detection engines, decision logic, automation actions, and human approval "
    "gates. Playbooks are triggered by AI, UEBA, network analytics, or threat intelligence correlation.",
    styles["BodyStyle"]
))

content.append(PageBreak())

content.append(Paragraph("3. Core SOC Playbooks", styles["HeaderStyle"]))

table_data = [
    ["Attack Type", "Trigger", "Automated Actions", "Outcome"],
    ["Phishing", "AI Email Detection", "Quarantine, User Alert, IOC Sharing", "Threat Contained"],
    ["Ransomware", "Behavioral Encryption Spike", "Host Isolation, Process Kill", "Spread Prevented"],
    ["Brute Force", "Login Failure Anomaly", "Account Lock, IP Block", "Access Secured"],
    ["DDoS", "Traffic Surge Baseline Break", "Rate Limit, Sinkhole", "Service Stabilized"],
    ["Insider Threat", "UEBA Deviation", "Access Revocation, Case Creation", "Data Loss Prevented"],
    ["DNS Tunneling", "Entropy Detection", "Domain Block, Forensics", "C2 Disrupted"],
    ["Advanced APT", "Swarm Intel / Quantum Stealth", "Deception Activation, Traceback", "Threat Neutralized"],
]

table = Table(table_data, colWidths=[80, 120, 180, 100])
table.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 1, black),
    ('BACKGROUND', (0,0), (-1,0), HexColor("#F2F2F2")),
]))
content.append(table)

content.append(PageBreak())

content.append(Paragraph("4. Automation Levels", styles["HeaderStyle"]))
content.append(Paragraph(
    "• Level 1: Alert Enrichment & Correlation\n"
    "• Level 2: Automated Containment\n"
    "• Level 3: Autonomous Response\n"
    "• Level 4: Self-Learning Playbook Optimization",
    styles["BodyStyle"]
))

content.append(Spacer(1, 20))
content.append(Paragraph("5. Governance & Audit", styles["HeaderStyle"]))
content.append(Paragraph(
    "All actions are logged, auditable, and compliant with ISO 27001, NIST, and SOC standards. "
    "Human-in-the-loop controls are enforced where required.",
    styles["BodyStyle"]
))

content.append(Spacer(1, 30))
content.append(Paragraph("© 2025 AEGIS Cyber Intelligence Platform", styles["BodyStyle"]))

doc.build(content)

print(f"PDF generated successfully at: {file_path}")
