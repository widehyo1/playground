DB      := finance.db
DATA    := data
SCRIPT  := script
REPORT  := report
SQLITE  := sqlite3 $(DB)
AWK     := awk

TABLES  := flow portpolio

help: ## Show available commands
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS=":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'


# -- DB shell ------------------------------------------------------------------
.PHONY: db
db: ## finance.db sqlite3 셸 진입

	$(SQLITE)

# -- schema --------------------------------------------------------------------
.PHONY: schema
schema: ## 테이블 스키마 출력
	$(SQLITE) -cmd '.schema' '.quit'

# -- count ---------------------------------------------------------------------
.PHONY: count count-flow count-portpolio
count-flow: ## flow 테이블 레코드 수 출력
	$(SQLITE) -cmd 'select count(1) from flow' '.quit'

count-portpolio: ## portpolio 테이블 레코드 수 출력
	$(SQLITE) -cmd 'select count(1) from portpolio' '.quit'

count: count-flow count-portpolio ## 전체 테이블 레코드 수 출력

# -- show ----------------------------------------------------------------------
.PHONY: show show-flow show-portpolio
show-flow: ## flow 테이블 전체 행 출력
	$(SQLITE) -cmd 'select * from flow' '.quit'

show-portpolio: ## portpolio 테이블 전체 행 출력
	$(SQLITE) -cmd 'select * from portpolio' '.quit'

show: show-flow show-portpolio ## 전체 테이블 내용 출력

# -- dump ----------------------------------------------------------------------
.PHONY: dump dump-flow dump-portpolio
dump-flow: ## flow 테이블을 data/flow.csv로 덤프
	$(SQLITE) -cmd '.mode csv' '.output $(DATA)/flow.csv' 'select * from flow' '.quit'

dump-portpolio: ## portpolio 테이블을 data/portpolio.csv로 덤프
	$(SQLITE) -cmd '.mode csv' '.output $(DATA)/portpolio.csv' 'select * from portpolio' '.quit'

dump: dump-flow dump-portpolio ## 전체 테이블을 CSV로 덤프

# -- delete --------------------------------------------------------------------
.PHONY: delete delete-flow delete-portpolio
delete-flow: ## flow 테이블 전체 행 삭제
	$(SQLITE) -cmd 'delete from flow' '.quit'

delete-portpolio: ## portpolio 테이블 전체 행 삭제
	$(SQLITE) -cmd 'delete from portpolio' '.quit'

delete: delete-flow delete-portpolio ## 전체 테이블 행 삭제

# -- insert --------------------------------------------------------------------
.PHONY: insert insert-flow insert-portpolio insert-portpolio-krw insert-portpolio-usd
insert-flow: ## data/flow.csv를 flow 테이블에 삽입
	$(SQLITE) -cmd '.mode csv' '.import --skip 1 $(DATA)/flow.csv flow' '.quit'

insert-portpolio: ## data/portpolio.csv를 portpolio 테이블에 삽입
	$(SQLITE) -cmd '.mode csv' '.import --skip 1 $(DATA)/portpolio.csv portpolio' '.quit'

insert-portpolio-krw: ## data/portpolio_krw.csv를 portpolio 테이블에 삽입
	$(SQLITE) -cmd '.mode csv' '.import --skip 1 $(DATA)/portpolio_krw.csv portpolio' '.quit'

insert-portpolio-usd: ## data/portpolio_usd.csv를 portpolio 테이블에 삽입
	$(SQLITE) -cmd '.mode csv' '.import --skip 1 $(DATA)/portpolio_usd.csv portpolio' '.quit'

insert: insert-flow insert-portpolio ## CSV → DB 전체 삽입

# -- create / drop -------------------------------------------------------------
.PHONY: create create-flow create-portpolio drop drop-flow drop-portpolio init-table
create-flow: ## flow 테이블 생성
	$(SQLITE) -cmd 'CREATE TABLE flow(date TEXT, asset INTEGER, income INTEGER, bonus_ibk INTEGER, bonus_parent INTEGER, event INTEGER, score INTEGER, expanse INTEGER)' '.quit'

create-portpolio: ## portpolio 테이블 생성
	$(SQLITE) -cmd 'CREATE TABLE portpolio(date TEXT, ticker TEXT, name TEXT, amount INTEGER, price TEXT, currency TEXT, value NUMBER, account TEXT, type TEXT)' '.quit'

create: create-flow create-portpolio ## 전체 테이블 생성

drop-flow: ## flow 테이블 삭제
	$(SQLITE) -cmd 'drop TABLE flow' '.quit'

drop-portpolio: ## portpolio 테이블 삭제
	$(SQLITE) -cmd 'drop TABLE portpolio' '.quit'

drop: drop-flow drop-portpolio ## 전체 테이블 삭제

init-table: drop create ## 전체 테이블 초기화 (drop → create)

# -- sync ----------------------------------------------------------------------
.PHONY: sync sync-flow sync-portpolio sync-portpolio-krw sync-portpolio-usd sync-krw sync-usd
sync-flow:          delete-flow      insert-flow          ## flow CSV → DB 동기화
sync-portpolio:     delete-portpolio insert-portpolio     ## portpolio CSV → DB 동기화
sync-portpolio-krw: delete-portpolio insert-portpolio-krw ## portpolio KRW CSV → DB 동기화
sync-portpolio-usd: delete-portpolio insert-portpolio-usd ## portpolio USD CSV → DB 동기화

sync-krw: usd2krw delete-portpolio insert-portpolio-krw ## USD→KRW 변환 후 동기화
sync-usd: krw2usd delete-portpolio insert-portpolio-usd ## KRW→USD 변환 후 동기화

sync: delete insert ## 전체 CSV → DB 동기화

# -- currency conversion -------------------------------------------------------
.PHONY: krw2usd usd2krw
krw2usd: ## portpolio.csv KRW → USD 변환 (portpolio_usd.csv 생성)
	$(AWK) -f $(SCRIPT)/krw_to_usd.awk $(DATA)/portpolio.csv > $(DATA)/portpolio_usd.csv

usd2krw: ## portpolio.csv USD → KRW 변환 (portpolio_krw.csv 생성)
	$(AWK) -f $(SCRIPT)/usd_to_krw.awk $(DATA)/portpolio.csv > $(DATA)/portpolio_krw.csv

# -- reports / analysis --------------------------------------------------------
.PHONY: generate-dat report-pdf asset-growth asset-diff asset-report net-asset
generate-dat: ## flow.csv → asset_with_score.dat 생성
	$(AWK) -f $(SCRIPT)/flow_to_asset_with_score_dat.awk $(DATA)/flow.csv > $(DATA)/asset_with_score.dat

report-pdf: ## asset_with_score PDF 리포트 생성 (gnuplot)
	gnuplot $(SCRIPT)/asset_with_score_pdf.dem

asset-growth: ## 자산 성장률 출력
	$(AWK) -f $(SCRIPT)/growth_rate.awk $(DATA)/flow.csv

asset-diff: ## 자산 차이 및 점수 비율 출력
	$(AWK) -f $(SCRIPT)/asset_diff_score_ratio.awk $(DATA)/flow.csv

asset-report: ## 자산 종합 리포트 출력
	$(AWK) -f $(SCRIPT)/flow_to_report.awk $(DATA)/flow.csv

net-asset: ## 순자산 흐름 출력
	$(AWK) -f $(SCRIPT)/net_flow.awk $(DATA)/flow.csv
