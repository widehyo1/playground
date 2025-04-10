{
  "query": {
      "has_parent": {
          "parent_type": "parent",
          "query": {
              "match_all": {}
          }
      }
  },
  "_source": [
    "knlg_info_id",
    "hstry_id",
    "smy_cn",
    "h_del_yn",
    "dwnld_cnt",
    "frst_reg_dt",
    "last_chg_dt",
    "hstry_expln",
    "page_cn",
    "page_cnt"
  ],
  "from": 0,
  "size": 10000
}
