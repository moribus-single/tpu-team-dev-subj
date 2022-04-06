"""
PATTERN of any metric:
    SOME_NAME_OF_METRIC = {
        'DESC': 'SOME DESCRIPTION OF THE METRIC',
        'QUERY': 'QUERY TO DATABASE'
    }

INSTRUCTION: for adding new one, just copy PATTERN above and paste after existing metrics.
NOTE: do not forget to change description and query.
"""


class Metrics:
    AVG_MARK_BY_GROUPS = {
        'DESC': 'Average mark of group',
        'QUERY': 'SELECT * FROM av_marks'
    }
