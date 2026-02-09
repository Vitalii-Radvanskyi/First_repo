from pathlib import Path

def get_cats_info(path):
    cats_info = []
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError
    with path.open(encoding='utf-8') as file:
        for line in file:
            try:
                cat_id, name, age =line.strip().split(',')
                cats_info.append({"cat_id":cat_id, "name":name, 'age':int(age)})
            except ValueError:
                continue
    return cats_info        
    

print(get_cats_info('test.txt'))