pre_querry = '''select switch_id, uni_a, uni_b, bill_dtm, duration, cdr_set,
 inc_tg, to_char(bill_dtm,'yyyymmdd'),
 substr(service_type,0,1), out01, out02, out03, out04, outblock, segment_a
from ms_lvv.calls
where
bill_dtm between to_date(' 01.09.2020 00:00:00 ','dd.mm.yyyy hh24:mi:ss')
              and to_date(' 01.10.2020 00:00:00 ','dd.mm.yyyy hh24:mi:ss')

and '''
#uni_a in(

post_querry = '''group by switch_id, uni_a, uni_b, bill_dtm, duration, cdr_set,
 inc_tg, to_char(bill_dtm,'yyyymmdd'),
 substr(service_type,0,1), out01, out02, out03, out04, outblock, segment_a
'''


fin = open('d:/python/double_dno/make_list_for_sql_in_function/export.tsv')
uni_a = list(map(str.rstrip, fin.readlines()))
print(uni_a)
for index in range(len(uni_a)):
    uni_a[index] = uni_a[index].strip('"')
print(uni_a)
filter_in_querry = 'UNI_A'
if uni_a[0] in ('UNI_A', 'UNI_B'):
    filter_in_querry = uni_a[0]
    uni_a = uni_a[1:]
print(uni_a, '\n', len(uni_a))
set_uni_a = set(uni_a)
print(set_uni_a, '\n', len(set_uni_a))
fout = open('d:/python/double_dno/make_list_for_sql_in_function/distinct_uni_a_new 3.txt', 'w')

print(pre_querry, file=fout, end='')
print(filter_in_querry, 'in(', file=fout)
max_len = 0
# cause in sql navigator max size of list in operator in could be 1000
if len(set_uni_a) >= 999:
    erased_items_file = open('d:/python/double_dno/make_list_for_sql_in_function/erased_numbers.txt', 'w')
    for index in range(0, len(set_uni_a) - 999):
        erased_item = set_uni_a.pop()
        print('"', erased_item, '"', file=erased_items_file, sep='')
    erased_items_file.close()
        
for index in range(len(set_uni_a)):
    current_item = set_uni_a.pop()
    if len(set_uni_a) == max_len:
        print("'", current_item, "'",sep='',file=fout) 
    else:
        print("'", current_item, "',",sep='',file=fout) 
        
print(')', file=fout)
print(post_querry, file=fout)
fout.close()
