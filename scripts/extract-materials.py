"""Read-only source extraction; run with beautifulsoup4, markdownify and python-pptx installed."""
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify
from pptx import Presentation
from urllib.parse import unquote
import json,re,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'materials';OUT.mkdir(exist_ok=True)
images=ROOT/'docs/public/images/problems';images.mkdir(parents=True,exist_ok=True)
def convert(node,file):
 node=BeautifulSoup(str(node),'html.parser')
 blocks={}
 for x in node.select('.katex'):
  a=x.select_one('annotation');x.replace_with(NavigableString('$'+a.get_text()+'$' if a else x.get_text()))
 for x in node.select('[data-blank-index]'):
  x.replace_with(NavigableString(' _____ '))
 for x in node.select('.cm-line [contenteditable="false"]'):
  if x.select_one('input'):x.replace_with(NavigableString('_____'))
 for x in node.select('[data-code]'):
  lines=x.select('.cm-content .cm-line')
  code='\n'.join(l.get_text().replace('\u200b','') for l in lines)
  lang='text' if x.get('data-lang') in ['in','out','text'] else 'python'
  key=f'CODEBLOCKTOKEN{len(blocks)}END'
  blocks[key]='\n\n```'+lang+'\n'+code+'\n```\n\n'
  x.replace_with(NavigableString(key))
 for x in node.select('img'):
  src=unquote(x.get('src',''));p=file.parent/src
  if p.exists() and p.is_file():
   dest=hashlib.sha256(p.read_bytes()).hexdigest()[:12]+p.suffix.lower();shutil.copyfile(p,images/dest);x['src']='/images/problems/'+dest;x['alt']=x.get('alt') or '题目配图'
  else:print('MISSING IMAGE',file.name,src)
 text=markdownify(str(node),heading_style='ATX',escape_underscores=False,escape_asterisks=False,escape_misc=False)
 for key,value in blocks.items():text=text.replace(key,value)
 text=text.replace('\\[','[').replace('\\] ','] ')
 # markdownify escapes code fences inside text nodes; restore only fences.
 text=text.replace('\\`','`')
 return re.sub(r'\n{3,}','\n\n',text).strip()
all=[]
for file in sorted((ROOT/'题目').glob('*.html')):
 soup=BeautifulSoup(file.read_text(),'html.parser');group=file.stem.split(' - ')[-1]
 if file.name.startswith('编程题'):continue
 if re.match(r'7-\d',file.name):
  markdown=soup.select_one('.rendered-markdown')
  all.append(dict(group=group,kind='programming',number=file.stem.split(' ')[0],title=file.stem.split(' - ')[0],body=convert(markdown,file),source=file.name))
 else:
  kind={'判断题':'judgment','单选题':'choice','填空题':'blank'}[file.name.split(' ')[0]]
  cards=soup.select('div[id].scroll-mt-0')
  for card in cards:
   label=card.select_one('button[class*=label_]');mds=card.select('.rendered-markdown')
   if not label or not mds:continue
   body=convert(mds[0],file)
   if kind=='choice':
    for opt in card.select('label'):
     md=opt.select_one('.rendered-markdown')
     if md:
      letter=opt.select_one('input')['id'].split('-')[-1];body+='\n\n'+letter+'. '+convert(md,file)
   all.append(dict(group=group,kind=kind,number=label.get_text(strip=True),title=label.get_text(strip=True),body=body,source=file.name))
(OUT/'questions.json').write_text(json.dumps(all,ensure_ascii=False,indent=2))
for g in sorted(set(q['group'] for q in all)):
 qs=[q for q in all if q['group']==g]
 (OUT/(g+'.md')).write_text('\n\n'.join('## '+q['number']+' '+q['title']+'\n\n'+q['body'] for q in qs))
 print(g,len(qs),{k:len([q for q in qs if q['kind']==k]) for k in ['judgment','choice','blank','programming']})
for f in sorted((ROOT/'课件').rglob('*.pptx')):
 prs=Presentation(f)
 text=[]
 for i,slide in enumerate(prs.slides,1):
  lines=[shape.text for shape in slide.shapes if shape.has_text_frame]
  text.append(f'## Slide {i}\n\n'+'\n\n'.join(lines))
 (OUT/(f.stem+'.txt')).write_text('\n\n'.join(text))
