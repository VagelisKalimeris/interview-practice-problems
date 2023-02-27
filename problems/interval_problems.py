from data_structures.interval import Interval


################################################################################
# Objective         : Given a list of intervals, sorted by starting timestamps #
#                     merge all the overlapping intervals to produce a list    #
#                     that has only mutually exclusive intervals.              #
# Time Complexity   : O(n)                                                     #
# Space Complexity  : O(1)                                                     #
################################################################################
def merge_overlapping_intervals(intervals):
    interval_count = len(intervals)

    # Edge cases, one or none intervals given
    if interval_count in (0, 1):
        return intervals

    inter_a, result = intervals[0], []
    for i in range(1, interval_count):
        inter_b = intervals[i]
        if inter_a.overlaps(inter_b):
            inter_a = inter_a & inter_b
            if i == interval_count - 1:
                result.append(inter_a)
            elif not inter_a.overlaps(intervals[i + 1]):
                result.append(inter_a)
                inter_a = intervals[i + 1]
        else:
            result.append(inter_a)
            if i == interval_count - 1:
                result.append(inter_b)
            inter_a = inter_b

    return result

