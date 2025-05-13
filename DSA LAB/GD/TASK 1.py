def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_end_time = -1
    
    for activity in activities:
        if activity[0] >= last_end_time:
            selected_activities.append(activity)
            last_end_time = activity[1]
    
    return selected_activities


