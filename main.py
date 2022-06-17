# string slicing

print("\nString Slicing")
print(" Index[] & Slice()")
print(" [start:stop:step]")
print(" (start:stop:step)\n")
#[start:stop:step]
#(start,stop,step)

print("Index[start:stop]")
random_words = "words: Flower Dance Extension Ash Basketball"
# slicing
first_slice = random_words[7:13]                      # passing the word 'words'
second_slice = random_words[14:19]
third_slice = random_words[20:29]
fourth_slice = random_words[30:33]
fifth_slice = random_words[34:]                        # python asume stop to be until the last
# output
print(" 1st word - " + first_slice)
print(" 2nd word - " + second_slice)
print(" 3rd word - " + third_slice)
print(" 4th word = " + fourth_slice)
print(" 5th word - " + fifth_slice + '\n')

print("Index[start:stop:step]")
# slicigg
print("(step:2) - Display every '2' character in a string")
st_slice = random_words[7:13:2]              # display every 'n' character in a string
nd_slice = random_words[14:13:2]
rd_slice = random_words[20:29:2]
rth_slice = random_words[30:33:2]
fth_slice = random_words[34::2]
# output
print("1st slice w/h step: " + st_slice)
print("2nd slice w/h step: " + nd_slice)
print("3rd slice w/h step: " + rd_slice)
print("4th slice w/h step: " + rth_slice)
print("5th slice w/h step: " + fth_slice)

# slice()
print("\nSlice(start:stop)")
print("Initial statements:")
web_one = " https://google.com"
web_two = " https://youtube.com"
web_three = " https://facebook.com"
web_four = " https://twitter.com"
web_five = " https://instagram.com\n"
# Display initial statements
print(web_one)
print(web_two)
print(web_three)
print(web_four)
print(web_five)
# slicing
slice_one = slice(9,-4)                            # 'stop' counts from behind becomes negative start from -1
slice_two = slice(9,-4)
slice_three = slice(9,-4)
slice_four = slice(9,-4)
slice_five = slice(9,-4)
#
print("Updated statements:")
print(web_one[slice_one])
print(web_two[slice_two])
print(web_three[slice_three])
print(web_four[slice_four])
print(web_five[slice_five])










