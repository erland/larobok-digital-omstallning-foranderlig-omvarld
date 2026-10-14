#!/usr/bin/env python3
import sys,yaml
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else '.');data=yaml.safe_load((p/'book.yaml').read_text())
assert data['book_kind']=='factbook'
assert data['author'] and data['title']
assert len(data['chapters'])==18, 'Förväntar inledning, 16 kapitel och källregister'
assert data['chapters'][0]=='chapters/00-inledning.md'
assert data['chapters'][-1]=='chapters/17-kallor-och-lasanvisning.md'
assert [int(Path(x).name[:2]) for x in data['chapters'][1:-1]]==list(range(1,17))
if data.get('cover_image'):
    assert (p/data['cover_image']).is_file(), 'Omslagsbild saknas' 
for item in data['chapters']:assert (p/item).exists(),item
assert (p/'docs/kallpolicy.md').exists()
print('PASS: bokprofil, metadata, kapitelordning och obligatoriska dokument')
