#!/usr/bin/env python3
"""Reproducerbar EPUB- och PDF-export av book.yaml:s kapitelordning."""
import argparse, subprocess, shutil, yaml, re, tempfile
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--format', choices=['epub','pdf','all'], default='all')
args=parser.parse_args()
root=Path(__file__).resolve().parent.parent
meta=yaml.safe_load((root/'book.yaml').read_text(encoding='utf-8'))
files=[str(root/s) for s in meta['chapters']]
cover_rel=meta.get('cover_image', '').strip()
cover=(root/cover_rel).resolve() if cover_rel else None
if cover_rel and (not cover.is_file() or not cover.is_relative_to(root.resolve())):
    raise SystemExit(f'Ogiltig eller saknad omslagsbild: {cover_rel}')
for f in files:
    if not Path(f).is_file(): raise SystemExit(f'Saknat kapitel: {f}')
    if 'REDATIONELL PLATSHÅLLARE' in Path(f).read_text(encoding='utf-8'):
        raise SystemExit('Export blockerad: planeringsmarkörer återstår')
# Exporta med globala interna referensmål utan att ändra källmanus.
prepared=root/'exports'/'_prepared'
prepared.mkdir(parents=True,exist_ok=True)
source_ids=set(re.findall(r'\*\*\[(K\d{3})\]\*\*', (root/'chapters/17-kallor-och-lasanvisning.md').read_text(encoding='utf-8')))
if not source_ids: raise SystemExit('Källregistret saknar numrerade poster')
prepared_files=[]
for i,file in enumerate(files):
    text=Path(file).read_text(encoding='utf-8')
    if Path(file).name.startswith('17-'):
        # Intern länkpunkt i PDF och EPUB och kort, obruten länktext till webben.
        text=re.sub(r'\*\*\[(K\d{3})\]\*\*',lambda m:'**['+m.group(1)+']{#'+m.group(1).lower()+'}**',text)
        text=re.sub(r'https?://[^\s)]+',lambda m:'[Öppna källan]('+m.group(0)+')',text)
    else:
        def replace_ref(m):
            code=m.group(1)
            if code not in source_ids: raise SystemExit('Okänt käll-ID: '+code)
            return '['+code+'](#'+code.lower()+')'
        text=re.sub(r'(?<!\[)\[(K\d{3})\](?!\])', replace_ref,text)
    target=prepared/f'{i:02d}.md'
    target.write_text(text,encoding='utf-8')
    prepared_files.append(str(target))
