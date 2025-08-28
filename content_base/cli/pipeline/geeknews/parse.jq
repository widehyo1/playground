def get_title:
    ..
    | objects
    | select(.id == "topic_contents")
    | .children[0].text // "";
