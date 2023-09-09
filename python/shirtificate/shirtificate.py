from fpdf import FPDF

def main():

    class PDF(FPDF):
        def header(self):
            # Rendering logo:
            self.image("shirtificate.png", 10, 8, 33)
            # Setting font: helvetica bold 15
            self.set_font("helvetica", "B", 40)
            # Printing title:
            self.cell(0, 10, "CS50 Shirtificate", align="C")
            # Performing a line break:
            self.ln(20)

        def footer(self):
            # Position cursor at 1.5 cm from bottom:
            self.set_y(-15)
            # Setting font: helvetica italic 8
            self.set_font("helvetica", "I", 25)
            # Printing page number:
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


    # Instantiation of inherited class
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    name = input("Name: ")
    pdf.cell(0, 10, f"{name}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("new_shirtificate.pdf")




if __name__ == "__main__":
    main()