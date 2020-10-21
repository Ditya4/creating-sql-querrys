pre_querry = '''select switch_id, uni_a, uni_b, bill_dtm, duration, cdr_set_out, out_tg, to_char(bill_dtm,'yyyymmdd'),
 substr(service_type,0,1), out01, out02, out03, out04, outblock, segment_b
from ms_lvv.calls
where

bill_dtm between to_date(' 01.09.2020 00:00:00 ','dd.mm.yyyy hh24:mi:ss')
              and to_date(' 01.10.2020 00:00:00 ','dd.mm.yyyy hh24:mi:ss')

and '''
#uni_b in(

post_querry = '''group by switch_id, uni_a, uni_b, bill_dtm, duration, cdr_set_out, out_tg, to_char(bill_dtm,'yyyymmdd'),
  substr(service_type,0,1), out01, out02, outblock, out03, out04, segment_b
'''


fin = open('d:/python/double_dno/make_list_for_sql_out_function/export.tsv')
uni_b = list(map(str.rstrip, fin.readlines()))
print(uni_b)
for index in range(len(uni_b)):
    uni_b[index] = uni_b[index].strip('"')
print(uni_b)
filter_in_querry = 'UNI_B'
if uni_b[0] in ('UNI_A', 'UNI_B'):
    filter_in_querry = uni_b[0]
    uni_b = uni_b[1:]
print(uni_b, '\n', len(uni_b))
set_uni_b = set(uni_b)
print(set_uni_b, '\n', len(set_uni_b))
fout = open('d:/python/double_dno/make_list_for_sql_out_function/distinct_uni_b_export.txt', 'w')

print(pre_querry, file=fout, end='')
print(filter_in_querry, 'in(', file=fout)
max_len = 0
# cause in sql navigator max size of list in operator in could be 1000
if len(set_uni_b) >= 999:
    erased_items_file = open('d:/python/double_dno/make_list_for_sql_out_function/erased_numbers.txt', 'w')
    for index in range(0, len(set_uni_b) - 999):
        erased_item = set_uni_b.pop()
        print('"', erased_item, '"', file=erased_items_file, sep='')
    erased_items_file.close()
        
for index in range(len(set_uni_b)):
    current_item = set_uni_b.pop()
    if len(set_uni_b) == max_len:
        print("'", current_item, "'",sep='',file=fout) 
    else:
        print("'", current_item, "',",sep='',file=fout) 
        
print(')', file=fout)
print(post_querry, file=fout)
fout.close()
