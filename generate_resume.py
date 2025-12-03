#!/usr/bin/env python3
"""
Resume Generator Script
Generates a professional 2-page PDF resume from experience and portfolio data
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor

def create_resume():
    """Generate a 2-page PDF resume"""
    
    # Create PDF
    pdf_path = "resume.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#666666'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Section heading style
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#0066cc'),
        spaceAfter=6,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=HexColor('#0066cc'),
        borderPadding=0,
        leftIndent=0
    )
    
    # Subsection heading style
    subsection_style = ParagraphStyle(
        'SubsectionHeading',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=HexColor('#333333'),
        spaceAfter=4,
        spaceBefore=4,
        fontName='Helvetica-Bold'
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#333333'),
        spaceAfter=4,
        alignment=TA_LEFT,
        fontName='Helvetica',
        leading=11
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#333333'),
        spaceAfter=2,
        leftIndent=12,
        bulletIndent=0,
        fontName='Helvetica',
        leading=10
    )
    
    # Header
    elements.append(Paragraph("Dan Gibson", title_style))
    elements.append(Paragraph("Senior Drupal Developer/Architect | Senior Full-Stack Developer | DevOps Engineer | AI Solutions Architect", subtitle_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Professional Summary
    elements.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    summary = """Accomplished Full-Stack Developer and DevOps Engineer with 15+ years of experience delivering enterprise-scale 
    web applications, cloud infrastructure, and AI-powered solutions. Expert in Drupal CMS (6-10), Angular, Docker, CI/CD automation, 
    AWS, API security, and system administration. Proven track record leading complex migrations, architecting scalable systems, 
    and implementing cutting-edge technologies including Llama AI models, OAuth 2.0 security, and comprehensive testing frameworks. 
    Specialized in federal government and healthcare sectors with deep expertise in WCAG compliance, security hardening, and 
    performance optimization."""
    elements.append(Paragraph(summary, body_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Core Technical Competencies
    elements.append(Paragraph("CORE TECHNICAL COMPETENCIES", section_style))
    
    competencies = [
        "<b>Web Development:</b> Drupal 6-10 | Angular 2-16+ | React | jQuery | TypeScript | PHP | Node.js | RESTful APIs | GraphQL | JSON:API",
        "<b>DevOps & Infrastructure:</b> Docker (Lando/Docksal) | Kubernetes | Jenkins | GitHub Actions | Terraform | Ansible | AWS (EC2, RDS, S3, Lambda, CloudWatch) | Azure | Linux Administration (Ubuntu, CentOS, RHEL)",
        "<b>CI/CD & Automation:</b> Jenkins Pipelines | GitHub Actions | GitLab CI | Acquia Pipelines | Bash/Shell Scripting | Infrastructure as Code | Automated Deployment",
        "<b>Security:</b> OAuth 2.0 | OpenID Connect | JWT | API Security | SimpleSAMLphp | SAML 2.0 | SSL/TLS | fail2ban | iptables | Security Hardening",
        "<b>Testing & QA:</b> Behat (BDD) | Playwright | Cypress | K6 | JMeter | Gatling | Load Testing | Performance Testing | Integration Testing",
        "<b>Databases:</b> MySQL | PostgreSQL | MariaDB | MongoDB | Redis | Memcached | Query Optimization | Replication",
        "<b>AI & Machine Learning:</b> Llama 2/3 | Code Llama | LangChain | LlamaIndex | RAG Architecture | Model Fine-tuning | Ollama",
        "<b>Monitoring & Observability:</b> Prometheus | Grafana | ELK Stack | Datadog | New Relic | CloudWatch | Nagios"
    ]
    
    for comp in competencies:
        elements.append(Paragraph(f"• {comp}", bullet_style))
    
    elements.append(Spacer(1, 0.1*inch))
    
    # Key Technical Expertise (Highlights)
    elements.append(Paragraph("KEY TECHNICAL EXPERTISE", section_style))
    
    expertise_items = [
        ("<b>Drupal CMS Mastery:</b>", "Enterprise-level implementations covering Drupal 6-10. Expert in complex migrations, custom module/theme development, API integrations, SSO via SimpleSAML, and USWDS/Bootstrap theming."),
        ("<b>System Administration & DevOps:</b>", "15+ years managing production Linux infrastructure (Ubuntu, CentOS, RHEL). Expert in LAMP/LEMP stacks, performance tuning, security hardening, backup/disaster recovery, and achieving 99.99% uptime."),
        ("<b>API Security Implementation:</b>", "Architected OAuth 2.0/OIDC authentication systems, JWT-based APIs, zero-trust security architectures, and achieved PCI DSS compliance. Reduced unauthorized access by 95%."),
        ("<b>CI/CD Pipeline Architecture:</b>", "Built Jenkins and GitHub Actions pipelines reducing deployment time by 70-90%. Implemented automated testing, security scanning, and zero-downtime deployments."),
        ("<b>Performance & Load Testing:</b>", "Conducted comprehensive testing with K6, JMeter, Gatling. Reduced response times by 60% and validated 10x peak traffic capacity. Expert in profiling, optimization, and bottleneck resolution."),
        ("<b>AI Solutions Development:</b>", "Deployed Llama AI models (2/3/Code Llama) for enterprise knowledge assistants, code review automation, and content generation. Built RAG systems with LangChain/LlamaIndex achieving 95%+ accuracy."),
    ]
    
    for title, desc in expertise_items:
        elements.append(Paragraph(f"<b>•</b> {title} {desc}", bullet_style))
    
    elements.append(Spacer(1, 0.15*inch))
    
    # PAGE 2 - Portfolio & Additional Experience
    elements.append(Paragraph("CLIENT PORTFOLIO & EXPERIENCE", section_style))
    
    # Portfolio entries (condensed)
    portfolio = [
        ("Quantum Improvements Consulting, LLC", "8(m) woman-owned small business specializing in training solutions. Delivered research-based solutions enhancing human performance for government clients."),
        ("Federal Aviation Administration (FAA)", "Developed and maintained mission-critical web applications for air traffic management and aviation safety systems."),
        ("Centers for Medicare & Medicaid Services (CMS)", "Built healthcare applications managing Medicare, Medicaid, and CHIP programs. Implemented HIPAA-compliant solutions with stringent security requirements."),
        ("USPS Office of Inspector General", "Delivered oversight and audit systems ensuring efficiency, accountability, and integrity of postal operations."),
        ("State of South Carolina", "Developed state government portals and services supporting education, public safety, transportation, and healthcare initiatives."),
        ("ICF Next", "Global marketing and communications agency. Delivered digital transformation projects and customer engagement platforms."),
        ("MITRE Corporation", "Built systems for federally funded research and development centers supporting national security, cybersecurity, and aviation."),
        ("U.S. House of Representatives", "Developed legislative systems and internal applications for congressional operations and public transparency."),
        ("IBM", "Enterprise technology solutions involving cloud computing, AI integration, and legacy system modernization."),
        ("Northrop Grumman Corporation", "Aerospace and defense technology applications. Delivered secure, mission-critical systems for military operations."),
        ("The InterAgency Board", "Emergency preparedness and response systems. Developed platforms for equipment standardization and interoperability across agencies."),
        ("U.S. Department of Energy (DOE)", "Built energy policy and nuclear infrastructure management systems. Implemented clean energy technology platforms."),
        ("Communications Training Analysis Corp (CTAC)", "Technology solutions provider for government digital transformation. Delivered cloud-native, scalable IT services."),
        ("Chenega Government Consulting, LLC", "Alaska Native Corporation subsidiary. Developed IT solutions for federal civilian agencies."),
        ("Energy Enterprise Solutions, LLC", "Systems integrator for federal government. Delivered IT infrastructure, cybersecurity, and systems engineering solutions."),
        ("Booz Allen Hamilton", "Leading consulting firm. Developed management and technology solutions for defense, intelligence, and civil sectors."),
    ]
    
    for org, desc in portfolio:
        elements.append(Paragraph(f"<b>{org}:</b> {desc}", bullet_style))
    
    elements.append(Spacer(1, 0.1*inch))
    
    # Additional Technical Areas
    elements.append(Paragraph("ADDITIONAL TECHNICAL AREAS", section_style))
    
    additional_areas = [
        ("<b>Bash/Shell Scripting:</b>", "Advanced automation for CI/CD, deployment orchestration, system administration, and data processing. Created hundreds of production scripts."),
        ("<b>Docker & Containerization:</b>", "Expert with Lando/Docksal for local development. Orchestrated production containers with Kubernetes, Docker Swarm, and AWS ECS."),
        ("<b>Database Administration:</b>", "MySQL/PostgreSQL management including replication, backup strategies, query optimization, and high-availability configurations."),
        ("<b>Networking & Load Balancing:</b>", "Configured HAProxy, Nginx load balancers, VPNs (OpenVPN, WireGuard), and managed DNS for high-availability setups."),
        ("<b>Monitoring & Alerting:</b>", "Deployed Prometheus, Grafana, Nagios, Zabbix, and ELK Stack. Built real-time dashboards and integrated PagerDuty/Slack alerting."),
        ("<b>Frontend Frameworks:</b>", "Angular (2-16+), React, jQuery. Built SPAs, headless CMS frontends, and progressive web applications with advanced state management."),
    ]
    
    for title, desc in additional_areas:
        elements.append(Paragraph(f"<b>•</b> {title} {desc}", bullet_style))
    
    elements.append(Spacer(1, 0.1*inch))
    
    # Certifications & Methodologies
    elements.append(Paragraph("METHODOLOGIES & STANDARDS", section_style))
    methodologies = [
        "Agile/Scrum Development | DevOps/GitOps Practices | Infrastructure as Code (IaC)",
        "WCAG 2.1 AA/AAA Accessibility Compliance | Section 508 Standards | 21st Century IDEA Act",
        "GDPR, HIPAA, PCI DSS Compliance | CIS Benchmarks | NIST Cybersecurity Framework",
        "API-First Architecture | Microservices | RESTful Design Principles | Headless CMS",
        "Test-Driven Development (TDD) | Behavior-Driven Development (BDD) | Continuous Testing"
    ]
    
    for method in methodologies:
        elements.append(Paragraph(f"• {method}", bullet_style))
    
    elements.append(Spacer(1, 0.1*inch))
    
    # Professional Highlights
    elements.append(Paragraph("PROFESSIONAL HIGHLIGHTS", section_style))
    highlights = [
        "Led Drupal 6/7/8 to Drupal 9/10 migration projects preserving data integrity across 50+ sites",
        "Architected API-first Drupal applications consumed by Angular, React, and mobile applications",
        "Implemented enterprise SSO solutions integrating SimpleSAMLphp with Shibboleth, SAML2, and ADFS",
        "Built RAG-powered AI assistants enabling natural language queries of internal documentation and knowledge bases",
        "Configured comprehensive security hardening including fail2ban, iptables, SELinux, and intrusion detection systems",
        "Automated database backup routines with encryption achieving compliance with federal data protection standards",
        "Developed custom Drupal modules for workflow automation, API endpoints, and third-party integrations (Salesforce, Azure)",
        "Conducted load testing validating system capacity to handle 10x peak traffic during high-profile campaigns"
    ]
    
    for highlight in highlights:
        elements.append(Paragraph(f"• {highlight}", bullet_style))
    
    elements.append(Spacer(1, 0.15*inch))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#666666'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    elements.append(Paragraph("References and detailed project portfolios available upon request", footer_style))
    
    # Build PDF
    doc.build(elements)
    print(f"Resume generated successfully: {pdf_path}")

if __name__ == "__main__":
    create_resume()
