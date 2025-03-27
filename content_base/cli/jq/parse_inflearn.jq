.dataResponse
| .[0]
| .dataSubset
| .[0]
| .dataset
| .tableDataset
| .column
| .[0].dateColumn.values as $open_date
| .[1].stringColumn.values as $title
| .[2].stringColumn.values as $large_category
| .[3].stringColumn.values as $small_category
| .[4].stringColumn.values as $skill_tag
| .[5].doubleColumn.values as $price
| .[6].longColumn.values as $student_count
| [
  $open_date
  ,$title
  ,$large_category
  ,$small_category
  ,$skill_tag
  ,$price
  ,$student_count
] as $keys
| [
   $open_date
  ,$title
  ,$large_category
  ,$small_category
  ,$skill_tag
  ,$price
  ,$student_count
]
| transpose
| map([.[]])
| map(@csv)[]
