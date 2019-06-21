class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_log = {}
        digit_log = []

        for log in logs:
            i = log.index(" ")
            val = log[i + 1:]
            if val[0].isdigit():
                digit_log.append(log)
            else:
                letter_log[log] = val

        sorted_letter_log = sorted(letter_log, key=lambda x: (letter_log[x], x))

        return sorted_letter_log + digit_log