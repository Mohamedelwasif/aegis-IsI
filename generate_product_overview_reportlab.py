from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
import os

# Ensure directory exists
output_dir = "AEGIS_Official_Docs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = os.path.join(output_dir, "AEGIS_Product_Overview.pdf")

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="TitleStyle",
    fontSize=24,
    textColor=HexColor("#00C2FF"),
    spaceAfter=20
))

styles.add(ParagraphStyle(
    name="HeaderStyle",
    fontSize=16,
    textColor=HexColor("#05070F"),
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name="BodyStyle",
    fontSize=11,
    leading=15,
    spaceAfter=10
))

content = []

content.append(Paragraph("AEGIS", styles["TitleStyle"]))
content.append(Paragraph("Intelligent Shield for Unified Cyber Defense", styles["BodyStyle"]))
content.append(Spacer(1, 20))

content.append(Paragraph("Product Overview", styles["HeaderStyle"]))
content.append(Paragraph(
    "AEGIS is an advanced cyber intelligence and autonomous defense platform designed "
    "to provide full visibility, detection, response, and compliance across complex enterprise "
    "and government networks. It combines AI-driven analytics, UEBA, SOAR automation, "
    "and cyber simulation into a single unified command platform.",
    styles["BodyStyle"]
))

content.append(Paragraph("Key Capabilities", styles["HeaderStyle"]))
content.append(Paragraph(
    "- Network Traffic Intelligence (Cisco, Aruba, Avaya, IoT)<br/>"
    "- AI & Machine Learning Detection<br/>"
    "- UEBA (User & Entity Behavior Analytics)<br/>"
    "- SOAR Automated Response<br/>"
    "- Threat Hunting & Digital Twin Simulation<br/>"
    "- Compliance & Forensics Suite",
    styles["BodyStyle"]
))

content.append(Paragraph("Target Markets", styles["HeaderStyle"]))
content.append(Paragraph(
    "• Large Enterprises<br/>"
    "• Telecom Operators<br/>"
    "• MSSP Providers<br/>"
    "• Government & Defense Organizations",
    styles["BodyStyle"]
))

content.append(PageBreak())

content.append(Paragraph("Why AEGIS?", styles["HeaderStyle"]))
content.append(Paragraph(
    "AEGIS goes beyond traditional SOC tools by acting as a cyber defense brain. "
    "It not only detects threats, but understands, simulates, and responds autonomously "
    "using its Hacker Mindset Engine and Stealth Detection Mode, "
    "reducing response times and operational costs while increasing resilience.",
    styles["BodyStyle"]
))

content.append(Paragraph("Deployment Options", styles["HeaderStyle"]))
content.append(Paragraph(
    "• On-Premise Enterprise Deployment<br/>"
    "• Cloud-Based SOC Platform<br/>"
    "• Air-Gapped Government Environments",
    styles["BodyStyle"]
))

content.append(Spacer(1, 30))
content.append(Paragraph("© 2025 AEGIS Cyber Intelligence Platform", styles["BodyStyle"]))

doc.build(content)

print(f"Generated PDF at: {file_path}")
