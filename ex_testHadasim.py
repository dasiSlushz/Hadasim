def ex(path):
    count_lines = 0
    count_words =0
    max_sentence = 0
    conter_unique = 0
    without_k = ''
    counter_k = 0
    dic_colors = {'red':0,'green':0,'pink':0,'gray':0,'brown':0,'blue':0,'white':0,'purple':0,'yellow':0,'black':0,'orange':0}
    with open(path, 'r') as file:

        lines_file = file.readlines()

        count_lines = len(lines_file)

        count_words =  len(str(lines_file).split())

        text = str(lines_file)
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]

        #finding unique
        unique = {}

        for word in words:
            if word.find('k') == -1:
                counter_k += 1
                without_k += word + ' '
            else:
                counter_k = 0
                without_k = ''
            if word in dic_colors.keys():
                dic_colors[word] = dic_colors[word] + 1
            if word not in unique.keys():
                unique[word] = 0
            else:
                unique[word] =  1
        for i in unique.keys():
            if unique[i] == 0:
                conter_unique += 1

        text = str(lines_file)
        words = text.replace('!', '.')
        words = words.replace('?', '.')
        words = words.split('.')
        print(len(words))
        conter = 0

        for line in words:
            if len(line) > max_sentence:
                max_sentence = len(line)
            conter += len(line)

        for (color,value) in dic_colors.items():
            if value > 0 :
                print('color',color ,'appers' ,value ,'times')

        #prints
        #1
        print("number of lines in file:", count_lines)
        #2
        print("number of words in file:", count_words)
        #3
        print("number of unique words in file:", conter_unique)
        #4
        print("maximum sentence length in file:", max_sentence)
        print("average sentence length in file:", conter /len(words))
        #6
        print("longest words without 'k':", without_k)
ex('work.txt')