from pathlib import Path
from datetime import datetime

path = Path('files', 'dados2', 'teste.txt')

#print(path.stat())

stats = path.stat()
second_created = stats.st_birthtime
date_created = datetime.fromtimestamp(second_created)
#print(date_created)
date_created_str = date_created.strftime('%d/%m/%Y %H:%M:%S')
print(date_created_str)


#st_ctime=1736298994