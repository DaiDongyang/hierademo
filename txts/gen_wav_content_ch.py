import os


item_temp = '''
<tr>
<td>({0})</td>
<td>&nbsp;</td>
<td><audio controls style="width: 300px;">
                            <source src="bs/{1}" type="audio/mpeg">
                          Your browser does not support the audio element.
 </audio></td>
 <td>&nbsp;</td>
 <td><audio controls style="width: 300px;">
                            <source src="ps/{1}" type="audio/mpeg">
                          Your browser does not support the audio element.
 </audio></td>
 <td>&nbsp;</td>
 <td><audio controls style="width: 300px;">
                            <source src="rap/{1}" type="audio/mpeg">
                          Your browser does not support the audio element.
 </audio></td>
</tr>
'''

def process_ch():
    out_file = 'part_ch_wav_content.html'
    wav_names = ['0000' + str(i) + '.wav'  for i in range(10, 40)]
    # html_items = list()
    count = 1
    with open(out_file, 'w') as out_f:
        for wav_name in wav_names:
            html_item = item_temp.format(count, wav_name)
            print(html_item, file=out_f)
            # html_items.append()
            count += 1


if __name__ == '__main__':
    process_ch()