from minted.models import Category

def generate_category_pie_chart_dataset(categories, start_date, end_date):
    pie_labels = []
    pie_data = []

    for category in categories:
        total_expenses_for_category = int(category.get_total_expenses_for_category(date_from=start_date, date_to=end_date))

        pie_labels.append(category.name)
        pie_data.append(total_expenses_for_category)
    
    category_pie_chart_data = {
        'labels': pie_labels,
        'data': pie_data
    }

    return category_pie_chart_data

def get_category_expenses_for_time_interval(category, time_interval, start_date, end_date):
    # only from python 3.10 onwards
    # match time_interval:
    #     case 'yearly':
    #         return category.get_yearly_expenses_for_category(date_from = start_date, date_to = end_date)
    #     case 'monthly':
    #         return category.get_monthly_expenses_for_category(date_from = start_date, date_to = end_date)
    #     case 'weekly':
    #         return category.get_weekly_expenses_for_category(date_from = start_date, date_to = end_date)
    #     case _:
    #         return category.get_daily_expenses_for_category(date_from = start_date, date_to = end_date)

    if time_interval == 'yearly':
        expenses = category.get_yearly_expenses_for_category(date_from = start_date, date_to = end_date)
    elif time_interval == 'monthly':
        expenses = category.get_monthly_expenses_for_category(date_from = start_date, date_to = end_date)
    elif time_interval == 'weekly':
        expenses = category.get_weekly_expenses_for_category(date_from = start_date, date_to = end_date)
    else:
        expenses = category.get_daily_expenses_for_category(date_from = start_date, date_to = end_date)
    
    return expenses

def generate_category_line_chart_dataset(categories, start_date, end_date, time_interval):
    line_dataset = []
    for category in categories:
        
        expenses = get_category_expenses_for_time_interval(category, time_interval, start_date, end_date)

        line_dataset.append({
            'category_name': category.name,
            'expenses_per_time': expenses
        })
    
    line_data = []
    for item in line_dataset:
        data=[]
        for date, expense in item['expenses_per_time'].items():
            data.append({
                'x':date,
                'y':expense
            })
        
        data_points = {
            'label': item['category_name'],
            'data': data,
            'fill': False,
            'borderColor': '',
            'backgroundColor': '',
            'pointHoverRadius': 8,
            'pointHoverBorderColor': 'white',
            'pointBorderColor': 'white',
            'pointStyle': 'rectRot',
        }
        
        line_data.append(data_points)
    
    
    category_line_chart_data = {
        #'labels':list(all_dates.keys()), 
        'labels':list(expenses.keys()),
        'datasets': line_data
    }

    return category_line_chart_data