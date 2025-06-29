# Dentro do ficheiro: gerador_pdf.py

# Primeiro, importamos a ferramenta que este trabalhador precisa
from fpdf import FPDF

# Agora, definimos a função que fará o trabalho
def criar_boletim_pdf(nome, notas, media, situacao):
    pdf = FPDF()
    pdf.add_page()

    # Título
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt='Boletim Escolar', ln=1, align='C')

    # Espaçamento
    pdf.ln(10) 

    # Conteúdo
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Aluno: {nome}", ln=1)
    pdf.cell(200, 10, txt=f"Notas: {str(notas)}", ln=1)
    pdf.cell(200, 10, txt=f"Média Final: {str(media)}", ln=1)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, txt=f"Situação: {situacao}", ln=1)

    # Salvar o ficheiro
    nome_do_ficheiro = f"boletim_{nome}.pdf"
    pdf.output(nome_do_ficheiro)
    print(f"\nPDF '{nome_do_ficheiro}' gerado com sucesso!")