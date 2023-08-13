import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione a pasta a ser organizada')
lista_arquivos = os.listdir(caminho)
locais = {
    'IMAGENS': ['jpg', 'png', 'jpeg', 'gif', 'bmp', 'svg'],
    'PLANILHAS': ['xlsx', 'xls', 'csv'],
    'APRESENTAÇÕES': ['pptx', 'ppt', 'pps', 'ppsx'],
    'DOCUMENTOS DE TEXTO': ['docx', 'doc', 'odt', 'txt', 'pdf'],
    'MÚSICAS': ['mp3', 'wav', 'wma', 'aac', 'ogg', 'flac'],
    'VÍDEOS': ['mp4', 'avi', 'wmv', 'mov', 'flv', 'mkv', 'webm'],
    'COMPACTADOS': ['zip', 'rar', '7z', 'tar', 'gz', 'pkg', 'deb'],
    'PROGRAMAS': ['exe', 'msi'],
    'ANDROID': ['apk'],
    'ISO': ['iso'],
    'IMAGENS DE DISCO': ['img', 'dmg'],
    'FIGMA': ['fig'],
    'ADOBE ILLUSTRATOR': ['ai'],
    'ADOBE PHOTOSHOP': ['psd'],
    'ADOBE XD': ['xd'],
    'ADOBE INDESIGN': ['indd'],
    'ADOBE PREMIERE': ['prproj'],
    'ADOBE AFTER EFFECTS': ['aep'],
    'ADOBE AUDITION': ['sesx'],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    extensao = extensao[1:]  # Removendo o ponto do início da extensão
    for pasta, extensoes in locais.items():
        if extensao in extensoes:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            break  # Uma vez que o arquivo foi movido, não precisamos verificar as outras pastas

print('Organização concluída!')
