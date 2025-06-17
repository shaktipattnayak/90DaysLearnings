# Fallback: generate PDF using ReportLab since docx2pdf isn't available
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

# Define path for PDF
pdf_path = "/mnt/data/Mock_Interview_Questions_Senior_Automation_Engineer.pdf"

# Initialize PDF
c = canvas.Canvas(pdf_path, pagesize=LETTER)
width, height = LETTER

# Text configuration
x, y = 40, height - 40
line_height = 14

# Title
c.setFont("Helvetica-Bold", 14)
c.drawString(x, y, "Mock Interview Questions – Senior Automation Engineer (Based on JD)")
y -= 30

# Content
sections = {
    "Python & Programming": [
        "Explain how you use Python to write reusable and maintainable test automation code.",
        "What are decorators in Python? Can you give a use case from automation?",
        "How would you manage test data in a Python-based framework?"
    ],
    "Selenium & UI Automation": [
        "How do you structure your Selenium automation project? Explain the Page Object Model.",
        "What strategies do you follow to handle dynamic elements in Selenium?",
        "Have you integrated Selenium tests into CI pipelines? How did you handle flaky tests?"
    ],
    "Robot Framework": [
        "What are the benefits of using Robot Framework over traditional Selenium?",
        "How do you structure test cases and custom keywords in Robot Framework?",
        "Can you explain how to integrate REST API testing into Robot Framework?"
    ],
    "API & Backend Testing": [
        "How do you validate API responses beyond status codes?",
        "What tools or libraries do you use for automating API tests in Python?",
        "Have you worked with Snowflake, Hive, or Athena for backend validation? Give examples."
    ],
    "CI/CD, Git, and DevOps": [
        "Explain how you integrate your automation suite with GitHub Actions or Jenkins.",
        "How do you manage test execution inside Docker containers?",
        "What is your process for handling merge conflicts during a sprint release?"
    ],
    "Soft Skills & Team Collaboration": [
        "How do you mentor junior QA engineers?",
        "Describe a situation where you had to push back on a tight deadline to ensure quality.",
        "How do you handle conflicts in cross-functional Agile teams?"
    ],
    "Scenario-Based & Architecture": [
        "You join a team with no automation. What’s your 30-day plan to set up automation from scratch?",
        "How do you ensure your automation framework scales across multiple services or teams?",
        "How do you prioritize what to automate in a fast-paced release environment?"
    ]
}

c.setFont("Helvetica-Bold", 12)
for section, questions in sections.items():
    if y < 80:
        c.showPage()
        y = height - 40
    c.drawString(x, y, section)
    y -= 20
    c.setFont("Helvetica", 10)
    for q in questions:
        if y < 60:
            c.showPage()
            y = height - 40
        c.drawString(x + 20, y, f"• {q}")
        y -= line_height
    c.setFont("Helvetica-Bold", 12)
    y -= 10

c.save()
pdf_path
