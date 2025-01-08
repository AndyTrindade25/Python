from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
    if path.is_file():
        stats = path.stat()
        #print(stats.st_birthtime)
        second_created = stats.st_birthtime
        date_created = datetime.fromtimestamp(second_created)

        date_created_str = date_created.strftime('%d-%m-%Y_%H_%m')
        #print(date_created_str)

        new_filename = f"{date_created_str}-{path.name}"
        #print(new_filename)

        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)