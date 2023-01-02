from datetime import  timedelta ,datetime
from icecream import ic
import numpy as np
def split_log_record(df_list):
    date = []
    time = []
    for x in range(len(df_list)):
        date_time = df_list[x][0]
        record = date_time.split(" ")
        date_ = record[0]
        time_ = record[1]
        date.append(date_)
        time.append(time_)
    return date , time

def convert_str_time(time):
    time = datetime.strptime(time,"%H:%M:%S")
    return time


def seperate_first_second_and_third_shift(df_list,third_shift_buffer_time_in, third_shift_buffer_time_out,first_second_shift_bufffer_time_in,first_second_shift_bufffer_time_out):
    first_second = []
    third = []
    for x in range(len(df_list)):
        current_time = convert_str_time( df_list[x][4])
        punch_code = df_list[x][0]
        if (current_time > third_shift_buffer_time_in and punch_code == 'in') or (current_time < third_shift_buffer_time_out and punch_code == 'out'):
            third.append(df_list[x])
        else:
            first_second.append(df_list[x])


        # if (current_time > third_shift_buffer_time_in and punch_code == 'in'):
        #     third.append(df_list[x])
        #     print(current_time,third_shift_buffer_time_in,punch_code,df_list[x][2],df_list[x][3],"third_in")
        # elif (current_time < third_shift_buffer_time_out and punch_code == 'out'):
        #     third.append(df_list[x])
        #     print(current_time,third_shift_buffer_time_out,punch_code,df_list[x][2],df_list[x][3],"third_out")
        # elif (current_time > first_second_shift_bufffer_time_in and punch_code == 'in'):
        #     first_second.append(df_list[x])
        #     print(current_time,first_second_shift_bufffer_time_in,punch_code,df_list[x][2],df_list[x][3],"first_second_in")
        # elif (current_time < first_second_shift_bufffer_time_out and punch_code == 'out'):
        #     first_second.append(df_list[x])
        #     print(current_time,first_second_shift_bufffer_time_out,punch_code,df_list[x][2],df_list[x][3],"first_second_out")
    return first_second , third

def in_empty_out_not_empty(out_data):
    manually_verify = []
    emp_code = out_data["emp_code"][0]
    emp_name = out_data["emp_name"][0]
    out_date = out_data["date"][0]
    out_date_time = out_data["time"][0]
    in_date = np.nan
    in_date_time = np.nan
    td = np.nan
    return emp_code,emp_name,in_date,in_date_time,out_date,out_date_time,td



def out_empty_in_not_empty(in_data):
    in_complete_row = []
    emp_code = in_data["emp_code"][0]
    emp_name = in_data["emp_name"][0]
    in_date = in_data["date"][0]
    in_date_time = in_data["time"][0]
    out_date = np.nan
    out_date_time = np.nan
    td = np.nan
    return emp_code,emp_name,in_date,in_date_time,out_date,out_date_time,td
    

def in_not_empty_and_out_not_empty(in_data,out_data):
    row = []
    emp_code = in_data["emp_code"][0]
    emp_name = in_data["emp_name"][0]
    in_date = in_data["date"][0]
    in_date_time = in_data["time"][0]
    out_date = out_data["date"][0]
    out_date_time = out_data["time"][0]
    in_day_date_time = in_date+' '+ in_date_time
    in_day_date_time = in_day_date_time
    out_day_date_time = out_date + ' ' + out_date_time
    out_day_date_time = out_day_date_time
    in_day_date_time = str_time(in_day_date_time)
    out_day_date_time = str_time(out_day_date_time)
    muster_time = out_day_date_time - in_day_date_time
    sec = (muster_time.total_seconds())
    td = str(timedelta(seconds=sec))
    return emp_code,emp_name,in_date,in_date_time,out_date,out_date_time,td
    

def str_time(time):
    time = datetime.strptime(time,"%d-%b-%Y %H:%M:%S")
    return time


def third_shift_in_out_present(in_data,out_data):
    row = []
    emp_code = in_data["emp_code"][0]
    emp_name = in_data["emp_name"][0]
    current_day_in_date = in_data["date"][0]
    current_day_in_time = in_data["time"][0]
    next_day_out_date = out_data["date"].tail(1).reset_index().drop(columns="index")
    next_day_out_date = next_day_out_date["date"][0]
    next_day_out_time = out_data["time"].tail(1).reset_index().drop(columns="index")
    next_day_out_time = next_day_out_time["time"][0]
    in_day_date_time = current_day_in_date + ' '+current_day_in_time
    in_day_date_time = str_time(in_day_date_time)
    out_day_date_time = next_day_out_date + ' '+ next_day_out_time
    out_day_date_time = str_time(out_day_date_time)
    muster_time_ = out_day_date_time - in_day_date_time
    sec = muster_time_.total_seconds()
    td = str(timedelta(seconds=sec))
    return emp_code,emp_name,current_day_in_date,current_day_in_time,next_day_out_date,next_day_out_time,td
    

def duplicate_in():
    pass

def duplicate_out():
    pass