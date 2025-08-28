#!/bin/bash
xq -r '.urlset.url | .[].loc' topic_meta/topic_2019.xml > url/topic_2019.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2020.xml > url/topic_2020.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2021.xml > url/topic_2021.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2022.xml > url/topic_2022.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2023.xml > url/topic_2023.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2024.xml > url/topic_2024.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2025.xml > url/topic_2025.txt

cat url/topic_2019.txt url/topic_2020.txt url/topic_2021.txt url/topic_2022.txt url/topic_2022.txt url/topic_2023.txt url/topic_2024.txt url/topic_2025.txt > url/all.url
# grep 'topic' url/all.url | sort --field-separator "=" --key 2,2 --sort numeric > url/topics.url
grep 'topic' url/all.url | sort | uniq | sort --field-separator "=" --key 2,2 --sort numeric > url/topics.url
