from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def create_report(summary,
                  keywords):

    filename = "analysis_report.pdf"

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Research Paper Analysis",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1,12)
    )

    elements.append(
        Paragraph(
            "Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1,12)
    )

    elements.append(
        Paragraph(
            "Keywords",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            ", ".join(keywords),
            styles["BodyText"]
        )
    )

    pdf.build(elements)

    return filename