for fmt in (['epub','pdf'] if args.format=='all' else [args.format]):
    if not shutil.which('pandoc'):raise SystemExit('Pandoc saknas')
    if fmt=='pdf' and not shutil.which('xelatex'):raise SystemExit('XeLaTeX saknas')
    settings=meta.get('exports',{}).get(fmt,{})
    out=root/'exports'/('digital-omstallning.'+fmt)
    cmd=['pandoc',*prepared_files,'-o',str(out),
         '--metadata',f"title:{meta['title']}",
         '--metadata',f"subtitle:{meta['subtitle']}",
         '--metadata',f"author:{meta['author']}",
         '--metadata','lang:sv',
         '--metadata',f"date:{meta.get('date','')}",
         '--toc','--toc-depth',str(settings.get('toc_depth',1))]
    if fmt=='pdf':
        cmd += ['--pdf-engine=xelatex','-V','papersize:a5','-V','geometry:margin=18mm','-V','documentclass:book','-V','classoption:openany','--top-level-division=chapter','-V','fontsize:10pt','-V','linestretch:1.13']
    else:
        cmd += ['--css',str(root/'publishing/epub.css')]
        if cover: cmd += ['--epub-cover-image',str(cover)]
    if fmt=='pdf':
        # Render first to a TeX document so we can insert ruled table rows while
        # leaving Pandoc's column widths and line wrapping intact.
        import re, tempfile
        tex=out.with_suffix('.tex')
        texcmd=[*cmd,'-s']
        texcmd[texcmd.index('-o')+1]=str(tex)
        subprocess.run(texcmd,check=True)
        t=tex.read_text(encoding='utf-8')
        if cover:
            # Fullbleed image on its own unnumbered first page.
            tex_cover=cover.as_posix()
            t=t.replace(r'\maketitle', '', 1)
            t=t.replace(r'\begin{document}',
                r'\begin{document}' + '\n'
                + r'\clearpage\thispagestyle{empty}\AddToShipoutPictureBG*{\AtPageLowerLeft{\includegraphics[width=\paperwidth,height=\paperheight]{'
                + tex_cover + r'}}}\null\clearpage' + '\n',1)
            t=t.replace(r'\begin{document}',r'\usepackage{graphicx}' + '\n' + r'\usepackage{eso-pic}' + '\n' + r'\begin{document}',1)
        # Ta bort löpande kapitelhuvud och centrera kapitelnummer/titel på två rader.
        t=t.replace('\\begin{document}', '\\begin{document}\n\\pagestyle{plain}')
        titlesec='\\usepackage{titlesec}\n\\titleformat{\\chapter}[display]{\\normalfont\\bfseries\\centering}{}{0pt}{\\large}\n\\titlespacing*{\\chapter}{0pt}{2pt}{15pt}'
        t=t.replace('\\begin{document}', titlesec+'\n\\begin{document}',1)
        t=re.sub(r'\\chapter\{(\d+)\.\s+(.*?)\}(\\label\{[^}]+\})?',
                 lambda m:r'\chapter['+m.group(1)+'. '+re.sub(r'\s+',' ',m.group(2))+']{'+r'\normalsize '+m.group(1)+r'\\[0.35em]\Large '+re.sub(r'\s+',' ',m.group(2))+'}'+(m.group(3) or ''),t,flags=re.S)
        # Länkad källtext ska inte få skrivas som lång obruten webbadress.
        def rule_longtable(match):
            block=match.group(0)
            # Every content row ends at a genuine LaTeX row terminator. Do not
            # alter headings or longtable control lines (\endhead etc.).
            lines=block.splitlines(keepends=True)
            for i,line in enumerate(lines):
                if re.search(r'(?<!\\)\\\\\s*$',line.rstrip('\n')) and not re.match(r'\s*\\(toprule|midrule|bottomrule|endhead|endfirsthead|endfoot)',line):
                    lines[i]=line.rstrip('\n')+'\n\\hline\n'
            return ''.join(lines)
        t=re.sub(r'\\begin\{longtable\}.*?\\end\{longtable\}',rule_longtable,t,flags=re.S)
        tex.write_text(t,encoding='utf-8')
        subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(out.parent),str(tex)],check=True,stdout=subprocess.DEVNULL)
        # Second pass resolves page references and the contents.
        subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(out.parent),str(tex)],check=True,stdout=subprocess.DEVNULL)
    else:
        subprocess.run(cmd,check=True)
        # EPUB: keep the navigation document for reader menus, not as a page in the spine.
        # Display chapter number and name as two centered lines without changing nav titles.
        from lxml import etree
        import zipfile, os
        tmp=out.with_suffix('.epub.tmp')
        nsx='http://www.w3.org/1999/xhtml'
        nsopf='http://www.idpf.org/2007/opf'
        with zipfile.ZipFile(out) as zin, zipfile.ZipFile(tmp,'w') as zout:
            for info in zin.infolist():
                data=zin.read(info.filename)
                if info.filename.endswith('.opf'):
                    tree=etree.fromstring(data)
                    items=tree.xpath('//*[local-name()="item" and contains(concat(" ",normalize-space(@properties)," ")," nav ")]')
                    ids={item.get('id') for item in items}
                    for ref in tree.xpath('//*[local-name()="itemref"]'):
                        if ref.get('idref') in ids: ref.set('linear','no')
                    data=etree.tostring(tree,xml_declaration=True,encoding='UTF-8')
                elif info.filename.endswith('.xhtml') and '/text/' in info.filename:
                    tree=etree.fromstring(data)
                    for h in tree.xpath('//*[local-name()="h1"]'):
                        raw=''.join(h.itertext()).strip()
                        m=re.fullmatch(r'(\d+)\.\s+(.+)',raw,re.S)
                        if not m: continue
                        for c in list(h): h.remove(c)
                        h.text=None
                        num=etree.SubElement(h,'{%s}span'%nsx)
                        num.set('class','chapter-number');num.text=m.group(1)
                        name=etree.SubElement(h,'{%s}span'%nsx)
                        name.set('class','chapter-name');name.text=m.group(2)
                        h.set('class', ((h.get('class') or '')+' two-line-chapter').strip())
                    data=etree.tostring(tree,xml_declaration=True,encoding='UTF-8')
                zout.writestr(info,data)
        os.replace(tmp,out)
    print(out)
