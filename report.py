# report.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

def create_report(summary,
                  keywords):

    pdf = SimpleDocTemplate(
        "analysis_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "<b>Summary</b>",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(summary,
                  styles["BodyText"])
    )

    content.append(
        Paragraph(
            "<br/><b>Keywords</b>",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            ", ".join(keywords),
            styles["BodyText"]
        )
    )

    pdf.build(content)

    return "analysis_report.pdf"