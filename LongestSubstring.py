def LongestSubstring(s):
    start = 0
    end = 0

    longest = ''
    char_set = set()

    while end < len(s):
        #print ("end:", end)
        cur_char = s[end]
        #print("cur_char:", cur_char)
        if cur_char not in char_set:
            char_set.add(cur_char)
            longest = s[start : end+1]

        else:
            if longest.index(cur_char) == 0:
                longest = longest[longest.index(cur_char)+1:]
                longest = longest + cur_char
                start = start + 1
                #print("start:", start)
            else:
                pass

        end = end + 1

    return longest

result = LongestSubstring("abcdabefb")
print(result)


def test(inp, expected):
    ret = LongestSubstring(inp)
    print(ret==expected, inp, expected, '"{}"'.format(ret))


    
    
    
    
test('dcba', 'dcba')
test('abcdab', 'abcd')
test('aaaa', 'a')
test('abcdabcde', 'abcde')
test('abcdabefb', 'cdabef')