

#1 3 5 7 8 10 12 - 31
#4 6 9 11 - 30
#2 - 28

li_31 = [0, 2, 4 ,6 ,7, 9, 11]
li_30 = [3, 5, 8, 10]
li_28 = [1]
li_29 = [1]

def day_range(month, leap = None):
    if month in li_31:
        return 31
    elif month in li_30:
        return 30
    elif month in li_29 and leap == True:
        return 29
    elif month in li_28:
        return 28
    else:
        return("Error")

def month_rain_getter(month_array, leap = None):
    num = 1
    month_arr = []
    if leap == True:
        for months in range(0,12):
            r_month_df = month_array[num: num+day_range(months, leap = True)]
            num = num + day_range(months, leap = True)
            month_sum = 0
            month_sum = sum(r_month_df)
            #month_mean = month_sum*0.5
            #month_arr = np.append(month_arr, month_mean)
            month_arr.append(month_sum)
        return month_arr
        
    else :
        for months in range(0,12):
            r_month_df = month_array[num: num+day_range(months)]
            num = num + day_range(months)
            month_sum = 0
            month_sum = sum(r_month_df)
            #month_mean = month_sum*0.5
            #month_arr = np.append(month_arr, month_mean)
            month_arr.append(month_sum)
        return month_arr

def week_rain_getter(week_array, leap = None):
    num = 0
    week_sum_arr = []
    while num < len(week_array):
        r_month_df = week_array[num: num+7]
        num = num + 7
        week_sum = 0
        week_sum = sum(r_month_df)
        week_sum_arr.append(week_sum)
    return week_sum_arr


def month_getter(month_array, leap = None):
    num = 1
    month_arr = []
    if leap == True:
        for months in range(0,12):
            r_month_df = month_array[num: num+day_range(months, leap = True)]
            num = num + day_range(months, leap = True)
            month_arr.append(r_month_df)
        return month_arr
        
    else :
        for months in range(0,12):
            r_month_df = month_array[num: num+day_range(months)]
            num = num + day_range(months)
            month_arr.append(r_month_df)
        return month_arr

def week_getter(week_array, leap = None):
    num = 0
    week_arr = []
    while num < len(week_array):
        r_month_df = week_array[num: num+7]
        num = num + 7
        week_arr.append(r_month_df)
    return week_arr

def seasonal_getter(months_arr):
    num = 0
    seas_arr = []
    for num in range(0, 12):
        if num%12 == 0:
            r_seas = months_arr[num: num + 3]
            seas_arr.append(r_seas)
        elif num == 3:
            r_seas = months_arr[num: num + 2]
            seas_arr.append(r_seas)
        elif num == 5:
            r_seas = months_arr[num: num + 4]
            seas_arr.append(r_seas)
        elif num == 9:
            r_seas = months_arr[num: num + 3]
            seas_arr.append(r_seas)
    return seas_arr

def season_sum(season_arr):
    sum_arr = []

    for inc_sum in range(0, 40):
        se_sum = 0
        se_sum = sum(season_arr[inc_sum])
        sum_arr.append(se_sum)
    return sum_arr