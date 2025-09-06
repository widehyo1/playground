["workCd","date","pjtCd","pjtNm","workTy","workTyTitle","workTitle","workTime"], (
  ..
  | objects
  | select(.work | length > 0)
  | .work[]
  | [.workCd, .date, .pjtCd, .pjtNm, .workTy, .workTyTitle, .workTitle, .workTime]
)
| @csv
