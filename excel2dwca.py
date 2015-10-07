#Created by Raul S. Ferreira raulsf@cos.ufrj.br
import subprocess
from pprint import pprint as pp

# deve ser trocado por endereco do arquivo a ser modificado e arquivo destino
file = "TESTE.xlsx result.csv"

#chama o shell e converte planilha para csv
argument = 'ssconvert {0}'.format(file)
command_process = subprocess.call([argument], shell=True)
#pp(command_process)