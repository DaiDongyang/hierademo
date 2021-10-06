import os


item_temp = '''
<tr>
<td>({0})</td>
<td>&nbsp;</td>
<td><audio controls style="width: 300px;">
                            <source src="en/{1}" type="audio/mpeg">
                          Your browser does not support the audio element.

</tr>
'''

def process_en():
    out_file = 'part_en_wav_content.html'
    wav_names = [str(i) + '__spk0.npy.wav'  for i in range(1, 31)]
    # html_items = list()
    count = 1
    with open(out_file, 'w') as out_f:
        for wav_name in wav_names:
            html_item = item_temp.format(count, wav_name)
            print(html_item, file=out_f)
            # html_items.append()
            count += 1


if __name__ == '__main__':
    process_en()