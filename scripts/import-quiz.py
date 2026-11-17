"""Import the supplied Markdown without altering the source file."""
from pathlib import Path
import re
source = Path('2026下-PTA测试2_题目与答案解析.md').read_text()
groups = [('judgment', '判断题', 17), ('choice', '单选题', 6), ('blank', '填空题', 11), ('programming', '编程题', 7)]
sections = re.split(r'^## .+$', source, flags=re.M)[1:]
output = ['''---
title: 第二次上机小测
eyebrow: QUIZ 02
description: 题目、参考答案与解析。
code: Quiz 02
questionGroups:
  - [判断题, judgment, 17]
  - [单选题, choice, 6]
  - [填空题, blank, 11]
  - [编程题, programming, 7]
---

<div class="editor-note">

本次小测共 **41 题**：判断题 17 题、单选题 6 题、填空题 11 题、编程题 7 题。整理自原始小测资料，答案按 Python 3 语义核对；编程题代码未在 PTA 平台提交验证。

文中 `□` 表示一个空格；真实输出放在代码块中，请注意前导和末尾空格。

</div>
''']
for (gid, name, count), section in zip(groups, sections):
    output.append(f'\n<h2 id="{gid}" class="quiz-group">{name}<span>{count:02d} QUESTIONS</span></h2>\n')
    questions = re.split(r'^### 第', section, flags=re.M)[1:]
    assert len(questions) == count
    for n, q in enumerate(questions, 1):
        header, body = q.split('\n', 1)
        title = header.split('：', 1)[1] if '：' in header else name
        # Include auxiliary answer paragraphs (e.g. visible whitespace) in the folded answer.
        match = re.search(r'\*\*答案[^\n]*', body)
        explain = body.index('**解析：**')
        question = body[:match.start()].strip().replace('**题目：**', '<div class="section-label">题干 <span>QUESTION</span></div>\n\n', 1)
        answer = body[match.start():explain].strip()
        # Strip opening bold marker while preserving paired inline emphasis.
        original = body[match.start():explain].strip()
        if original.startswith('**答案：**'):
            answer = original[len('**答案：**'):].strip()
        elif original.startswith('**答案：'):
            answer = original[len('**答案：'):]
            if answer.endswith('**'): answer = answer[:-2]
        elif original.startswith('**答案（'):
            answer = original.replace('**答案（用 `□` 显示空格）：**', '**用 `□` 显示空格：**', 1)
        explanation = body[explain + len('**解析：**'):].strip()
        output.append(f'\n:::: question {gid}-{n} | Q{n:02d}. {title}\n\n{question}\n\n::: answer\n\n{answer.strip()}\n\n:::\n\n::: explanation\n\n{explanation}\n\n:::\n\n::::\n')
Path('docs/quizzes/quiz-02.md').write_text('\n'.join(output))
