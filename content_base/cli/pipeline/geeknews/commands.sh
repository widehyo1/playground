#!/bin/bash
# https://news.hada.io/sitemap.xml
# xq -r '.sitemapindex.sitemap | .[].loc' sitemap.xml > url/sitemap_urls.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2019.xml > url/topic_2019.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2020.xml > url/topic_2020.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2021.xml > url/topic_2021.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2022.xml > url/topic_2022.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2023.xml > url/topic_2023.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2024.xml > url/topic_2024.txt
xq -r '.urlset.url | .[].loc' topic_meta/topic_2025.xml > url/topic_2025.txt
