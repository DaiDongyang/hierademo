import os


item_temp = '''
<tr>
<td>({0})</td>
<td>&nbsp;</td>
<td>{1}</td>
</tr>
'''

ch_txt = './txts/ch.txt'
en_txt = './txts/en.txt'

def process_ch(out_fpath):
    content_items = list()
    with open(ch_txt, 'r') as ch_f:
        for line in ch_f:
            eles = line.strip().split()
            if len(eles) >= 2:
                content_item = ' '.join(eles[1:])
                print(eles)
                print(content_item)
                content_items.append(content_item)
    with open(out_fpath, 'w') as out_f:
        count = 1
        for content_item in content_items:
            html_item = item_temp.format(count, content_item)
            print(html_item, file=out_f)
            count += 1

def process_en(out_fpath):
    content_items = list()
    with open(en_txt, 'r') as ch_f:
        for line in ch_f:
            eles = line.strip().split()
            if len(eles) >= 1:
                content_item = line.strip()
                content_items.append(content_item)
    with open(out_fpath, 'w') as out_f:
        count = 1
        for content_item in content_items:
            
            html_item = item_temp.format(count, content_item)
            print(html_item, file=out_f)
            count += 1

if __name__ == '__main__':
    process_ch('part_ch_content.html')