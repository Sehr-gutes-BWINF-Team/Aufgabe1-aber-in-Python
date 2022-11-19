import re


def create_regex(string):
    out = ""

    word_prefix = "("
    word_suffix = ")\\W+"
    wildcard = "([^\\s]+)\\W+"

    for element in string.split(' '):
        if element == "_":
            out += wildcard
        else:
            out += word_prefix + element + word_suffix

    return out


def clean(string):
    everything_but_words_and_spaces = re.compile(r"[^\w\s]")
    redundant_spaces = re.compile(r"\s{2,}")
    string = re.sub(everything_but_words_and_spaces, '', string)
    string = string.replace('\n', ' ')
    string = string.replace('\t', '')
    string = string.replace('_', '')
    string = re.sub(redundant_spaces, ' ', string)
    return string


if __name__ == '__main__':
    with open("resources/Alice_im_Wunderland.txt") as file:
        data = file.read()
        data = clean(data)
        # print(data)

        with open("resources/stoerung1.txt") as riddle:
            riddle_data = riddle.read()
            regex = create_regex(riddle_data)
            print("Generierter Regexausdruck: " + regex)
            matches = re.findall(regex, data, flags=re.IGNORECASE)
            for match in matches:
                print(f'Passende Textstelle: {" ".join(match)}')


