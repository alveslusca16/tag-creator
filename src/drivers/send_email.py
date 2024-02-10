import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


def read_first_image_name():
    # Listar arquivos no diretório atual
    arquivos_no_diretorio = os.listdir(os.getcwd())

    # Filtrar apenas arquivos de imagem (por exemplo, com extensão .png)
    imagens = [
        arquivo for arquivo in arquivos_no_diretorio if arquivo.lower().endswith(('.png'))]

    # Verificar se há pelo menos uma imagem no diretório
    if imagens:
        # Obter o nome da primeira imagem encontrada
        primeiro_nome_de_imagem = imagens[0]
        return primeiro_nome_de_imagem

    print("No images found in the directory.")
    return None


def send_email(barcode):
    corpo_email = """
    <p>Hello,</p>
    <p>Attached is the photo.</p>
    """

    # Configuração da mensagem multipart para suportar texto, imagem e anexo
    msg = MIMEMultipart()
    msg['Subject'] = "Subject"
    msg['From'] = 'emailhere@gmail.com'  # sender's email
    msg['To'] = 'emailhere@gmail.com'  # recipient's email
    password = '#### #### #### ####'  # Your app password

    # Adiciona o corpo do e-mail como HTML
    msg.attach(MIMEText(corpo_email, 'html'))

    # Anexa a foto
    with open(barcode, 'rb') as photo:
        img = MIMEImage(photo.read())
        img.add_header('Content-Disposition',
                       'attachment', filename='barcode.png')
        msg.attach(img)

    # Conecta ao servidor SMTP e envia o e-mail
    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        return None
    except Exception as e:
        print(f"Error to send email: {str(e)}")
        return None
