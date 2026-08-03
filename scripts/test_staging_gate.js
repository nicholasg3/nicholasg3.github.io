/* End-to-end check of the staging gate.
 *
 * Serve the site and run against it:
 *   python3 -m http.server 8899 --bind 127.0.0.1 &
 *   STAGING_PASSWORD='...' node scripts/test_staging_gate.js
 *
 * WebCrypto needs a secure context, so localhost works and file:// does not.
 * Set CHROME_PATH if Chromium is not where Playwright put it.
 */
const { chromium } = require('playwright');

const BASE = process.env.BASE_URL || 'http://localhost:8899';
const PASSWORD = process.env.STAGING_PASSWORD;
if (!PASSWORD) {
  console.error('Set STAGING_PASSWORD to the staging password.');
  process.exit(2);
}
const results = [];
function check(name, pass, detail) {
  results.push({ name, pass, detail: detail || '' });
  console.log(`${pass ? 'PASS' : 'FAIL'}  ${name}${detail ? '  — ' + detail : ''}`);
}

(async () => {
  const browser = await chromium.launch(
    process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const ctx = await browser.newContext();
  const page = await ctx.newPage();

  // 1. Locked draft page shows no draft content before unlock.
  await page.goto(`${BASE}/blog/staging/posts/metric-authorship.html`);
  const lockedText = await page.locator('body').innerText();
  check('locked draft hides content before password',
    lockedText.includes('Locked draft') && !lockedText.toLowerCase().includes('completion'),
    `body starts: ${JSON.stringify(lockedText.slice(0, 40))}`);

  // 2. Wrong password is rejected.
  await page.fill('#password', 'not-the-password-at-all');
  await page.click('#unlock-btn');
  await page.waitForFunction(() => document.getElementById('gate-error')?.textContent.length > 0, null, { timeout: 30000 });
  const err = await page.locator('#gate-error').innerText();
  check('wrong password rejected', /wrong password/i.test(err), err);

  // 3. Correct password decrypts the draft in place.
  await page.fill('#password', PASSWORD);
  await page.click('#unlock-btn');
  await page.waitForFunction(() => document.querySelector('h1')?.textContent.includes('success'), null, { timeout: 60000 });
  const title = await page.locator('h1').first().innerText();
  check('correct password decrypts draft', /score may track who defines the task/i.test(title), title);

  // 4. Stylesheet still resolves after document.write (relative paths intact).
  const styled = await page.evaluate(() =>
    [...document.querySelectorAll('link[rel=stylesheet]')].map(l => l.href).join(','));
  check('draft keeps its stylesheet link', styled.includes('styles.css'), styled);

  // 5. Staging index: locked, then decrypts the manifest and lists drafts.
  const ctx2 = await browser.newContext();
  const page2 = await ctx2.newPage();
  await page2.goto(`${BASE}/blog/staging/`);
  await page2.waitForTimeout(1200);
  const indexLocked = await page2.locator('#gate').evaluate(el => !el.classList.contains('hidden'));
  check('staging index is locked on arrival', indexLocked);

  await page2.fill('#password', PASSWORD);
  await page2.click('#unlock-btn');
  await page2.waitForSelector('#list:not(.hidden)', { timeout: 60000 });
  const cards = await page2.locator('.stage-card').count();
  check('index decrypts manifest and lists drafts', cards === 30, `${cards} cards`);

  // 6. Following a draft link in the same tab reuses the session key — no re-prompt.
  await page2.locator('.stage-card h2 a').first().click();
  await page2.waitForFunction(
    () => !document.body.innerText.includes('Locked draft'), null, { timeout: 60000 });
  const draftText = await page2.locator('body').innerText();
  check('draft opens from the index without re-entering the password',
    draftText.length > 800 && !draftText.includes('Locked draft'),
    `${draftText.length} chars rendered`);

  // 7. Lock clears the session key.
  await page2.goto(`${BASE}/blog/staging/`);
  await page2.waitForSelector('#list:not(.hidden)', { timeout: 60000 });
  await page2.click('#lock-btn');
  await page2.waitForTimeout(1200);
  const relocked = await page2.locator('#gate').evaluate(el => !el.classList.contains('hidden'));
  check('Lock button re-locks the session', relocked);

  const page3 = page2;

  // 7. The unfinished draft is gone from the public blog.
  const res = await page3.goto(`${BASE}/blog/posts/metric-authorship-ai-coding.html`);
  check('public draft URL no longer served', res.status() === 404, `HTTP ${res.status()}`);

  // 8. The public blog index no longer links it.
  await page3.goto(`${BASE}/blog/`);
  const links = await page3.evaluate(() => [...document.querySelectorAll('a')].map(a => a.getAttribute('href')).join(','));
  check('public index has no link to the draft', !links.includes('metric-authorship'));

  // 9. The idea backlog is no longer served as public JSON.
  const jsonRes = await page3.goto(`${BASE}/blog/data/ideas-queue.json`);
  check('ideas backlog JSON no longer served', jsonRes.status() === 404, `HTTP ${jsonRes.status()}`);

  // 10. The ideas queue page still works, behind the same password.
  const ctx3 = await browser.newContext();
  const page4 = await ctx3.newPage();
  await page4.goto(`${BASE}/blog/ideas-queue.html`);
  await page4.waitForTimeout(1200);
  const queueLocked = await page4.locator('#gate').evaluate(el => !el.classList.contains('hidden'));
  check('ideas queue is locked on arrival', queueLocked);

  await page4.fill('#password', PASSWORD);
  await page4.click('#unlock-btn');
  await page4.waitForSelector('#queue:not(.hidden)', { timeout: 60000 });
  const rows = await page4.locator('#ideas-body tr').count();
  check('ideas queue decrypts and renders the backlog', rows === 30, `${rows} rows`);

  // 11. Encrypted payloads must not leak plaintext to a reader who just fetches them.
  const raw = await (await fetch(`${BASE}/blog/staging/posts/metric-authorship.html`)).text();
  check('served draft bytes contain no plaintext',
    !/completion metrics|Goodhart|definition of done/i.test(raw), `${raw.length} bytes`);

  await browser.close();
  const failed = results.filter(r => !r.pass);
  console.log(`\n${results.length - failed.length}/${results.length} checks passed`);
  process.exit(failed.length ? 1 : 0);
})().catch(e => { console.error('ERROR', e); process.exit(1); });
