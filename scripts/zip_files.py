# заархивировать файлы
import zipfile

files = ['file1.txt', 'file2.txt']
with zipfile.ZipFile('pycl.zip', 'w') as zipf:
  for file in files:
    zipf.write(file)

print("ZIP file created!")

