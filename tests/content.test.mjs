import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
const source = readFileSync('2026下-PTA测试2_题目与答案解析.md', 'utf8')
const quiz = readFileSync('docs/quizzes/quiz-02.md', 'utf8')
const originalQuestions = source.split(/^### 第.+$/m).slice(1)
const importedQuestions = quiz.split(/^:::: question .+$/m).slice(1)

test('all 41 source questions retain question text, explanation, code, tables and whitespace', () => {
  assert.equal(originalQuestions.length, 41)
  assert.equal(importedQuestions.length, 41)
  for (let i = 0; i < 41; i++) {
    const original = originalQuestions[i].split(/^## /m)[0]
    const imported = importedQuestions[i]
    const question = original.split('**答案')[0].replace('**题目：**', '').trim()
    assert.ok(imported.includes(question), `Question ${i + 1} text lost`)
    const explanation = original.split('**解析：**')[1].trim()
    assert.ok(imported.includes(explanation), `Question ${i + 1} explanation lost`)
    const fences = [...original.matchAll(/```[^\n]*\n([\s\S]*?)```/g)]
    for (const [, code] of fences) assert.ok(imported.includes(code), `Question ${i + 1} code whitespace changed`)
    const answer = original.slice(original.indexOf('**答案'), original.indexOf('**解析：**'))
    const expected = answer.replace(/^\*\*答案：\*\*/, '').replace(/^\*\*答案：/, '').replace(/\*\*\s*$/, '').trim()
    if (!answer.startsWith('**答案（')) assert.ok(imported.includes(expected), `Question ${i + 1} answer changed`)
  }
})

test('programming references pass every supplied input/output example', () => {
  const programming = source.split('## 四、')[1].split(/^### 第.+$/m).slice(1)
  for (const [i, question] of programming.entries()) {
    const code = question.split('**答案：**')[1].match(/```python\n([\s\S]*?)```/)[1]
    const examples = [...question.split('**答案：**')[0].matchAll(/\*\*输入样例[^\n]*\n\n```text\n([\s\S]*?)```\n\n\*\*输出样例[^\n]*\n\n```text\n([\s\S]*?)```/g)]
    assert.ok(examples.length > 0)
    for (const [, input, expected] of examples) {
      const result = spawnSync('python3', ['-c', code], { input, encoding: 'utf8' })
      assert.equal(result.status, 0, `Programming ${i + 1}: ${result.stderr}`)
      assert.equal(result.stdout, expected, `Programming ${i + 1}: sample mismatch`)
    }
  }
})

test('new homework and quiz collections preserve all source questions and code indentation', () => {
  const sourceQuestions = JSON.parse(readFileSync('materials/questions.json', 'utf8'))
  const collections = [
    ['2026下-python-第1章作业', 'docs/assignments/homework-01.md', 31],
    ['2026下-python-第2章作业', 'docs/assignments/homework-02.md', 63],
    ['2026下-python-第3章作业', 'docs/assignments/homework-03.md', 63],
    ['2026下-PTA测试1', 'docs/quizzes/quiz-01.md', 42],
  ]
  for (const [group, file, count] of collections) {
    const markdown = readFileSync(file, 'utf8')
    assert.equal((markdown.match(/^:::: question /gm) || []).length, count)
    assert.equal((markdown.match(/^::: answer$/gm) || []).length, count)
    assert.equal((markdown.match(/^::: explanation$/gm) || []).length, count)
    for (const q of sourceQuestions.filter(q => q.group === group)) {
      for (const [, code] of q.body.matchAll(/```[^\n]*\n([\s\S]*?)```/g)) {
        assert.ok(markdown.includes(code), `${file}: code or sample changed for ${q.number}`)
      }
    }
    assert.ok(!markdown.includes('1 分'), `${file}: grading UI leaked into content`)
  }
})

test('new programming references pass 59 supplied samples with one explicitly documented source conflict', () => {
  const result = spawnSync('python3', ['scripts/check-programming.py'], { encoding: 'utf8' })
  assert.equal(result.status, 0, result.stdout + result.stderr)
  assert.match(result.stdout, /Samples checked: 59/)
  assert.match(result.stdout, /Documented source conflict: 1/)
})
