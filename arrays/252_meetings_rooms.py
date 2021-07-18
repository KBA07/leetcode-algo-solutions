"""
Given an array of meetings with start and end index, return if a person can attend all the meetings
"""

def attendMeetings(meetings):
    start_list = []
    end_list = []

    for meeting in meetings:
        s, e = meeting

        start_list.append(s)
        end_list.append(e)

    start_list.sort()
    end_list.sort()

    for index in range(len(start_list) - 1):
        if end_list[index] > start_list[index + 1]:
            return False
    
    return True