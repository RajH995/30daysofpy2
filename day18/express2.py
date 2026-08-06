import re

paragraph1 = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


def count_words(paragraph):
    my_list = re.split(r'[\s.]+', paragraph.lower())
    my_dict = {}
    for word in my_list:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return my_dict

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

my_dict = count_words(clean_text(sentence))

print(dict(list(my_dict.items())[:3]))