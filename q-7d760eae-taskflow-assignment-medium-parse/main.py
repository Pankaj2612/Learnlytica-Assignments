import csv
import io


def parse_tasks_csv(csv_text):
    if not csv_text or not csv_text.strip():
        return []
    reader = csv.DictReader(io.StringIO(csv_text))

    out = []
    for row in reader:
        if  row is None or row.get('id').strip() == "":
            continue 
        # TODO: skip rows with a blank id
        # TODO: build a typed dict (int id, stripped title, int/0 points, bool done)
        row['id'] = int(row.get('id'))
        row['title'] = row.get('title').strip()
        if row.get('points').strip() == '':
            row['points'] = 0
        else:    
            row['points'] = int(row.get('points'))

        if row.get('done').strip().lower() == "true":
            row['done'] = True
        else:
            row['done'] = False 
        out.append(row)
    return out

