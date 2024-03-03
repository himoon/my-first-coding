def split_tags(tags):
    hash_removed = tags.replace("#", "")
    list_tags = hash_removed.split(",")
    return list_tags


print(split_tags("#파이썬,#자바"))
print(split_tags("#한빛미디어,#혼공학습단,#혼공"))
print(split_tags("#혼공 첫 프로그래밍"))
