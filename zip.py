import zipfile

zip_files = ['teste.docx','teste.txt', 'teste.xlsx' ]

with zipfile.ZipFile('zip_with_python.zip','w') as zipF:
    for file in zip_files:
        zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)


print("Files zipped sucefully")