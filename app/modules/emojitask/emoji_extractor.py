import emoji as em
import re
from collections import defaultdict

def get_most_freq_emojis(comments_list, count = 5):
    text = em.demojize(' '.join(comments_list))
    text = re.findall(r'(:[!_\-\w]+:)', text)
    list_emoji = [em.emojize(x) for x in text]

    all_emojis_count = defaultdict(int)

    for emoji in list_emoji:
        all_emojis_count[emoji] += 1

    sorted_emojis_count = [k for k, v in sorted(all_emojis_count.items(), key = lambda item: item[1], reverse = True)]
    return sorted_emojis_count[:count]
