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

# Guard against internal editorial instructions leaking into the published book.
import re
for item in data['chapters']:
    body=(p/item).read_text(encoding='utf-8')
    forbidden=[
        r'fortsatta bokarbetet',r'inför färdigställandet',
        r'inför publicering',r'innan publicering',
        r'redaktionell (?:anmärkning|notering|kommentar)',
        r'återstår att (?:faktagranska|verifiera|kontrollera)']
    for phrase in forbidden:
        assert not re.search(phrase,body,re.IGNORECASE), f'Intern arbetsnotering i {item}: {phrase}'
print('PASS: inga kända redaktionella arbetsmarkörer i boktexten')
