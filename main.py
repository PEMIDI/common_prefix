from data import words


def find_common_prefix(words_list):

    shortest_word = min(words_list, key=len)

    parse_result = []
    for i in range(len(shortest_word)):
        tmp = ""

        for word in words_list:
            tmp += word[i]
        parse_result.append(tmp)
    print(parse_result)

    total_result = ""

    for item in parse_result:
        if len(set(item)) != 1:
            break
        print(item)
        total_result += item[0]

    return total_result


print(find_common_prefix(words))









# print(find_common_prefix(words))
