FROM diamol/node

CMD ["node", "/web-ping/app.js"]

ENV TARGET="blog.sixeyed.com" \
    METHOD="HEAD" \
    INTERVAL="3000" \
    ASDF="asdf"

WORKDIR /web-ping
COPY app.js .

