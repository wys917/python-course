from pathlib import Path
import json,re,subprocess
root=Path(__file__).resolve().parents[1]
qs=json.loads((root/'materials/questions.json').read_text());solutions=json.loads((root/'materials/programming-solutions.json').read_text())
fail=[];count=0;conflicts=0
for q in qs:
 if q['kind']!='programming':continue
 code=solutions[q['group']+'/'+q['number']]['code']
 blocks=re.findall(r'####? (输入样例[^\n]*|输出样例[^\n]*)\n([\s\S]*?)(?=\n####? |\Z)',q['body'])
 inputs=[]
 for heading,body in blocks:
  m=re.search(r'```[^\n]*\n([\s\S]*?)\n```',body)
  if not m:continue
  data=m[1]+'\n'
  if heading.startswith('输入'):inputs.append(data)
  else:
   assert inputs,(q['title'],heading)
   result=subprocess.run(['python3','-c',code],input=inputs.pop(0),text=True,capture_output=True,timeout=5)
   count+=1
   if q['group']=='2026下-python-第3章作业' and q['number']=='7-8' and data=='no\n':
    assert result.stdout=='yes\n' and '冲突' in solutions[q['group']+'/'+q['number']]['explanation']
    conflicts+=1
    continue
   if result.stdout!=data or result.returncode:fail.append((q['group'],q['number'],repr(data),repr(result.stdout),result.stderr))
print('Samples checked:',count, '| Documented source conflict:',conflicts)
for item in fail:print('FAIL',item)
assert not fail
