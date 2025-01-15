import pdfplumber
import re
def get_word_position(text):
    # word_position = {}
    start_word = {}
    word_num = 0
    # split the text into lines and get the position of the first word in each line
    for line_num,line in enumerate(text.split('\n')):
        start_word[word_num] =  line_num
        for word in line.split(' '):
            # word_position[word_num] = line_num
            word_num+=1
    return start_word#,word_position

def format_text(text):
    new_text1 = ''
    for line in text.split('\n'):
        line = split_english_text(line)
        new_text1+=line + '\n'

    new_text2 = ''

    for line in new_text1.split('\n'):
        line = line.replace('.',' . ').replace(',',' , ').replace('-',' - ')
        line = line.replace('  ',' ').replace('  ',' ').strip()
        if line == '':
            continue
        if not  re.match(r'^[a-zA-Z]', line):
            
            line = ' '.join(reversed([word if ord(word[0])<= 57 and ord(word[0])>= 48 else word[::-1] for word in line.split(' ')]))
        line = line.replace(' .','.').replace('. ','.').replace(' ,',',').replace(', ',',')
        new_text2+=line + '\n'
    return new_text2

def split_english_text(line):
    english_pattern = r'[A-Za-z]+'  # Matches English text and email addresses
    english_text = ' '.join(re.findall(english_pattern, line))
    start = english_text.split(' ')[0]
    new_start = f'\n {start}' if start != '' else ''
    
    end = english_text.split(' ')[-1]
    new_end = f'{end} \n' if end != '' else ''
    return line.replace(start, new_start).replace(end, new_end)
# Open the PDF file

def get_line_metadata(words,line_start_words):
    'from the words metadata get the line metadata by identifiying  the position of the word in each line and taking its metadata'
    lines = {} # Store the line position of each word in the text
    for i,word in enumerate(words): # Loop through all the words in the text

        if i in line_start_words.keys():# if the word is the first word in the line  - get the line metadata data drawn from the word metadata
            line_num = line_start_words[i]
            lines[line_num] = word
            # lines[line_num]['page_num'] = page_num
            del lines[line_num]['upright'],lines[line_num]['doctop']#,lines[i]['text'],lines[line_num]['direction']
    return lines

def remove_header_footer(text,lines,header_height=60,footer_height=800):
    new_text = ''        
    for line_num,line in enumerate(text.split('\n')):
        if lines[line_num]['top']<header_height or lines[line_num]['bottom']>footer_height or lines[line_num]['direction']=='ttb': 
            continue 
        # print(lines[line_num]['height'])    
        new_text+=line + '\n'
    return new_text
def read_heb_pdf(pdf_path,header_height=60,footer_height=800):
    full_text = ''
      
    with pdfplumber.open(pdf_path) as pdf:
        # Loop through all the pages in the PDF
        for page_num in range(len(pdf.pages)):
            # page_num = 10
            page = pdf.pages[page_num]
            
            # Extract text & words from the page
            text = page.extract_text()
            words = page.extract_words()# Extract words and their metadata (position, font size, etc.)
            
            # Get the position of the first word in each line and extract the line metadata from it
            line_start_words = get_word_position(text)
            lines = get_line_metadata(words,line_start_words)
            
            #loop through the text and get the text that is not in the header or footer
            text_without_headers = remove_header_footer(text,lines,header_height,footer_height)
                    
            # split the text into lines of english and hebrew and than format it
            full_text += format_text(text_without_headers)
            # break
    return full_text
# full_text = read_heb_pdf(pdf_path)
# print('full_text: \n',full_text)

    
    

