const { test, expect } = require("@playwright/test");
const chapters=["01","02","03","04","05","06","07","08"];
test("home lists all chapters and stage filter works",async({page})=>{
 await page.goto("/");
 await expect(page.locator("[data-course-card]")).toHaveCount(28);
 await page.locator("[data-stage-filter]").selectOption("derivative");
 await expect(page.locator("[data-course-card]:visible")).toHaveCount(7);
 await page.locator("[data-stage-filter]").selectOption("all");
 await page.locator("[data-course-search]").fill("ε–δ");
 await expect(page.locator("[data-course-card]:visible").first()).toBeVisible();
});
for(const chapter of chapters){
 test(`chapter ${chapter}: MathML, SVG, responsive layout and interaction`,async({page})=>{
  const errors=[];page.on("pageerror",e=>errors.push(e.message));
  await page.goto(`/${chapter}.html`);
  await expect(page.locator("h1")).toBeVisible();
  await expect(page.locator("math").first()).toBeVisible();
  const audit=await page.evaluate(()=>{
   const maths=[...document.querySelectorAll("math")],svgs=[...document.querySelectorAll("svg")];
   return {overflow:document.documentElement.scrollWidth>innerWidth,mathCount:maths.length,mathNamespaces:maths.every(e=>e.namespaceURI==="http://www.w3.org/1998/Math/MathML"),mathVisible:maths.every(e=>e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0),svgAccessible:svgs.every(s=>s.querySelector("title")&&s.querySelector("desc"))};
  });
  expect(audit.overflow).toBeFalsy();expect(audit.mathCount).toBeGreaterThan(5);expect(audit.mathNamespaces).toBeTruthy();expect(audit.mathVisible).toBeTruthy();expect(audit.svgAccessible).toBeTruthy();
  const slider=page.locator("[data-demo] input[type=range]").first(),status=page.locator("[data-demo-status]").first();
  await expect(slider).toBeVisible();const before=await status.textContent();
  await slider.evaluate(el=>{const step=Number(el.step)||1;el.value=String(Math.min(Number(el.max),Number(el.value)+step));el.dispatchEvent(new Event("input",{bubbles:true}));el.dispatchEvent(new Event("change",{bubbles:true}))});
  await expect(status).not.toHaveText(before);expect(errors).toEqual([]);
 });
}
