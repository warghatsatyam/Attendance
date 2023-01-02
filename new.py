from utils import seperate_first_second_and_third_shift ,convert_str_time ,in_empty_out_not_empty,out_empty_in_not_empty,in_not_empty_and_out_not_empty,third_shift_in_out_present
from icecream import ic
import pandas as pd
dummy_data = [
    #multiple in and no out 
    ['in','1','DASHARATH','01-Nov-2022','8:22:32'],
    ['in','1','DASHARATH','01-Nov-2022','8:23:32'],
    ['in','1','DASHARATH','01-Nov-2022','8:25:32'],
    ['in','1','DASHARATH','01-Nov-2022','8:27:32'],
    ['in','1','DASHARATH','01-Nov-2022','8:28:32'],
    
    # multiple in and single out 
    ['in', '101', 'NAGENDRA KUMAR', '01-Nov-2022', '6:52:39'],
    ['in', '101', 'NAGENDRA KUMAR', '01-Nov-2022', '6:52:41'],
    ['in', '101', 'NAGENDRA KUMAR', '01-Nov-2022', '6:52:43'],
    ['out', '101', 'NAGENDRA KUMAR', '01-Nov-2022', '22:21:13'],
    # single in and multiple out
    ['in', '101', 'NAGENDRA KUMAR',  '02-Nov-2022', '14:37:49'],
    ['out', '101', 'NAGENDRA KUMAR', '02-Nov-2022', '22:44:04'],
    ['out', '101', 'NAGENDRA KUMAR', '02-Nov-2022', '22:50:04'],
    ['out', '101', 'NAGENDRA KUMAR', '02-Nov-2022', '23:44:04'],
    # multiple in and multiple out
    ['in', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '14:45:43'],
    ['in', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '14:49:43'],
    ['in', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '14:50:43'],
    ['out', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '22:44:53'],
    ['out', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '22:54:53'],
    ['out', '106', 'BAIJNATH DUBEY', '14-Nov-2022', '22:59:53'],
    # 0 in and out or multiple out
    ['out', '109', 'RAJU RAJBHAR', '08-Nov-2022', '15:03:19'],
    ['out', '109', 'RAJU RAJBHAR', '08-Nov-2022', '15:13:19'],
    ['out', '109', 'RAJU RAJBHAR', '08-Nov-2022', '15:23:19'],
    ['out', '109', 'RAJU RAJBHAR', '08-Nov-2022', '15:33:19'],
    # proper in and out pair third shift
    ['in', '111', 'SUHAS JADHAV', '25-Nov-2022', '22:30:51'],
    ['out', '111', 'SUHAS JADHAV', '26-Nov-2022', '7:07:36'],
    ['in','111', 'SUHAS JADHAV', '27-Nov-2022', '22:34:34'],
    ['out', '111', 'SUHAS JADHAV', '28-Nov-2022', '7:07:42'],

    # multiple in and no out
    ['in','111', 'SANJAY K. GANGAWANE', '19-Nov-2022', '22:34:34'],
    ['in','111', 'SANJAY K. GANGAWANE', '19-Nov-2022', '22:34:34'],
    
    # multiple out and no in 
    ['out', '111', 'SUHAS JADHAV', '20-Nov-2022', '7:07:42'],
    ['out', '111', 'SUHAS JADHAV', '20-Nov-2022', '7:17:42'],

    # multiple in and single out 
    ['in','111', 'SANJAY K. GANGAWANE', '21-Nov-2022', '22:34:34'],
    ['in','111', 'SANJAY K. GANGAWANE', '21-Nov-2022', '22:40:34'],
    ['out', '111', 'SUHAS JADHAV', '22-Nov-2022', '7:07:42'],

    # multiple out and single in

    ['in','111', 'SANJAY K. GANGAWANE', '22-Nov-2022', '22:34:34'],
    ['out', '111', 'SUHAS JADHAV', '23-Nov-2022', '7:07:42'],
    ['out', '111', 'SUHAS JADHAV', '23-Nov-2022', '7:17:42'],

    
]


