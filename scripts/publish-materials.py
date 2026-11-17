"""Generate maintainable course Markdown from extracted sources and reviewed solutions."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
qs=json.loads((root/'materials/questions.json').read_text())
solutions=json.loads((root/'materials/solutions.json').read_text())
programs=json.loads((root/'materials/programming-solutions.json').read_text())
groups=[('2026下-python-第1章作业','assignments/homework-01','第1章作业','HOMEWORK 01'),('2026下-python-第2章作业','assignments/homework-02','第2章作业','HOMEWORK 02'),('2026下-python-第3章作业','assignments/homework-03','第3章作业','HOMEWORK 03'),('2026下-PTA测试1','quizzes/quiz-01','第一次上机小测','QUIZ 01')]
kinds=[('judgment','判断题'),('choice','单选题'),('blank','填空题'),('programming','编程题')]
for group,path,title,code in groups:
 items=[q for q in qs if q['group']==group]
 fm=f'---\ntitle: {title}\neyebrow: {code}\ncode: {code}\ndescription: 题目、参考答案与解析。\nquestionGroups:\n'
 for kind,name in kinds:fm+=f'  - [{name}, {kind}, {sum(q["kind"]==kind for q in items)}]\n'
 fm+='---\n\n<div class="editor-note">\n\n题目整理自所提供的 PTA 网页，参考答案按 Python 3 核对，未在 PTA 平台提交验证。原题编号重复时保留原编号，以页面题序区分。\n\n</div>\n'
 for kind,name in kinds:
  section=[q for q in items if q['kind']==kind]
  if kind=='programming':section.sort(key=lambda q:int(q['number'].split('-')[-1]))
  fm+=f'\n<h2 id="{kind}" class="quiz-group">{name}<span>{len(section):02} QUESTIONS</span></h2>\n'
  for i,q in enumerate(section,1):
   key=f'{group}/{kind}/{i}'
   if kind=='programming':
    solution=programs[group+'/'+q['number']];answer='```python\n'+solution['code']+'```';explanation=solution['explanation'];heading=q['title']
   else:solution=solutions[key];answer=solution['answer'];explanation=solution['explanation'];heading=q['number']+' '+name
   body=q['body'].replace('### ','#### ')
   # Protect literal less-than comparisons outside code/math against Vue HTML parsing.
   chunks=re.split(r'(```[\s\S]*?```|`[^`]*`|\$[^$]*\$)',body)
   for n in range(0,len(chunks),2):chunks[n]=chunks[n].replace('<','&lt;')
   body=''.join(chunks)
   # Keep option letters as literal text instead of repeated ordered-list markers.
   body=re.sub(r'^([ABCD])\. ',r'**\1.** ',body,flags=re.M)
   body=body.replace('**D.** ```python', '**D.**\n\n```python')
   fm+=f'\n:::: question {kind}-{i} | {heading}\n\n<div class="section-label">题干 <span>QUESTION</span></div>\n\n{body}\n\n::: answer\n\n{answer}\n\n:::\n\n::: explanation\n\n{explanation}\n\n:::\n\n::::\n'
 (root/('docs/'+path+'.md')).write_text(fm)
 print(path,len(items))
