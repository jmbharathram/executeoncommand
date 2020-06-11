str = "hi and hi hello and"
str_list = str.split()
#print(str_list)
#Solution 1 O(n^2)

duplicate_words = set()

for word in str_list: #O(n)
  count = str_list.count(word) #O(n)
  if count > 1:
     duplicate_words.add(word)

#print(duplicate_words)

#Solution 2 O(n)
str = "hi and hi hello and"
str_list = str.split()

count = {}
duplicate_words = set()
for word in str_list:
    count[word] = count.get(word, 0) + 1
    print(count)
    if count[word] > 1:
        duplicate_words.add(word)

print(duplicate_words)
