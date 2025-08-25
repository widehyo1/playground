const { Cluster } = require('puppeteer-cluster');
const fs = require("fs");
const path = require("path");

const requests = [
  { url: "https://news.ycombinator.com", selector: ".title" },
  { url: "https://github.com", selector: "title" },
];

// 1. 누적 저장용 파일 (하나로 모으는 경우)
const aggregateFile = "results_html.json";

// 기존 파일 초기화
fs.writeFileSync(aggregateFile, "[]");

(async () => {
  const cluster = await Cluster.launch({
    concurrency: Cluster.CONCURRENCY_PAGE,
    maxConcurrency: 5, // 동시에 5개까지 실행
  });

  // 크롤링 작업 정의
  await cluster.task(async ({ page, data: { url } }) => {
    await page.goto(url, { waitUntil: "domcontentloaded" });
    const html = await page.content();
    return { url, html };
  });

  // 요청들 실행
  const results = await Promise.all(
    requests.map(req => cluster.execute(req))
  );

  // ------------------------------------------------------
  // 1) 모든 응답을 하나의 파일에 누적 저장
  // ------------------------------------------------------
  const existing = JSON.parse(fs.readFileSync(aggregateFile, "utf8"));
  const newResults = [...existing, ...results];
  fs.writeFileSync(aggregateFile, JSON.stringify(newResults, null, 2));

  // ------------------------------------------------------
  // 2) 각 요청당 응답을 개별 파일로 저장
  // ------------------------------------------------------

  // html_outputs 디렉토리 없으면 생성
  if (!fs.existsSync("html_outputs")) {
    fs.mkdirSync("html_outputs");
  }

  for (const result of results) {
    // URL을 안전한 파일명으로 변환
    const safeName = result.url.replace(/https?:\/\//, "").replace(/[^\w.-]/g, "_");
    const filename = path.join("html_outputs", `${safeName}.html`);
    fs.writeFileSync(filename, result.html, "utf8");
  }

  console.log("✅ HTML 저장 완료!");
  await cluster.idle();
  await cluster.close();
})();
