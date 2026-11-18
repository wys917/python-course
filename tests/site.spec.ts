import { test, expect } from '@playwright/test'
test.beforeEach(async ({ page }) => {
  await page.goto('/', { waitUntil: 'networkidle' })
})
test('homepage, local navigation, color mode persistence and 404', async ({ page }) => {
  const errors: string[] = []
  page.on('pageerror', e => errors.push(e.message))
  await page.goto('/', { waitUntil: 'networkidle' })
  await expect(page.locator('h1')).toContainText('Python')
  await expect(page.locator('.module-card')).toHaveCount(4)
  await page.screenshot({ path: 'test-results/home-desktop.png', fullPage: true })
  await page.getByRole('button', { name: '切换深色模式' }).click()
  await expect(page.locator('html')).toHaveClass(/dark/)
  await page.reload()
  await expect(page.locator('html')).toHaveClass(/dark/)
  await page.screenshot({ path: 'test-results/home-dark.png', fullPage: true })
  await page.getByRole('button', { name: '切换浅色模式' }).click()
  for (const url of ['/topics/', '/assignments/', '/quizzes/', '/final-review/']) {
    await page.goto(url, { waitUntil: 'networkidle' })
    await expect(page.locator('.page-heading h1')).toBeVisible()
    await page.reload()
    await expect(page.locator('.page-heading h1')).toBeVisible()
  }
  await page.goto('/missing.html', { waitUntil: 'networkidle' })
  await expect(page.locator('.error-number')).toContainText('404')
  expect(errors).toEqual([])
})

test('all questions, answers hidden initially, animated toggles, code copy and anchors', async ({ page, context }) => {
  await context.grantPermissions(['clipboard-read', 'clipboard-write'])
  await page.goto('/quizzes/quiz-02.html', { waitUntil: 'networkidle' })
  await expect(page.locator('.question-card')).toHaveCount(41)
  await expect(page.locator('.answer-toggle[aria-expanded="false"]')).toHaveCount(41)
  const answer = page.locator('.question-card').first().locator('.answer')
  expect(await answer.locator('.answer-grid').evaluate(e => e.getBoundingClientRect().height)).toBe(0)
  await answer.locator('button').click()
  await expect(answer.locator('button')).toHaveAttribute('aria-expanded', 'true')
  await expect(answer.locator('.answer-content')).toContainText('T（正确）')
  await answer.locator('button').click()
  await expect(answer.locator('button')).toHaveAttribute('aria-expanded', 'false')
  await page.locator('.question-nav-grid a[href="#programming-1"]').click()
  await expect(page).toHaveURL(/#programming-1$/)
  const programming = page.locator('.question-card').filter({ has: page.locator('#programming-1') })
  await programming.locator('.answer-toggle').click()
  const code = programming.locator('.answer-content .language-python')
  await code.hover()
  await code.locator('button.copy').click()
  await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toContain('sum(int(c) for c in s)')
  await page.screenshot({ path: 'test-results/quiz-desktop.png', fullPage: false })
  await page.reload()
  await expect(page.locator('.answer-toggle[aria-expanded="false"]')).toHaveCount(41)
})

test('local search finds question text and navigates to quiz', async ({ page }) => {
  await page.goto('/', { waitUntil: 'networkidle' })
  await page.locator('.VPNavBarSearch button').click()
  const input = page.locator('#localsearch-input')
  await expect(input).toBeVisible()
  await input.fill('回文')
  await expect(page.locator('.VPLocalSearchBox .result').first()).toBeVisible()
  await page.locator('.VPLocalSearchBox .result').first().click()
  await expect(page).toHaveURL(/(quiz-02|homework-03)/)
})

test('comments load on request with separate threads and stay off closed topics', async ({ page }) => {
  const threads: string[] = []
  await page.route('https://giscus.app/**', async route => {
    threads.push(new URL(route.request().url()).searchParams.get('term') || '')
    await route.fulfill({ contentType: 'text/html', body: '<p>评论区</p>' })
  })
  await page.goto('/assignments/homework-01.html')
  const load = page.getByRole('button', { name: '加载评论' })
  await expect(load).toBeVisible()
  expect(threads).toEqual([])
  await load.click()
  await expect.poll(() => threads.slice()).toEqual(['assignments/homework-01.md'])
  await page.locator('.desktop-nav').getByRole('link', { name: 'Final Review' }).click()
  await load.click()
  await expect.poll(() => threads.slice()).toEqual(['assignments/homework-01.md', 'final-review/index.md'])
  await page.locator('.desktop-nav').getByRole('link', { name: 'Topics' }).click()
  await expect(page.locator('#comments')).toHaveCount(0)
})

test('mobile navigation, question contents and layout fit viewport', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 })
  await page.goto('/', { waitUntil: 'networkidle' })
  await page.screenshot({ path: 'test-results/home-mobile.png', fullPage: true })
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBe(390)
  await page.getByRole('button', { name: '切换导航菜单' }).click()
  await page.locator('.mobile-nav').getByRole('link', { name: 'Quizzes' }).click()
  await expect(page.locator('.page-heading h1')).toContainText('课堂小测')
  await page.locator('.resource-card[href="/quizzes/quiz-02.html"]').click()
  await expect(page.locator('.question-card')).toHaveCount(41)
  await page.getByRole('button', { name: '本次小测目录' }).click()
  await page.locator('.mobile-toc a[href="#programming"]').click()
  await expect(page).toHaveURL(/#programming$/)
  await expect(page.locator('.mobile-toc')).toHaveCount(0)
  await page.screenshot({ path: 'test-results/quiz-mobile.png' })
  expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBe(390)
})

test('collections and local images render while chapter links show only the closure notice', async ({ page }) => {
  const errors: string[] = []
  page.on('pageerror', e => errors.push(e.message))
  for (const [url, count] of [['/assignments/homework-01.html',31],['/assignments/homework-02.html',63],['/assignments/homework-03.html',63],['/quizzes/quiz-01.html',42]] as const) {
    await page.goto(url, { waitUntil: 'networkidle' })
    await expect(page.locator('.question-card')).toHaveCount(count)
    await expect(page.locator('.answer-toggle[aria-expanded="false"]')).toHaveCount(count)
    const ids = await page.locator('.question-card h3').evaluateAll(es => es.map(e => e.id))
    expect(new Set(ids).size).toBe(count)
    for (const img of await page.locator('.vp-doc img').all()) expect(await img.evaluate((e: HTMLImageElement) => e.complete && e.naturalWidth > 0)).toBe(true)
    await page.reload({ waitUntil: 'networkidle' })
    await expect(page.locator('.question-card')).toHaveCount(count)
  }
  for (let chapter = 1; chapter <= 8; chapter++) {
    await page.goto(`/topics/chapter-0${chapter}.html`, { waitUntil: 'networkidle' })
    await expect(page.locator('.page-heading')).toContainText('本模块暂未开放')
    await expect(page.locator('.vp-doc')).toHaveText('你仍可前往课后作业或课堂小测进行练习。')
  }
  await page.setViewportSize({width:390,height:844})
  for (const url of ['/', '/topics/chapter-03.html','/assignments/homework-02.html']) {
    await page.goto(url, { waitUntil: 'networkidle' })
    expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBe(390)
  }
  await page.goto('/topics/', { waitUntil: 'networkidle' })
  await expect(page.locator('.page-heading')).toContainText('本模块暂未开放')
  expect(errors).toEqual([])
})