first_second = []
third = []

third_in =  convert_str_time('20:00:00')
third_out = convert_str_time('8:00:00')

first_in = convert_str_time('06:00:00')
first_out = convert_str_time('23:00:00')

first_second_ , third_ = seperate_first_second_and_third_shift(dummy_data,third_in,third_out,first_in,first_out)

dummy_data_df = pd.DataFrame(dummy_data,columns=["punch_code","emp_code","emp_name","date","time"])
first_second_df = pd.DataFrame(first_second_,columns=["punch_code","emp_code","emp_name","date","time"])
third_df = pd.DataFrame(third_,columns=["punch_code","emp_code","emp_name","date","time"])

unique_first_second_user = first_second_df["emp_code"].unique()
unique_third_user = third_df["emp_code"].unique()
unique_date = dummy_data_df["date"].unique()


row = []
in_complete_row = []
for x in range(len(unique_first_second_user)):
    for y in range(len(unique_date)):
        emp_code_grouped = first_second_df[first_second_df["emp_code"] == unique_first_second_user[x]]
        emp_code_grouped_date = emp_code_grouped[emp_code_grouped["date"] == unique_date[y]]
        in_data = emp_code_grouped_date[emp_code_grouped_date["punch_code"] == 'in'].reset_index().drop(columns="index")
        out_data = emp_code_grouped_date[emp_code_grouped_date["punch_code"] == 'out'].reset_index().drop(columns="index")
        if in_data.empty and not out_data.empty:
            emp_code,emp_name,in_date,in_time,out_date,out_date_time,td = in_empty_out_not_empty(out_data)
            in_complete_row.append([emp_code,emp_name,in_date,in_time,out_date,out_date_time,td])
        if out_data.empty and not in_data.empty:
            emp_code,emp_name,in_date,in_time,out_date,out_date_time,td = out_empty_in_not_empty(in_data)
            in_complete_row.append([emp_code,emp_name,in_date,in_time,out_date,out_date_time,td])
        if not in_data.empty and not out_data.empty:
            emp_code,emp_name,in_date,in_time,out_date,out_date_time,td = in_not_empty_and_out_not_empty(in_data,out_data)
            row.append([emp_code,emp_name,in_date,in_time,out_date,out_date_time,td])

for x in range(len(unique_third_user)):
    for y in range(len(unique_date)-1):
        emp_code_grouped = third_df[third_df["emp_code"] == unique_third_user[x]]
        emp_code_grouped_date = emp_code_grouped[emp_code_grouped["date"] == unique_date[y]]
        emp_code_grouped_next_date = emp_code_grouped[emp_code_grouped["date"] == unique_date[y+1]]
        in_data = emp_code_grouped_date[emp_code_grouped_date["punch_code"] == 'in'].reset_index().drop(columns="index")
        out_data = emp_code_grouped_next_date[emp_code_grouped_next_date["punch_code"] == 'out'].reset_index().drop(columns="index")

        if in_data.empty and not out_data.empty:
            pass
        if out_data.empty and not in_data.empty:
            pass
        if not in_data.empty and not out_data.empty:
            emp_code,emp_name,in_date,in_time,out_date,out_date_time,td = third_shift_in_out_present(in_data,out_data)
            row.append([emp_code,emp_name,in_date,in_time,out_date,out_date_time,td])


final_df = pd.DataFrame(row,columns=["emp_code","emp_name","in_date","in_time","out_date","out_time","muster_time"])
final_incomple_df = pd.DataFrame(in_complete_row,columns=["emp_code","emp_name","in_date","in_time","out_date","out_time","muster_time"])

print(final_df)
print(final_incomple_df)

# for x in range(len(in_complete_row)):
#     ic(in_complete_row[x])

# for y in range(len(row)):
#     print(row[y])