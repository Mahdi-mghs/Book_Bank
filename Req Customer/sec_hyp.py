import numpy as np
import pandas as pd
import scipy.stats as stats

df = pd.read_csv('All_books.csv')

hardcover_prices = df[df['types'] != 'شومیز']['current_price']
paperback_prices = df[df['types'] == 'شومیز']['current_price']

t_stat, p_value = stats.ttest_ind(hardcover_prices, paperback_prices, equal_var=False)
print("t status:", t_stat)
print("p value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("تفاوت معناداری در قیمت کتب با جلد سخت و جلد شومیز وجود دارد.")
else:
    print("تفاوت معناداری در قیمت کتب با جلد سخت و جلد شومیز وجود ندارد.")

# Mann-whitney Testing
statistic, p_value_mw = stats.mannwhitneyu(hardcover_prices, paperback_prices)

print("t status:", t_stat)
print("p value:", p_value)

if p_value_mw < alpha:
    print("توزیع معناداری در قیمت کتب با جلد سخت و جلد شومیز وجود دارد.")
else:
    print("توزیع معناداری در قیمت کتب با جلد سخت و جلد شومیز وجود ندارد.")