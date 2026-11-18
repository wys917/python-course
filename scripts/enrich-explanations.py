"""Add reviewed, topic-specific teaching notes without changing questions or answers.

The original explanation stays at the beginning. Markers make this operation
idempotent and allow edits to the shared notes to be applied repeatedly.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
notes_source = (ROOT / 'materials/explanation-guides.md').read_text()
notes = dict(re.findall(r'^## ([\w-]+)\n\n(.*?)(?=^## |\Z)', notes_source, re.M | re.S))
# Order follows the published page, not the original PTA numbering.
MAP = {
 'homework-01': {
 'judgment': 'execution environment environment math input output names binding encoding input names',
 'choice': 'hardware execution input base base hardware encoding comments names environment paradigm output',
 'blank': 'fractions-base base signed signed',
 'programming': 'input precedence output patterns',
 },
 'homework-02': {
 'judgment': 'conversions precedence conversions conversions precedence format format format truth names truth truth conversions base short-circuit assignment',
 'choice': 'string-model complex numeric numeric numeric base types-add truth math complex encoding string-model',
 'blank': 'precedence precedence rounding short-circuit base base short-circuit complex short-circuit short-circuit short-circuit join short-circuit short-circuit precedence precedence numeric base encoding bitwise bitwise',
 'programming': 'range branches branches rational rational conversions base sorting range rational rational math branches patterns',
 },
 'homework-03': {
 'judgment': 'types-add search sorting string-model mutability mutability slicing slicing slicing slicing slicing slicing slicing slicing sorting chained join join format format rounding repeat repeat methods',
 'choice': 'sorting escapes string-model slicing list-methods',
 'blank': 'repeat split list-methods list-methods random format-args format-args format search search methods methods strip copying iteration aggregate assignment',
 'programming': 'aggregate search conversions filtering filtering counting conversions counting sorting strip bitwise format bitwise filtering filtering counting counting',
 },
 'quiz-01': {
 'judgment': 'names encoding precedence conversions format format truth conversions base short-circuit assignment join sorting repeat',
 'choice': 'execution comments names paradigm string-model base types-add math complex encoding string-model assignment copying',
 'blank': 'base signed signed short-circuit complex short-circuit precedence numeric branches',
 'programming': 'branches sorting conversions rational math patterns',
 },
 'quiz-02': {
 'judgment': 'types-add search mutability slicing slicing slicing chained join format format repeat methods random input string-model import mutability',
 'choice': 'escapes slicing list-methods assignment import range',
 'blank': 'split list-methods format-args format-args format search strip copying iteration aggregate assignment',
 'programming': 'conversions strip filtering filtering counting patterns fractions-base',
 },
}

# Each programming note explains the exact reference solution on that page.
PROGRAM_STEPS = {
'homework-01': [
'两次 `input()` 对应两行输入，而不是同一行里的两个数。每次先用 `int()` 转换，再做加法；若直接相加两次读取的字符串，输入 12 和 3 会得到 123 而不是 15。最后一次 `print()` 只输出结果，不能附带说明。',
'先把同一行的三个系数依次拆给 a、b、c，再计算判别式。`b*b` 是平方，`4*a*c` 的乘号不能省略。这里只计算判别式，不需要继续开平方或求方程根；判别式为负也是合法结果，不能自行改成 0。',
'这道题没有输入，所以不应写 `input()` 等待数据。字符串定界用的引号不会被打印；引号内部的中文逗号、英文字母大小写和文字内容则都是输出的一部分。`print()` 会在行末自动加一个换行。',
'把图形按行拆成五个字符串。前两行与后两行都是星号、三个空格、星号，中间一行是五个连续星号。`\\n` 分隔行而不产生额外空行；不要用制表符代替三个空格，因为显示宽度与实际字符都不同。',
],
'homework-02': [
'求的是 11 到 m 的所有整数之和，所以首项为 11，最后一项为 m。`range(11,m+1)` 中的 `+1` 用来让 m 真正被取到；再由 `sum()` 累加。可用 m=11 检查只含一项，再用 m=12 检查是否包含末项。输出中的 `sum = ` 也属于格式要求。',
'分段点是 x=0，必须先分支再求 `1/(2*x)`，否则会除零。条件表达式只求选中的那一支，所以 x=0 时不会执行除法。输入和函数值分别使用 `.3f` 显示三位小数；格式化发生在计算之后，不要先把 x 四舍五入再代入。',
'把用电量拆成“基础部分”和“超出部分”。基础部分最多 50 度，由 `min(usage,50)` 得到；超出部分最低为 0，由 `max(usage-50,0)` 得到。超出部分单价是基础单价加额外加价，而不是只收加价。代入 49、50、51 三个值检查边界，避免把全部用量都按高价计费。',
'第 i 项分母是第 i 个正奇数 `2*i-1`，i 从 1 到 n，恰好 n 项。用 `Fraction(1,2*i-1)` 保持分数精确，先算总和，再用 `ceil()` 向上取整。n=1 时和恰为 1，向上取整仍应为 1，不是无条件加 1。',
'先分开观察项的三个部分：分子依次为 i，分母依次为 `2*i-1`，符号从正号开始交替，所以是 `(-1)**(i-1)`。把三者相乘并对 i=1～n 求和，最后保留三位小数。手算前两项 `1-2/3` 可检查符号与下标是否整体错位。',
'先按题面允许的分隔方式取得数字 a 和次数 b。`str(a)*b` 构造重复文本，如 a=3、b=4 时得到 `3333`，再用 `int()` 变为整数输出。这里的 b 是重复次数，不是乘法倍数；若输入允许多位 a，重复的单位就是整个 a 的文本，而不是其中某一位。',
'第一个输入必须先保留为文本，因为其中可能含十六进制字母，也可能带前导零。第二个输入是基数，先转成整数，再执行 `int(digits,base)`。例如文本 11 在二进制中是 3，在八进制中是 9；提前按十进制转换会丢掉“按指定进制解析”的步骤。',
'输入是码点数值，先按整数排序，再用 `chr()` 转字符。若先转成字符串数字排序，100 与 65 的顺序会不符合数值大小。最后用 `<` 作为 `join()` 的分隔符，因此只出现在相邻字符之间，首尾不多加符号，也不加空格。',
'先统一检查 `-20 <= lower <= upper <= 50`，不合法就只输出 `Invalid.`。合法时输出表头，然后按摄氏度步长 2 遍历，不要求一定经过 upper，但不能超过它。华氏温度由 `c*1.8+32` 计算，`14.1f` 控制的是这一数值字段的宽度及小数位，不是整行宽度。',
'先确定要构造的数字长度是 2、4、…，不是 1 到 n 每个长度。对每个 width，用 `str(a)*width` 得到一个重复数字项，再转整数求和。循环终点用 n+1 保证 n 为偶数时能取到 n；n 为奇数时自然停在前一个偶数。可以用 n=2 和 n=4 检查首项、末项。',
'每项由整数平方和分数两部分组成，i 遍历 m 到 n 且包含两端。先把所有项加完，最后执行 `floor()`；若先对每项取整，就会丢失可能合起来超过 1 的小数部分。用 m=n=1 检查整数边界，并结合题面提示理解这里采用的是向下取整定义。',
'将公式拆成三块：角度正弦、带指数的分式、自然对数，再按原式相加减。35° 先转弧度，分母整个 `sqrt(x**4+1)` 需要放在除号右侧，最后是减去 `log(7*x)`。实数范围要求 x>0 才能计算这个对数；按题目合法输入计算，不能擅自把非法参数取绝对值。',
'先用 x<=15 决定第一段，否则用第二段。边界 x=15 代入两段都为 20，因此公式衔接；x 略大于 15 时才使用后一段。输出两位小数只是表现形式，分支判断应使用原输入值，不应先把 x 格式化或取整。',
'外层循环 i 从 1 到 n，第 i 行把 `* ` 这个两字符单元重复 i 次。单元中的空格也被重复，因此每行末尾保留一个空格，与原样例一致。每次 `print()` 后自动换行；这里是左对齐三角形，无需补前导空格。',
],
'homework-03': [
'先读完整组身高并求总和，再按原顺序逐一判断。条件 `height*人数 > 总和` 与“身高严格大于平均值”等价，却无需浮点除法。等于平均值的不输出，也不能先排序改变原序。每个合格身高后按样例保留一个空格，最后另行换行。',
'最大合法下标是 `len(s)-1`，倒序遍历用 `range(len(s)-1,-1,-1)`，其中终点 -1 不会被取到，所以下标 0 仍会检查。匹配 a 或 b 用一个 `or`，两字符恰好相同时也只输出一次。输出的是原字符串下标和原字符，不能先反转字符串后直接使用反转后的下标。',
'先把输入规范化为整数，再转成字符串，因而不会把前导零算进位数。位数等于字符个数，各位和则逐字符转成整数累加。输入 0 时字符串是 `0`，位数为 1、数字和为 0。代码按题目给定的非负数范围工作；若扩展到负数，应先取绝对值，不能把负号送给 `int(c)`。',
'反向字母表从 Z 到 A，原字母相对 A 的偏移量为 `ord(c)-ord(\'A\')`，用这个偏移量索引转换表。只转换 A～Z，其余字符原样保留。检查 A→Z、Z→A、M→N 三个位置，可以确认映射起点和方向；`join()` 只拼接结果，不增加分隔符。',
'先按题意处理输入两端空格，再把目标字符转为小写，作为比较标准。遍历 s 时用 `c.lower()` 判断是否应删去，但保留下来的仍是原字符 c，因此不会把整串都变成小写。内部空格不应因删除字符而自动合并，若题意没有要求忽略大小写，也不能自行标准化。',
'`seen` 保存已经接受过的字母的小写形式，用于不区分大小写地判断重复；`result` 保存原字符，保留首次出现的大小写。先排除非英文字母，再判断首次出现，满 10 个后立即停止。最后检查是否确实凑够 10 个，不足时输出 `not found`，不能输出不完整结果。',
'反转对象是数字的十进制文本，而不是整数本身。`[::-1]` 产生反向字符串，再转成整数会自动去掉前导零，所以 700 得到 7。此解按题目非负输入范围处理；若扩展到负数，需要单独保存符号，不能让反转后的负号落在末尾。',
'先统一大小写，再对字符排序。排序既保留字符种类，也保留每种字符的出现次数，因此能区分 aab 与 abb；单纯比较 `set()` 做不到。空格、数字及标点没有被题意排除时都参与比较，不能随意删掉。原样例冲突仍按上文保留和说明，参考代码遵循忽略大小写的题意。',
'`enumerate(s)` 产生字符及其下标，代码交换成 `(字符,下标)` 元组交给 `max()`。元组先比较第一项，相同才比较第二项，因此会选最大字符的最后一次出现位置。这是利用元组的字典序规则，而不是 `max()` 自动知道题意。非空字符串是前提，空串没有可选元素。',
'每次用 `input()` 读取完整一行，只去掉左侧普通空格后测长度。末尾空格属于有效内容，不能用 `strip()`；中间空格也不能用拆分输入的方式破坏。`longest` 从 0 开始，每轮代表已读各行的最大有效长度。输出 `length=` 后紧跟数值，没有额外空格。',
'`bin(n)` 返回带 `0b` 前缀的二进制字符串，前缀里没有字符 1，因此直接统计 `1` 即可。n=0 得到 `0b0`，统计结果仍是 0。这里统计的是值为 1 的位，不是总位数，也不是十进制数字 1 的个数；补前导零不会改变答案。',
'分别把两个整数格式化为至少 8 位二进制，然后输出分隔线和两数的和。`08b` 中 0 表示补零，8 是最小宽度，b 是二进制；若和需要第 9 位，不会被截掉。不要只把两个输入的二进制字符串拼接，也不要先把格式化文本当十进制数相加。',
'对每一二进制位，异或只在两数该位不同的时候产生 1。因此先求 `x^y`，再统计其二进制中 1 的数量即可。两数相等时异或为 0，距离为 0；高位补零后仍适用。这个做法依赖题目的非负整数表示语义，负数若未规定固定字长，不能直接照搬汉明距离解释。',
'先筛出字母数字，再统一小写，最后比较标准化字符串与逆序结果。三个步骤的顺序与目的要分开：标点不参与，大小写不影响匹配，数字仍参与。清理后为空串时，它和自身逆序相等，代码输出 yes。若题目只允许 ASCII 字母数字，需要相应缩小筛选范围。',
'按原顺序筛出合法十六进制字符，构造 h；保留原字符是为了满足第一行输出的大小写要求。第二行再用 `int(h,16)` 计算数值，例如 a1B 为 `10*16**2+1*16+11=2587`。`isalnum()` 会接受 G 等非法十六进制字符，不能替代白名单。空结果的处理约定已在上文说明。',
'A 保证没有重复字符，因此逐个遍历 A 并检查是否在 B 中，每个共同字符恰好计数一次。布尔值可参与求和，`sum(c in b for c in a)` 就是把每次匹配的 True 当成 1。不能改为遍历 B，因为它的重复字符可能多算；大小写按原字符比较，不能额外转小写。',
'先检查长度和前 17 位是否均为十进制数字，避免转换时报错；合法后让每一位与对应权重相乘，再求和。余数 `total%11` 是校验表下标，查到的字符必须与第 18 位完全一致，包括大写 X。错误号码按输入顺序收集，最后统一输出；只有列表为空时才输出 `All passed`。',
],
'quiz-01': [
'分段点为 x=0：该点返回 0，其他输入才计算 `1/(2*x)`。条件表达式仅求所选分支，因而能避免除零。输入值和计算值分别保留三位小数；不要先舍入输入再判断它是否等于 0。',
'先把输入转成整数，再按 `reverse=True` 降序排序。排序完成后用 `map(str,values)` 转回文本，以 `>` 连接，因此符号只在相邻两项之间出现。用 2、10、3 检查可以发现按字符串排序与按整数排序的区别。',
'HHMM 不是以 100 为进制的时间长度。用 `//100` 取小时、`%100` 取分钟，各自换算成当天累计分钟，再相减。最后用 `divmod(差值,60)` 得到小时和分钟，如 0950 到 1010 是 20 分钟，不能直接用 1010-950 当分钟数。此解按题目同日到达前提处理。',
'第 i 项是 `i*i+1/i`，i 从 m 到 n 且包含两端。先以精确分数求总和，再统一向下取整，不能先把每个分数部分删除。`floor()` 对整数保持原值，与“严格小于”字面定义的差别沿用原题提示并已作说明。',
'先把公式分为角度正弦、指数分式和自然对数。35 度转成弧度后调用 `sin()`，分母使用完整的 `sqrt(x**4+1)`，对数使用 `log(7*x)`。自然对数要求 x>0。最后只格式化结果，不在中间任意取整，以免放大误差。',
'第 i 行重复 i 次 `* `，包括每个星号后的普通空格，行末空格与原样例一致。循环从 1 到 n，终点用 n+1；`print()` 每轮自动换行，因此不需要在字符串中再加一个换行。',
],
'quiz-02': [
'输入 456 时，规范化字符串为 `456`，长度是 3，逐个转换并相加得到 4+5+6=15。`sum(int(c) for c in s)` 可展开为从 0 开始的循环累加，有助于理解生成器表达式。0 也占一位；若以后扩展到负数，先分离负号再处理数字。',
'每轮读一整行，清理左侧普通空格后测长度，再与目前最长值比较。例如一行是三个前导空格、abc、两个尾随空格，处理后长度是 5 而不是 3。输入数量控制循环次数，不应把所有词拆开当成不同字符串。',
'先标准化再比较，避免让标点或大小写影响回文定义。可用短例子 `A,b,a!` 推演：筛选并转小写后为 `aba`，左右对称。也可以用左右双指针逐项比较来理解切片比较的含义；不同写法必须保留相同的筛选规则。',
'第一行要输出筛选后的原字符，第二行才输出该串的十进制值，所以不能在筛选时一律转小写。十六进制字符的顺序决定各位权重，也不能排序。`int(h,16)` 完成按位权解释；`print()` 整数默认显示十进制，与 h 原本的进制不同。',
'题目明确 A 无重复，因此从 A 出发逐个做存在判断，B 的重复次数不会影响一次判断结果。若 A=`EOo`，B=`EOOO`，只匹配 E 和 O，小写 o 不匹配，计数为 2。若取消 A 无重复的条件，就必须先重新定义题目究竟数不同字符还是数匹配位置。',
'外层 i 从 m 到 n 表示每行的峰值；递增段为 1～i，递减段为 i-1～1，峰值不能重复。把两段各自用 `range()` 构造后连接，左侧补 n-i 个空格。对 m=n 的情况也只输出一行，而不是从第 1 行开始补出整座图形。',
'维护剩余小数，每次乘 2 后提取整数位，再把剩余小数留给下一轮。例如 0.625 依次得到位 1、0、1。精确分数能可靠判断余数是否为零；仍需最多 10 轮的上限处理无限循环表示。输出按题意截断，不对第 11 位做四舍五入。',
],
}

START = '<!-- teaching-notes:start -->'
END = '<!-- teaching-notes:end -->'

def enrich_page(path):
    text = path.read_text()
    chunks = re.split(r'(^:::: question [^\n]+\n)', text, flags=re.M)
    counts = {}
    total = 0
    for i in range(1, len(chunks), 2):
        kind = chunks[i].split()[2].rsplit('-', 1)[0]
        counts[kind] = counts.get(kind, 0) + 1
        index = counts[kind] - 1
        keys = MAP[path.stem][kind].split()
        key = keys[index]
        extra = notes[key].strip()
        if kind == 'programming':
            extra = '**解题步骤与边界**\n\n' + PROGRAM_STEPS[path.stem][index] + '\n\n' + extra
        body = chunks[i + 1]
        # Replace only a prior enrichment, preserving original imported explanation.
        body = re.sub(r'\n\n' + re.escape(START) + r'.*?' + re.escape(END), '', body, flags=re.S)
        match = re.search(r'(<div class="explanation">\s*\n\s*<div class="section-label">解析 <span>EXPLANATION</span></div>\s*\n)([\s\S]*?)(\n\s*</div>\s*\n\s*:::)', body, re.M)
        assert match, (path, chunks[i])
        # Replace only a prior enrichment, preserving the imported explanation and answer.
        enriched = re.sub(r'\n\s*' + re.escape(START) + r'.*?' + re.escape(END), '', match[2], flags=re.S).rstrip()
        addition = '\n\n' + START + '\n\n' + extra + '\n\n' + END
        body = body[:match.start(2)] + enriched + addition + '\n\n' + body[match.end(2):]
        chunks[i + 1] = body
        total += 1
    for kind, keys in MAP[path.stem].items():
        assert counts.get(kind) == len(keys.split()), (path, kind, counts)
    assert counts['programming'] == len(PROGRAM_STEPS[path.stem])
    path.write_text(''.join(chunks))
    return total

if __name__ == '__main__':
    total = 0
    for directory, names in [('assignments', ['homework-01','homework-02','homework-03']), ('quizzes',['quiz-01','quiz-02'])]:
        for name in names:
            path = ROOT / 'docs' / directory / (name + '.md')
            count = enrich_page(path)
            total += count
            print(f'{path.relative_to(ROOT)}: {count} explanations enriched')
    print(f'Total: {total}')
