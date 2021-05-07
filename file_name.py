file_name=input("Input the filename: ")
ext = file_name.split('.')
if ext[1] == 'py':
    op='python'
else:
    op='not python'
print(f'The extension of the file is: {op} ')
