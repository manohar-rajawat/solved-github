def solution(string):
    string = string.split()
    for i in range(len(string)):
        if (string[i][0] == '`' or string[i][-1] == '`') and string[i] != string[i].upper():
            new_word = []
            for idx,val in enumerate(string[i].split('_')):
                if idx==0:
                    new_word.append(val)
                else:
                    new_word.append(val.capitalize())
            string[i] = ''.join(new_word)
    return ' '.join(string)
            

string = "Hello this is manohar `singh_manohar rajawat` and I want to be followed by `this_is_going_to_be_cool` I'm here `this_is_going to_be_cool` I'm new here `CONSTANT_TIME`"
print (solution(string))
