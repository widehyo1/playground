db:
	sqlite3 -init rc.finance finance.db

count-flow:
	sqlite3 -init rc.finance finance.db -cmd 'select count(1) from flow' '.quit'

count-portpolio:
	sqlite3 -init rc.finance finance.db -cmd 'select count(1) from portpolio' '.quit'

count: count-flow count-portpolio

show-flow:
	sqlite3 -init rc.finance finance.db -cmd 'select * from flow' '.quit'

show-portpolio:
	sqlite3 -init rc.finance finance.db -cmd 'select * from portpolio' '.quit'

show: show-flow show-portpolio

schema:
	sqlite3 -init rc.finance finance.db -cmd '.schema' '.quit'

dump-flow:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.output data/flow.csv' 'select * from flow' '.quit'

dump-portpolio:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.output data/portpolio.csv' 'select * from portpolio' '.quit'

dump: dump-flow dump-portpolio

delete-flow:
	sqlite3 -init rc.finance finance.db -cmd 'delete from flow' '.quit'

delete-portpolio:
	sqlite3 -init rc.finance finance.db -cmd 'delete from portpolio' '.quit'

delete: delete-flow delete-portpolio

insert-flow:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.import --skip 1 data/flow.csv flow' '.quit'

insert-portpolio:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.import --skip 1 data/portpolio.csv portpolio' '.quit'

insert-portpolio-krw:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.import --skip 1 data/portpolio_krw.csv portpolio' '.quit'

insert-portpolio-usd:
	sqlite3 -init rc.finance finance.db -cmd '.mode csv' '.import --skip 1 data/portpolio_usd.csv portpolio' '.quit'

insert: insert-flow insert-portpolio

create-flow:
	sqlite3 finance.db -cmd 'CREATE TABLE flow(date TEXT, asset INTEGER, income INTEGER, bonus_ibk INTEGER, bonus_parent INTEGER, event INTEGER, score INTEGER, expanse INTEGER)' '.quit'

create-portpolio:
	sqlite3 finance.db -cmd 'CREATE TABLE portpolio(date TEXT, ticker TEXT, name TEXT, amount INTEGER, price TEXT, currency TEXT, value NUMBER, account TEXT, type TEXT)' '.quit'

create: create-flow create-portpolio

drop-flow:
	sqlite3 finance.db -cmd 'drop TABLE flow' '.quit'

drop-portpolio:
	sqlite3 finance.db -cmd 'drop TABLE portpolio' '.quit'

drop: drop-flow drop-portpolio

init-table: drop create

sync-flow: delete-flow insert-flow

sync-portpolio: delete-portpolio insert-portpolio

sync-portpolio-krw: delete-portpolio insert-portpolio-krw
sync-portpolio-usd: delete-portpolio insert-portpolio-krw

sync-krw: usd2krw delete-portpolio insert-portpolio-krw
sync-usd: krw2usd delete-portpolio insert-portpolio-usd

sync: delete insert

generate-dat:
	awk -f ./flow_to_asset_with_score_dat data/flow.csv > data/asset_with_score.dat

krw2usd:
	awk -f ./krw_to_usd.awk data/portpolio.csv > data/portpolio_usd.csv

usd2krw:
	awk -f ./usd_to_krw.awk data/portpolio.csv > data/portpolio_krw.csv

report-pdf:
	gnuplot asset_with_score_pdf.dem


